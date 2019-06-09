# -*- coding: utf-8 -*-
# Advanced zoom for images of various types from small to huge up to several GB
import math
import warnings
import tkinter as tk
import glob
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import pandas as pd
from tabulate import tabulate
import pytablewriter

def pprint_df(dframe):
    print (tabulate(dframe, headers='keys', tablefmt='psql', showindex=True))
def to_markdown(df):
    writer = pytablewriter.MarkdownTableWriter()
    writer.table_name = "example_table"
    writer.header_list = list(df.columns.values)
    writer.value_matrix = df.values.tolist()
    writer.write_table()

class AutoScrollbar(Scrollbar):
    """ A scrollbar that hides itself if it's not needed. Works only for grid geometry manager """

    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise tk.TclError(
            'Cannot use pack with the widget ' + self.__class__.__name__)

    def place(self, **kw):
        raise tk.TclError(
            'Cannot use place with the widget ' + self.__class__.__name__)


class CanvasImage:
    """ Display and zoom image """

    def __init__(self, placeholder, path):
        """ Initialize the ImageFrame """
        self.imscale = 1.0  # scale for the canvas image zoom, public for outer classes
        self.__delta = 1.3  # zoom magnitude
        # could be: NEAREST, BILINEAR, BICUBIC and ANTIALIAS
        self.__filter = Image.ANTIALIAS
        self.__previous_state = 0  # previous state of the keyboard
        self.path = path  # path to the image, should be public for outer classes
        # Create ImageFrame in placeholder widget
        # placeholder of the ImageFrame object
        self.__imframe = Frame(placeholder)
        # Vertical and horizontal scrollbars for canvas
        hbar = AutoScrollbar(self.__imframe, orient='horizontal')
        vbar = AutoScrollbar(self.__imframe, orient='vertical')
        hbar.grid(row=1, column=0, sticky='we')
        vbar.grid(row=0, column=1, sticky='ns')
        # Create canvas and bind it with scrollbars. Public for outer classes
        self.canvas = tk.Canvas(self.__imframe, highlightthickness=0,
                                xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.update()  # wait till canvas is created
        # bind scrollbars to the canvas
        hbar.configure(command=self.__scroll_x)
        vbar.configure(command=self.__scroll_y)
        # Bind events to the Canvas
        # canvas is resized
        self.canvas.bind('<Configure>', lambda event: self.__show_image())
        # remember canvas position
        self.canvas.bind('<ButtonPress-1>', self.__move_from)
        # move canvas to the new position
        self.canvas.bind('<B1-Motion>',     self.__move_to)
        # zoom for Windows and MacOS, but not Linux
        self.canvas.bind('<MouseWheel>', self.__wheel)
        # zoom for Linux, wheel scroll down
        self.canvas.bind('<Button-5>',   self.__wheel)
        # zoom for Linux, wheel scroll up
        self.canvas.bind('<Button-4>',   self.__wheel)
        # Handle keystrokes in idle mode, because program slows down on a weak computers,
        # when too many key stroke events in the same time
        self.canvas.bind('<Key>', lambda event: self.canvas.after_idle(
            self.__keystroke, event))
        # Decide if this image huge or not
        self.__huge = False  # huge or not
        self.__huge_size = 14000  # define size of the huge image
        self.__band_width = 1024  # width of the tile band
        # suppress DecompressionBombError for the big image
        Image.MAX_IMAGE_PIXELS = 1000000000
        with warnings.catch_warnings():  # suppress DecompressionBombWarning
            warnings.simplefilter('ignore')
            # open image, but down't load it
            self.__image = Image.open(self.path)
        self.imwidth, self.imheight = self.__image.size  # public for outer classes
        if self.imwidth * self.imheight > self.__huge_size * self.__huge_size and \
           self.__image.tile[0][0] == 'raw':  # only raw images could be tiled
            self.__huge = True  # image is huge
            self.__offset = self.__image.tile[0][2]  # initial tile offset
            self.__tile = [self.__image.tile[0][0],  # it have to be 'raw'
                           # tile extent (a rectangle)
                           [0, 0, self.imwidth, 0],
                           self.__offset,
                           self.__image.tile[0][3]]  # list of arguments to the decoder
        # get the smaller image side
        self.__min_side = min(self.imwidth, self.imheight)
        # Create image pyramid
        self.__pyramid = [self.smaller()] if self.__huge else [
            Image.open(self.path)]
        # Set ratio coefficient for image pyramid
        self.__ratio = max(self.imwidth, self.imheight) / \
            self.__huge_size if self.__huge else 1.0
        self.__curr_img = 0  # current image from the pyramid
        self.__scale = self.imscale * self.__ratio  # image pyramide scale
        self.__reduction = 2  # reduction degree of image pyramid
        w, h = self.__pyramid[-1].size
        while w > 512 and h > 512:  # top pyramid image is around 512 pixels in size
            w /= self.__reduction  # divide on reduction degree
            h /= self.__reduction  # divide on reduction degree
            self.__pyramid.append(
                self.__pyramid[-1].resize((int(w), int(h)), self.__filter))
        # Put image into container rectangle and use it to set proper coordinates to the image
        self.container = self.canvas.create_rectangle(
            (0, 0, self.imwidth, self.imheight), width=0)
        self.__show_image()  # show image on the canvas
        self.canvas.focus_set()  # set focus on the canvas

    def smaller(self):
        """ Resize image proportionally and return smaller image """
        w1, h1 = float(self.imwidth), float(self.imheight)
        w2, h2 = float(self.__huge_size), float(self.__huge_size)
        aspect_ratio1 = w1 / h1
        aspect_ratio2 = w2 / h2  # it equals to 1.0
        if aspect_ratio1 == aspect_ratio2:
            image = Image.new('RGB', (int(w2), int(h2)))
            k = h2 / h1  # compression ratio
            w = int(w2)  # band length
        elif aspect_ratio1 > aspect_ratio2:
            image = Image.new('RGB', (int(w2), int(w2 / aspect_ratio1)))
            k = h2 / w1  # compression ratio
            w = int(w2)  # band length
        else:  # aspect_ratio1 < aspect_ration2
            image = Image.new('RGB', (int(h2 * aspect_ratio1), int(h2)))
            k = h2 / h1  # compression ratio
            w = int(h2 * aspect_ratio1)  # band length
        i, j, n = 0, 1, round(0.5 + self.imheight / self.__band_width)
        while i < self.imheight:
            print('\rOpening image: {j} from {n}'.format(j=j, n=n), end='')
            # width of the tile band
            band = min(self.__band_width, self.imheight - i)
            self.__tile[1][3] = band  # set band width
            self.__tile[2] = self.__offset + self.imwidth * \
                i * 3  # tile offset (3 bytes per pixel)
            self.__image.close()
            self.__image = Image.open(self.path)  # reopen / reset image
            # set size of the tile band
            self.__image.size = (self.imwidth, band)
            self.__image.tile = [self.__tile]  # set tile
            cropped = self.__image.crop(
                (0, 0, self.imwidth, band))  # crop tile band
            image.paste(cropped.resize((w, int(band * k)+1),
                                       self.__filter), (0, int(i * k)))
            i += band
            j += 1
        print('\r' + 30*' ' + '\r', end='')  # hide printed string
        return image

    def redraw_figures(self):
        """ Dummy function to redraw figures in the children classes """
        pass

    def grid(self, **kw):
        """ Put CanvasImage widget on the parent widget """
        self.__imframe.grid(**kw)  # place CanvasImage widget on the grid
        self.__imframe.grid(sticky='nswe')  # make frame container sticky
        self.__imframe.rowconfigure(0, weight=1)  # make canvas expandable
        self.__imframe.columnconfigure(0, weight=1)

    def pack(self, **kw):
        """ Exception: cannot use pack with this widget """
        raise Exception('Cannot use pack with the widget ' +
                        self.__class__.__name__)

    def place(self, **kw):
        """ Exception: cannot use place with this widget """
        raise Exception('Cannot use place with the widget ' +
                        self.__class__.__name__)

    # noinspection PyUnusedLocal
    def __scroll_x(self, *args, **kwargs):
        """ Scroll canvas horizontally and redraw the image """
        self.canvas.xview(*args)  # scroll horizontally
        self.__show_image()  # redraw the image

    # noinspection PyUnusedLocal
    def __scroll_y(self, *args, **kwargs):
        """ Scroll canvas vertically and redraw the image """
        self.canvas.yview(*args)  # scroll vertically
        self.__show_image()  # redraw the image

    def __show_image(self):
        """ Show image on the Canvas. Implements correct image zoom almost like in Google Maps """
        box_image = self.canvas.coords(self.container)  # get image area
        box_canvas = (self.canvas.canvasx(0),  # get visible area of the canvas
                      self.canvas.canvasy(0),
                      self.canvas.canvasx(self.canvas.winfo_width()),
                      self.canvas.canvasy(self.canvas.winfo_height()))
        # convert to integer or it will not work properly
        box_img_int = tuple(map(int, box_image))
        # Get scroll region box
        box_scroll = [min(box_img_int[0], box_canvas[0]), min(box_img_int[1], box_canvas[1]),
                      max(box_img_int[2], box_canvas[2]), max(box_img_int[3], box_canvas[3])]
        # Horizontal part of the image is in the visible area
        if box_scroll[0] == box_canvas[0] and box_scroll[2] == box_canvas[2]:
            box_scroll[0] = box_img_int[0]
            box_scroll[2] = box_img_int[2]
        # Vertical part of the image is in the visible area
        if box_scroll[1] == box_canvas[1] and box_scroll[3] == box_canvas[3]:
            box_scroll[1] = box_img_int[1]
            box_scroll[3] = box_img_int[3]
        # Convert scroll region to tuple and to integer
        self.canvas.configure(scrollregion=tuple(
            map(int, box_scroll)))  # set scroll region
        # get coordinates (x1,y1,x2,y2) of the image tile
        x1 = max(box_canvas[0] - box_image[0], 0)
        y1 = max(box_canvas[1] - box_image[1], 0)
        x2 = min(box_canvas[2], box_image[2]) - box_image[0]
        y2 = min(box_canvas[3], box_image[3]) - box_image[1]
        if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
            if self.__huge and self.__curr_img < 0:  # show huge image
                h = int((y2 - y1) / self.imscale)  # height of the tile band
                self.__tile[1][3] = h  # set the tile band height
                self.__tile[2] = self.__offset + \
                    self.imwidth * int(y1 / self.imscale) * 3
                self.__image.close()
                self.__image = Image.open(self.path)  # reopen / reset image
                # set size of the tile band
                self.__image.size = (self.imwidth, h)
                self.__image.tile = [self.__tile]
                image = self.__image.crop(
                    (int(x1 / self.imscale), 0, int(x2 / self.imscale), h))
            else:  # show normal image
                image = self.__pyramid[max(0, self.__curr_img)].crop(  # crop current img from pyramid
                    (int(x1 / self.__scale), int(y1 / self.__scale),
                     int(x2 / self.__scale), int(y2 / self.__scale)))
            #
            imagetk = ImageTk.PhotoImage(image.resize(
                (int(x2 - x1), int(y2 - y1)), self.__filter))
            self.imageid = self.canvas.create_image(max(box_canvas[0], box_img_int[0]),
                                               max(box_canvas[1],
                                                   box_img_int[1]),
                                               anchor='nw', image=imagetk)
            self.canvas.lower(self.imageid)  # set image into background
            # keep an extra reference to prevent garbage-collection
            self.canvas.imagetk = imagetk

    def __move_from(self, event):
        """ Remember previous coordinates for scrolling with the mouse """
        self.canvas.scan_mark(event.x, event.y)

    def __move_to(self, event):
        """ Drag (move) canvas to the new position """
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.__show_image()  # zoom tile and show it on the canvas

    def outside(self, x, y):
        """ Checks if the point (x,y) is outside the image area """
        bbox = self.canvas.coords(self.container)  # get image area
        if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]:
            return False  # point (x,y) is inside the image area
        else:
            return True  # point (x,y) is outside the image area

    def __wheel(self, event):
        """ Zoom with mouse wheel """
        x = self.canvas.canvasx(
            event.x)  # get coordinates of the event on the canvas
        y = self.canvas.canvasy(event.y)
        if self.outside(x, y):
            return  # zoom only inside image area
        scale = 1.0
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:  # scroll down, smaller
            if round(self.__min_side * self.imscale) < 30:
                return  # image is less than 30 pixels
            self.imscale /= self.__delta
            scale /= self.__delta
        if event.num == 4 or event.delta == 120:  # scroll up, bigger
            i = min(self.canvas.winfo_width(), self.canvas.winfo_height()) >> 1
            if i < self.imscale:
                return  # 1 pixel is bigger than the visible area
            self.imscale *= self.__delta
            scale *= self.__delta
        # Take appropriate image from the pyramid
        k = self.imscale * self.__ratio  # temporary coefficient
        self.__curr_img = min(
            (-1) * int(math.log(k, self.__reduction)), len(self.__pyramid) - 1)
        self.__scale = k * math.pow(self.__reduction, max(0, self.__curr_img))
        #
        self.canvas.scale('all', x, y, scale, scale)  # rescale all objects
        # Redraw some figures before showing image on the screen
        self.redraw_figures()  # method for child classes
        self.__show_image()

    def __keystroke(self, event):
        """ Scrolling with the keyboard.
            Independent from the language of the keyboard, CapsLock, <Ctrl>+<key>, etc. """
        if event.state - self.__previous_state == 4:  # means that the Control key is pressed
            pass  # do nothing if Control key is pressed
        else:
            self.__previous_state = event.state  # remember the last keystroke state
            # Up, Down, Left, Right keystrokes
            if event.keycode in [68, 39, 102]:  # scroll right, keys 'd' or 'Right'
                self.__scroll_x('scroll',  1, 'unit', event=event)
            elif event.keycode in [65, 37, 100]:  # scroll left, keys 'a' or 'Left'
                self.__scroll_x('scroll', -1, 'unit', event=event)
            elif event.keycode in [87, 38, 104]:  # scroll up, keys 'w' or 'Up'
                self.__scroll_y('scroll', -1, 'unit', event=event)
            elif event.keycode in [83, 40, 98]:  # scroll down, keys 's' or 'Down'
                self.__scroll_y('scroll',  1, 'unit', event=event)

    def crop(self, bbox):
        """ Crop rectangle from the image and return it """
        if self.__huge:  # image is huge and not totally in RAM
            band = bbox[3] - bbox[1]  # width of the tile band
            self.__tile[1][3] = band  # set the tile height
            self.__tile[2] = self.__offset + self.imwidth * \
                bbox[1] * 3  # set offset of the band
            self.__image.close()
            self.__image = Image.open(self.path)  # reopen / reset image
            # set size of the tile band
            self.__image.size = (self.imwidth, band)
            self.__image.tile = [self.__tile]
            return self.__image.crop((bbox[0], 0, bbox[2], band))
        else:  # image is totally in RAM
            return self.__pyramid[0].crop(bbox)

    def destroy(self):
        """ ImageFrame destructor """
        self.__image.close()
        map(lambda i: i.close, self.__pyramid)  # close all pyramid images
        del self.__pyramid[:]  # delete pyramid list
        del self.__pyramid  # delete pyramid variable
        self.canvas.destroy()
        self.__imframe.destroy()


