from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)

def f_start():
    pass


root = Tk()
root.title('PhotoSort')
root.geometry('400x100+450+200')

frame = Frame(root, bg='#56ADFF', bd=5)
frame.pack(pady=10, padx=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, ipady=2, expand=1, fill=X)

btn_diag = ttk.Button(frame, text='Обрати папку', command=choose_dir)
btn_diag.pack(side=RIGHT, padx=5)

btn_start = ttk.Button(root, text='Старт', command=f_start)
btn_start.pack(fill=X, padx=10)

root.mainloop()
