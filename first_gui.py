# pyton tkinter tutorial

# starter code
#import tkinter
#from tkinter import *
import tkinter as tk        # preferable
from tkinter import ttk
from csv import DictWriter
import os
#win = tkinter.Tk()
win = tk.Tk()
win.title('GUI')

# create labels
# widgets --> label,buttons,radio buttons -- ttk has better design than tk
name_label = ttk.Label(win,text = 'enter your name :')
name_label.grid(row=0,column=0, sticky=tk.W)

age_label = ttk.Label(win,text = 'enter your age :')
age_label.grid(row=1,column=0 , sticky=tk.W)

email_label = ttk.Label(win,text = 'enter your email :')
email_label.grid(row=2,column=0 , sticky=tk.W)

gender_label = ttk.Label(win,text = 'select your gender :')
gender_label.grid(row=3,column=0,sticky=tk.W)

# create entry box for labels
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=16, textvariable = name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width=16, textvariable = age_var)
age_entrybox.grid(row=1,column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width=16, textvariable = email_var)
email_entrybox.grid(row=2,column=1)

# create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width = 13,textvariable = gender_var , state = 'readonly')
gender_combobox['values'] = ('Male','Female','Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

# create radio button
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text = 'student', value='student', variable=usertype)
radiobtn1.grid(row=4,column=0,sticky = tk.W)

radiobtn2 = ttk.Radiobutton(win,text='faculty',value='faculty',variable=usertype)
radiobtn2.grid(row=4,column=1,sticky = tk.W)

#radiobtn3 = ttk.Radiobutton(win,text='other staff',value='other staff',variable=usertype)
#radiobtn3.grid(row=4,column=2,sticky = tk.W)

# create check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win,text = 'check if you want to submit or not and make it clear',variable = checkbtn_var)
checkbtn.grid(row=5,columnspan=3)


# create button

#def action():
#    username = name_var.get()
#    userage = age_var.get()
#    user_email = email_var.get()
#    usergender = gender_var.get()
#    user_type = usertype.get()
#    if checkbtn_var.get() == 0:
#        submit = 'NO'
#    else:
#        submit = 'YES'
    
    #print(f" name :{username}")
    #print(f" age :{ userage}")
    #print(f" email_add :{user_email}")
    #print(f" gender :{usergender}")
    #print(f" type :{user_type}")
    #print(f"submit :{submit}")

#    with open('file.txt','a') as f:
#        f.write(f'{username},{userage},{user_email},{usergender},{user_type},{submit}\n')
    
#    name_entrybox.delete(0,tk.END)
#    age_entrybox.delete(0,tk.END)
#    email_entrybox.delete(0,tk.END)

    # changing color of labels
#    name_label.configure(foreground='#1157D9')
#    age_label.configure(foreground='#1157D9')
#    email_label.configure(foreground='#1157D9')
#    submit_button.configure(foreground='#2F1694')

# write to csv files
def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    usergender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        submit = 'NO'
    else:
        submit = 'YES'

    with open('file1.csv','a',newline='') as f:  
        dict_writer = DictWriter(f,fieldnames=['User Name','User email','user age','user gender','user type','submit'])
        if os.stat('file1.csv').st_size==0:
            dict_writer.writeheader()

        dict_writer.writerow({
            'User Name' : username,
            'User email' : user_email,
            'user age' : userage,
            'user gender' : usergender,
            'user type' : user_type,
            'submit' : submit,
        })

    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='#1157D9')



submit_button = tk.Button(win,text = 'Submit',command = action)
submit_button.grid(row=6,column=0)



win.mainloop()      
 # -> to run our gui application infinite times and  want user to close gui window by himself 
