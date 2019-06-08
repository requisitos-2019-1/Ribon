from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import json
import glob
import ast

class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1366x768')

        self.frame = Frame(self.root, bd=2, relief=SUNKEN)

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.xscrollbar = Scrollbar(self.frame, orient=HORIZONTAL)
        self.xscrollbar.grid(row=1, column=0, sticky=E+W)

        self.yscrollbar = Scrollbar(self.frame)
        self.yscrollbar.grid(row=0, column=1, sticky=N+S)

        self.grade = 0;
        self.all_questions = [];
        self.all_imgs = [];
        self.question = '';
        self.verifying = '';

        self.uncheck = PhotoImage(file="uncheck.png")
        self.uncheck_btn = Button(self.root, command=self.apply_grade)
        self.uncheck_btn.config(image=self.uncheck, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.uncheck_btn.place(x=390, y=730, anchor=W)

        self.check = PhotoImage(file="check.png")
        self.check_btn = Button(self.root, command=self.apply_grade)
        self.check_btn.config(image=self.check, width="31", height="31", background='#363636', bd=0, highlightbackground='#232323')
        self.check_btn.place(x=480, y=730, anchor=W)

        self.ii = PhotoImage(file=".imgs/ii/favicon-32x32.png")
        self.ii_btn = Button(self.root, command=self.apply_grade)
        self.ii_btn.config(image=self.ii, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.ii_btn.place(x=570, y=730, anchor=W)

        self.mi = PhotoImage(file=".imgs/mi/favicon-32x32.png")
        self.mi_btn = Button(self.root, command=self.apply_grade)
        self.mi_btn.config(image=self.mi, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.mi_btn.place(x=660, y=730, anchor=W)

        self.mm = PhotoImage(file=".imgs/mm/favicon-32x32.png")
        self.mm_btn = Button(self.root, command=self.apply_grade)
        self.mm_btn.config(image=self.mm, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.mm_btn.place(x=750, y=730, anchor=W)

        self.ms = PhotoImage(file=".imgs/ms/favicon-32x32.png")
        self.ms_btn = Button(self.root, command=self.apply_grade)
        self.ms_btn.config(image=self.ms, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.ms_btn.place(x=840, y=730, anchor=W)

        self.ss = PhotoImage(file=".imgs/ss/favicon-32x32.png")
        self.ss_btn = Button(self.root, command=self.apply_grade)
        self.ss_btn.config(image=self.ss, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.ss_btn.place(x=930, y=730, anchor=W)
        
        self.frame.pack()
        self.retrieve_questions()
        self.question = Text(self.root) 
        self.question.configure(background='#363636', spacing2=2, foreground='#FFFFDB', wrap=WORD, padx=10, pady=5, bd=2.5, relief=FLAT)
        self.artifact = Text(self.root) 
        self.artifact.configure(background='#FBFBFB', spacing2=2, foreground='#000', wrap=WORD, padx=10, pady=5, bd=2.5, relief=FLAT)
        self.theme = Text(self.root) 
        self.theme.configure(background='#FBFBFB', spacing2=2, foreground='#000', wrap=WORD, padx=10, pady=5, bd=2.5, relief=FLAT)



        self.it_img = [0,0]

        self.it_quest = [0,0]

        self.canvas = Canvas(self.frame, bd=0, xscrollcommand=self.xscrollbar.set,
                yscrollcommand=self.yscrollbar.set, width=1366, height=568)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
        self.img = ImageTk.PhotoImage(Image.open(self.all_imgs[self.it_img[0]][self.it_img[1]]))
        self.current_image = self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        self.display_text(self.question, self.all_questions[0][0])
        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)
        # print(json.dumps(ast.literal_eval(str(self.all_questions)), indent=4))
        # print(self.all_questions["Argumentacao"][0])
        # self.root.after(500, self.xd)
        self.root.mainloop()

    def retrieve_questions(self, ext='.txt', base='vis/'):
        end = '/*/*'+ext
        for current_filename in glob.iglob(base+end, recursive=True):
            theme = current_filename.split('/')[-2]
            self.all_questions.append(open(current_filename).read().split('\n')) # add all "perguntas.txt"
            self.all_imgs.append([x.lstrip('./') for x in  glob.glob('./vis/{0}/*.png'.format(theme))])
        return

    def display_text(self, text, current_question, wid=0.6, hei=0.10, x=0.585, y=0.85):
        self.begin_edit(text)
        text.configure(font=Font(family="Helvetica", size=16))
        text.insert(END, current_question)
        text.place(relwidth = wid, relheight = hei, relx = x, rely = y, anchor=CENTER)
        self.end_edit(text)

    def apply_grade (self):
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
        self.img = ImageTk.PhotoImage(Image.open(current_img))
        self.change_img()
        artifact = current_img.split('/')[-1].strip('.png')
        theme = current_img.split('/')[-2]
        self.display_text(self.question, self.all_questions[self.it_quest[0]][self.it_quest[1]])
        self.display_text(self.artifact, artifact, x=0.125, hei=0.06, wid=0.20, y=0.90)
        self.display_text(self.theme, theme, x=0.1, hei=0.06, wid=0.15, y=0.82)

        return

    def begin_edit(self, text):
        text.config(state=NORMAL)
        text.delete(1.0, END)

    def end_edit(self, text):
        text.config(state=DISABLED)
    def change_img(self):
        self.canvas.itemconfig(self.current_image, image = self.img)

app = App()

## passar argumentos pra func é: widget.after(10, self.runBackup, mybackup)