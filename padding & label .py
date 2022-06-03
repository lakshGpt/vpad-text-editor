# if we apply padding to labels then it is automatically apply to the entry box

import tkinter as tk
from tkinter import ttk
"""
win = tk.Tk()
win.title('padding and label')

labels = ['what is your name :','what is your age :','what is your gender :','country :','state :','city :']

for i in range(len(labels)):
    cur_label = 'label'+str(i)
    cur_label = ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W,padx=4,pady=2)

user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
    }
counter = 0
for i in user_info: 
    cur_entrybox = 'entry'+i
    cur_entrybox = ttk.Entry(win,width=16,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1,padx=4,pady=2)
    counter += 1

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())           
    

submit_btn = ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=6,columnspan=3)
"""
# for label frame
win = tk.Tk()
win.title('label frame')

label_frame = ttk.LabelFrame(win,text='enter your details below')
label_frame.grid(row=0,column=0,padx=10,pady=0)

labels = ['what is your name :','what is your age :','what is your gender :','country :','state :','city :']

for i in range(len(labels)):
    cur_label = 'label'+str(i)
    cur_label = ttk.Label(label_frame,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar()
    }
counter = 0
for i in user_info: 
    cur_entrybox = 'entry'+i
    cur_entrybox = ttk.Entry(label_frame,width=16,textvariable=user_info[i])
    cur_entrybox.grid(row=counter,column=1)
    counter += 1

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get()) 

submit_btn = ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,columnspan=2)

 # -> label frame class has a method called winfo_children which gives list of all widgets present on label frame
for child in label_frame.winfo_children():
    child.grid_configure(padx=4,pady=2) 

win.mainloop()