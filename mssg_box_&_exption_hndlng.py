import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk()
win.title('mssg_box_&_exption_hndlng')

label_frame = ttk.Labelframe(win,text='contact details')
label_frame.grid(row=0,column=0,padx=40,pady=10)

name_label = ttk.Label(label_frame,text='enter your name please :',font=('Helvetica',10,'bold'))
age_label = ttk.Label(label_frame,text='enter your age please :',font=('Helvetica',10,'bold'))

name_var  = tk.StringVar()
age_var  = tk.StringVar()

name_entry = ttk.Entry(label_frame,width=24,textvariable=name_var)
age_entry = ttk.Entry(label_frame,width=24,textvariable=age_var)

name_label.grid(row=0,column=0,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,pady=5,padx=5,sticky=tk.W)
age_entry.grid(row=1,column=1,pady=5,padx=5,sticky=tk.W)

def submit():
    #m_box.showerror('title','content of the this message box !!')
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('error','Please fill both name and age !!')
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror('title','only digits are allowed in age field')
        else:
            if age < 18:
                m_box.showwarning('warning','you are below 18 years old')
            print(f'{name} : {age}')
        

submit_btn = ttk.Button(win,text='submit',command=submit)
submit_btn.grid(row=1,columnspan=2,padx=40)
win.mainloop()