class MainWindow(Frame):
    """ Main window class """

    def __init__(self, mainframe, path):
        """ Initialize the main Frame """
        Frame.__init__(self, master=mainframe)
        self.master.title('Verificação de Requisitos')
        # self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
        for r in range(10):
            self.master.rowconfigure(r, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.frame_img = Frame(self.master, bg="gray")
        self.frame_img.grid(row=0, column=0, rowspan=6, sticky=W+E+N+S)

        self.frame_content = Frame(self.master, bg="gray10")
        self.frame_content.grid(row=6, column=0, rowspan=4, sticky=W+E+N+S)
        
        self.frame_img.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
        self.frame_img.columnconfigure(0, weight=1)

        for i in range(8):
            self.frame_content.rowconfigure(i, weight=1)
            
        for i in range(10):
            self.frame_content.columnconfigure(i, weight=1)
        
        self.frame_buttons = Frame(self.frame_content, bg="gray20")
        self.frame_buttons.grid(row=7, column=0, columnspan=10, sticky=W+E+N+S)
        self.frame_texts = Frame(self.frame_content, bg="#000")
        self.frame_texts.grid(row=0, column=0, rowspan=7, columnspan=10, sticky=W+E+N+S)
        for i in range(10):
            self.frame_buttons.columnconfigure(i, weight=1)
            self.frame_texts.columnconfigure(i, weight=1)
        for i in range(7):
            self.frame_texts.rowconfigure(i, weight=1)
        self.frame_buttons.rowconfigure(0, weight=1)

        self.grade = 0;
        self.all_questions = [];
        self.all_imgs = [];
        self.all_dfs_checklist = []
        self.all_dfs_justifications = []

        self.question = '';
        self.verifying = '';

        self.uncheck = PhotoImage(file="uncheck.png")
        self.uncheck_btn = Button(self.frame_buttons, command= lambda: self.apply_grade('X'))
        self.uncheck_btn.config(image=self.uncheck, width="31", height="31",   background='#ccc', bd=0, highlightbackground='#000')
        self.uncheck_btn.grid(row=0, column=0)

        self.check = PhotoImage(file="check.png")
        self.check_btn = Button(self.frame_buttons, command=  lambda: self.apply_grade('&#10003;'))
        self.check_btn.config(image=self.check, width="31", height="31", background='#ccc', bd=0, highlightbackground='#000')
        self.check_btn.grid(row=0, column=1)

        self.sr = PhotoImage(file=".imgs/sr/favicon-32x32.png")
        self.sr_btn = Button(self.frame_buttons, command= lambda: self.apply_grade('0'))
        self.sr_btn.config(image=self.sr, width="31", height="31", background='#363636', bd=0, highlightbackground='#232323')
        self.sr_btn.grid(row=0, column=2)

        self.ii = PhotoImage(file=".imgs/ii/favicon-32x32.png")
        self.ii_btn = Button(self.frame_buttons, command= lambda: self.apply_grade('2'))
        self.ii_btn.config(image=self.ii, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.ii_btn.grid(row=0, column=3)

        self.mi = PhotoImage(file=".imgs/mi/favicon-32x32.png")
        self.mi_btn = Button(self.frame_buttons, command= lambda: self.apply_grade('4'))
        self.mi_btn.config(image=self.mi, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.mi_btn.grid(row=0, column=4)

        self.mm = PhotoImage(file=".imgs/mm/favicon-32x32.png")
        self.mm_btn = Button(self.frame_buttons, command= lambda: self.apply_grade('6'))
        self.mm_btn.config(image=self.mm, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.mm_btn.grid(row=0, column=5)

        self.ms = PhotoImage(file=".imgs/ms/favicon-32x32.png")
        self.ms_btn = Button(self.frame_buttons, command= lambda: self.apply_grade('8'))
        self.ms_btn.config(image=self.ms, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.ms_btn.grid(row=0, column=6)

        self.ss = PhotoImage(file=".imgs/ss/favicon-32x32.png")
        self.ss_btn = Button(self.frame_buttons, command= lambda: self.apply_grade('10'))
        self.ss_btn.config(image=self.ss, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.ss_btn.grid(row=0, column=7)

        self.retrieve_questions()

        self.question = Label(self.frame_texts) 
        self.question.configure(background='#363636', foreground='#FFFFDB', padx=10, pady=5, bd=2.5, relief=FLAT)
        self.question.grid(row= 4,column= 3,columnspan= 3,rowspan=2)
        self.artifact = Label(self.frame_texts) 
        self.artifact.configure(background='#000', foreground='#fbfbfb', padx=10, pady=5, bd=2.5, relief=FLAT)
        self.artifact.grid(row= 1,column=4 ,columnspan=1 ,rowspan=1 )
        self.theme = Label(self.frame_texts) 
        self.theme.configure(background='#000', foreground='#fbfbfb', padx=10, pady=5, bd=2.5, relief=FLAT)
        self.theme.grid(row=0 ,column=4 ,columnspan=1 ,rowspan=1 )
        self.js = Label(self.frame_texts) 
        self.js.configure(background='#000', foreground='#fbfbfb', padx=10, pady=5, bd=2.5, relief=FLAT)
        self.js.grid(row=4 ,column=9 ,columnspan=1 ,rowspan=1 )
        self.js["text"]='Justificativa (para notas menores que 10)'
        self.nota = Label(self.frame_buttons) 
        self.nota.configure(background='#000', foreground='#fbfbfb', padx=10, pady=5, bd=2.5, relief=FLAT)
        self.nota.grid(row=0 ,column=8)
        self.nota["text"]='Nota:'
        
        self.it_img = [0,0]
        self.it_quest = [0,0]

        current_img = self.all_imgs[self.it_img[0]][self.it_img[1]]
        artifact = current_img.split('/')[-1].strip('.png')
        theme = current_img.split('/')[-2]

        self.canvas = CanvasImage(self.frame_img, current_img)  # create widget
        self.canvas.grid(row=0, column=0)  # show widget
        self.display_text(self.question, self.all_questions[0][0])
        self.display_text(self.artifact, artifact)
        self.display_text(self.theme, theme)
        
        vcmd = (self.master.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.grade = tk.Entry(self.frame_buttons, validate = 'key', validatecommand = vcmd)
        self.grade.grid(row=0, column=9, ipady=2)
        
        self.justify = tk.Text(self.frame_texts, height=8, width=60)
        self.justify.grid(row=5, column=9, columnspan=2)
        
        self.grade.bind('<Return>', self.get_val)
        self.grade_text = ''
        self.justify_text = ''
        
    def retrieve_input(self):
        self.justify_text = self.justify.get("1.0",'end-1c')



    def get_val(self, event):
        self.grade_text=str(self.grade.get()) # construct string
        self.grade.delete('0', 'end')
        self.apply_grade(self.grade_text)
        
        print(to_markdown(self.all_dfs_checklist[0].reset_index()))
        for k, v in self.all_dfs_justifications[0].items():
            print(self.all_dfs_justifications[0][k].to_string())

    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789':
            return True
        else:
            return False

    def get_name(self, n):
        return n.split('/')[-1].strip('.png')
    def retrieve_questions(self, ext='.txt', base='vis/'):
        end = '/*/*'+ext
        it = 0
        for current_filename in glob.iglob(base+end, recursive=True):
            theme = current_filename.split('/')[-2]
            questions = open(current_filename).read().split('\n')
            self.all_questions.append(questions) # add all "perguntas.txt"
            self.all_imgs.append([x.lstrip('./') for x in  glob.glob('./vis/{0}/*.png'.format(theme))])
            no_questions = list(filter(None,questions))
            n = {'artefatos':[self.get_name(n) for n in self.all_imgs[it]]}
            for i in range(len(no_questions)):
                n[i+1]=''
            print(n) 
            df = pd.DataFrame(n)
            df=df.set_index('artefatos')
            print (list(df))
            self.all_dfs_checklist.append(df)

            dfs = {}
            for n in self.all_imgs[it]: 
                z = {'Justificativa':''}
                x = self.get_name(n)
                z[x]=[i+1 for i in range(len(no_questions))]
                df = pd.DataFrame(z)
                df = df.set_index(x)
                dfs[x]=df
                
            self.all_dfs_justifications.append(dfs)

            # xd = pd.DataFrame({'CN001':[2, 6, 11],'JUSTIFICATIVA':''})
            # xd.set_index('CN001')
            # xd.at[2,'JUSTIFICATIVA']='ola'
            # xd=xd[xd.JUSTIFICATIVA != '']

            it+=1
        return

    def display_text(self, text, current_question):
        text.configure(font=Font(family="Helvetica", size=15))
        text["text"] = current_question

    def apply_grade (self, nota):
        print(nota)
        self.retrieve_input()
        artifact = self.get_name(self.all_imgs[self.it_img[0]][self.it_img[1]])
        self.all_dfs_checklist[self.it_img[0]].at[artifact,self.it_quest[1]+1]=nota
        self.all_dfs_justifications[self.it_img[0]][artifact].at[self.it_quest[1]+1,'Justificativa']=self.justify_text.replace('\n', r'<br />')
        self.justify_text=''
        self.justify.delete('1.0', 'end')

        self.it_img[1]+=1
        if len(self.all_imgs[self.it_img[0]]) == self.it_img[1]:
            self.it_img[1]=0
            self.it_quest[1]+=1

        if self.it_quest[1] == len(self.all_questions[self.it_quest[0]]):
            self.it_img[0]+=1
            self.it_img[1]=0
            self.it_quest[0]+=1
            self.it_quest[1]=0
        current_img = self.all_imgs[self.it_img[0]][self.it_img[1]]
        self.change_img(current_img)
        artifact = self.get_name(current_img)
        theme = current_img.split('/')[-2]
        self.display_text(self.question, self.all_questions[self.it_quest[0]][self.it_quest[1]])
        self.display_text(self.theme, theme)
        self.display_text(self.artifact, artifact)

        return

    def change_img(self, path):
        self.canvas.destroy()
        self.canvas = CanvasImage(self.frame_img, path)  # create widget
        self.canvas.grid(row=0, column=0)

filename = 'vis/iStar_SR/SR05_Doar_Ribons_V2.png'  # place path to your image here

root = tk.Tk()
screen_width = int(root.winfo_screenwidth()*0.65)
screen_height = int(root.winfo_screenheight()*0.8)
root.geometry("{0}x{1}".format(screen_width, screen_height))
app = MainWindow(root, path=filename)
app.mainloop()
