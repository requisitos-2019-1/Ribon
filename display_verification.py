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

        self.canvas = Canvas(self.frame, bd=0, xscrollcommand=self.xscrollbar.set,
                        yscrollcommand=self.yscrollbar.set, width=1366, height=568)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
        File1 = "vis/Protocolo/protocolo.png"
        File2 = "vis/Backlog/backlog_de_produto.png"
        self.img1 = ImageTk.PhotoImage(Image.open(File1))
        self.img2 = ImageTk.PhotoImage(Image.open(File2))
        self.current_image = self.canvas.create_image(0, 0, image=self.img1, anchor="nw")
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)

        self.grade = 0;
        self.all_questions = [];
        self.question = '';
        self.verifying = '';

        self.uncheck = PhotoImage(file="uncheck.png")
        self.uncheck_btn = Button(self.root, command=self.apply_grade)
        self.uncheck_btn.config(image=self.uncheck, width="31", height="31",   background='#363636', bd=0, highlightbackground='#232323')
        self.uncheck_btn.place(x=390, y=730, anchor=W)

        self.check = PhotoImage(file="check.png")
        self.check_btn = Button(self.root, command=self.change_theme0)
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
        self.text_showed = Text(self.root) 
        self.text_showed.configure(background='#363636', spacing2=2, foreground='#FFFFDB', wrap=WORD, padx=10, pady=5, bd=2.5, relief=FLAT)
        self.rsvp_display(self.all_questions[0][0])
        # print(json.dumps(ast.literal_eval(str(self.all_questions)), indent=4))
        # print(self.all_questions["Argumentacao"][0])
        # self.root.after(500, self.xd)
        self.root.mainloop()

    def retrieve_questions(self, ext='.txt', base='vis/'):
        end = '/*/*'+ext
        for current_filename in glob.iglob(base+end, recursive=True):
            self.verifying = current_filename.split('/')[-1].split('.txt')[0]
            self.all_questions.append(open(current_filename).read().split('\n'))
            # current_dir = '/'.join(current_filename.split('/')[:-1])+'/'
            # glob.glob('./*.txt')


        return

    def rsvp_display(self, current_question):
        self.begin_edit()
        self.text_showed.configure(font=Font(family="Helvetica", size=16))
        self.text_showed.insert(END, current_question)
        self.text_showed.place(relwidth = 0.40, relheight = 0.07, relx = 0.5, rely = 0.85, anchor=CENTER)
        self.end_edit()

    def change_theme0(self):
        print('iae')
        return
    def apply_grade (self):
        print('iai')
        return

    def begin_edit(self):
        self.text_showed.config(state=NORMAL)
        self.text_showed.delete(1.0, END)

    def end_edit(self):
        self.text_showed.config(state=DISABLED)
    def xd(self):
        self.canvas.itemconfig(self.current_image, image = self.img2)

app = App()

## passar argumentos pra func é: widget.after(10, self.runBackup, mybackup)