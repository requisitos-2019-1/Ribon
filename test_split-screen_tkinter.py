from tkinter import *

root = Tk()
root.geometry("600x400")

# left = Frame(root, borderwidth=2, relief="solid")
# right = Frame(root, borderwidth=2, relief="solid")

# label2 = Label(right, text="I could be a button")
# label3 = Label(right, text="So could I")


# # container.pack(expand=True, fill="both", padx=5, pady=5)
# # box1.pack(expand=True, fill="both", padx=10, pady=10)
# # box2.pack(expand=True, fill="both", padx=10, pady=10)
# left.pack(side="top", expand=True, fill="both", width=root.winfo_width(), height=0.7*root.winfo_height())
# right.pack(side="bottom", expand=True, fill="both")
# label2.pack()
# label3.pack()
# root.update()
# left.config(width=root.winfo_width(), height=0.7*root.winfo_height()) #doing this will keep the width of your frame
# right.config(width=root.winfo_width(), height=0.3*root.winfo_height()) #doing this will keep the width of your frame
# root.update()

root.title("Grid Manager")
root.grid()

for r in range(10):
    root.rowconfigure(r, weight=1)    
for c in range(5):
    root.columnconfigure(c, weight=1)

Frame1 = Frame(root, bg="red")
Frame1.grid(row = 0, column = 0, rowspan = 7, columnspan = 5, sticky = W+E+N+S) 

Frame3 = Frame(root, bg="green")
Frame3.grid(row = 7, column = 0, rowspan = 9, columnspan = 5, sticky = W+E+N+S)

for c in range(5):
    Button(root, text="Button {0}".format(c)).grid(row=10,column=c,sticky=E+W)

root.mainloop()