# notebook -- contain two pages
# page 1                    page2
# widgets                   widgets

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('TAB controller')
nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1,text='ONE')
nb.add(page2,text='two')
#nb.grid(row=0,column=0)
nb.pack(expand=True,fill='both')

label1 = ttk.Label(page1,text='this is label :')
label1.grid(row=0,column=0)
entrybx1 = ttk.Entry(page1,width=16)
entrybx1.grid(row=0,column=1)

label2 = ttk.Label(page2,text='this is label :')
label2.grid(row=0,column=0)
entrybx2 = ttk.Entry(page2,width=16)
entrybx2.grid(row=0,column=1)
win.mainloop()