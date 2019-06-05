from tkinter import *
from PIL import Image, ImageTk


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
        File1 = "vis/shot.png"
        File2 = "vis/User_Stories/backlog.png"
        self.img1 = ImageTk.PhotoImage(Image.open(File1))
        self.img2 = ImageTk.PhotoImage(Image.open(File2))
        self.current_image = self.canvas.create_image(0, 0, image=self.img1, anchor="nw")
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        self.xscrollbar.config(command=self.canvas.xview)
        self.yscrollbar.config(command=self.canvas.yview)

        self.check = PhotoImage(file="check.png")

        self.check_btn = Button(self.root, command=self.change_theme0)
        self.check_btn.config(image=self.check, width="31", height="31",
                         background='#363636', bd=0, highlightbackground='#232323')
        self.check_btn.place(x=680, y=730, anchor=W)

        self.uncheck = PhotoImage(file="uncheck.png")

        self.uncheck_btn = Button(self.root, command=self.change_theme1)
        self.uncheck_btn.config(image=self.uncheck, width="31", height="31",
                           background='#363636', bd=0, highlightbackground='#232323')
        self.uncheck_btn.place(x=590, y=730, anchor=W)

        self.current_question = ''

        self.frame.pack()
        self.root.after(500, self.xd)
        self.root.mainloop()

    # def retrieve_questions(self, path, depth=1, ext='.md', base='Verificação/'):
    #     end = '/*'*depth+ext
    #     for current_filename in glob.iglob(base+path+end, recursive=True):
    #         model = current_filename.split('/')[-1].split('Verificação_')[-1].split('.md')[0]
            
    #     perguntas='''
    #     1 - Os itens classificados estão realmente de acordo com a prioridade que devia estar?
    #     2 - Existe duplicidade de requisitos?
    #     3 - Existe Rastro do requisito?
    #     4 - Existe ambiguidade na escrita do requisito?
    #     '''.split('\n')
    #     return

    # def rsvp_display(self, current_question):
	# 	self.begin_edit()
	# 	self.text_showed.configure(font=self.text_font_rsvp)
	# 	self.text_showed.insert(END, current_question)
	# 	self.text_showed.place(relwidth = 0.60, relheight = 0.11, relx = 0.45, rely = 0.4, anchor=CENTER)
	# 	self.end_edit()

    def change_theme0(self):
        print('iae')
        return
    def change_theme1(self):
        print('iai')
        return

    def xd(self):
        self.canvas.itemconfig(self.current_image, image = self.img2)

app = App()

## passar argumentos pra func é: widget.after(10, self.runBackup, mybackup)