
import tkinter as tk
from tkinter import ttk
import os
win = tk.Tk()
win.title('create menubar')

def func(): 
    print('func called')

 # -> for menubar python have Menu class

 # ------------------ simple menu bar -----------------
#menubar = tk.Menu(win)
#menubar.add_command(label='Save',command=func)
#menubar.add_command(label='Save As',command=func)
#menubar.add_command(label='Copy',command=func)
#menubar.add_command(label='Paste',command=func)

 # -> for drop down menu bar
main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label='New File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator()
file_menu.add_command(label='Save File',command=func)
main_menu.add_cascade(label='File',menu=file_menu)

edit_menu = tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Copy',command=func)
edit_menu.add_command(label='cut',command=func)
edit_menu.add_separator()
edit_menu.add_command(label='paste',command=func)
main_menu.add_cascade(label='Edit',menu=edit_menu)


win.config(menu=main_menu)


win.mainloop()
