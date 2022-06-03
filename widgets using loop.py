import tkinter as tk
from tkinter import ttk
import os

win = tk.Tk()
win.title('LOOP')

labels = ['what is your name :','what is your age :','what is your gender :','country :','state :','city :']

for i in range(len(labels)):
    cur_label = 'label'+str(i)
    cur_label = ttk.Label(win,text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

    # entry box
    #cur_var = tk.StringVar()
    #cur_entrybox = ttk.Entry(win,width=16,textvariable=cur_var)
    #cur_entrybox.grid(row=i,column=1)

# entry box - we use dictionary for this
#name_var = tk.StringVar()
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
submit_btn.grid(row=6,columnspan=3)

win.mainloop()
