# from database import calculate_attendence, save_file_absent, save_file_present
from tkinter import *
import datetime
import os
import tkinter.messagebox as msg
from PIL import Image,ImageTk

__root__ = Tk()
__root__.geometry("600x600")

# Adding a icon for the GUI

# pic = Image.open("icon.jpeg")

# picture = ImageTk.PhotoImage(image=pic)

# __root__.iconphoto(False,picture)

__root__.title("AMS")
__root__.maxsize(600,600)
__root__.minsize(600,600)
# "25 50 9"
# ["25","50","9"]
# [25,50,9]
lst = []

def mark_present():
    input = str(txt1.get(1.0,END))

    lst = input.splitlines()

    int_list = []

    for a in lst:

        int_list.append(int(a))
    
    # save_file_present(int_list)
    quit()

def mark_absent():
    text = txt1.get(1.0,END)
    lst = text.splitlines()
    int_list = []

    for a in lst:
        int_list.append(int(a))

    # save_file_absent(int_list)
    quit()

def clear_text():
    txt1.delete(1.0,END)

# Ishaan Pathak
#
#

# ["Ishaan Pathak","",""]
def calculate():
    name_input = txt1.get(1.0,END)
    name = name_input.splitlines()
    # result =  calculate_attendence(name[0])
    
    # msg.showinfo("Attendence",f"{name[0]} has {result} % Attendence")
    quit()
    
# Creating A Heading using canvas

canvas = Canvas(__root__,width=600,height=100)
canvas.pack()

canvas.create_text(300,30,text="Attendence Management System",font="Times 16 bold italic")

# Creating Date Frame in the setting

date = Frame(__root__)
date.pack()

date_label = Label(date,text=f"{datetime.date.today()}") 
date_label.pack()
# Now creating a TextBox and placing it at the end of the GUI

frmM = Frame(__root__)
frmM.pack(padx=10,pady=10,side=BOTTOM)


lb1 = Listbox(frmM) # as a replacement for Label
lb1.pack()
txt1 = Text(lb1,height=10,font="Times 16 bold italic")
txt1.pack()

frm = Frame(frmM)
frm.pack()

btn1 = Button(frm,text="Present",command=mark_present)
btn1.grid(row=1,column=1,padx=20)
btn2 = Button(frm,text="Absent",command=mark_absent)
btn2.grid(row=1,column=2)
btn3 = Button(frm,text="QUIT",command=quit)
btn3.grid(row=1,column=3,padx=20)
btn4 = Button(frm,text="clear",command=clear_text)
btn4.grid(row=1,column=4)
btn5 = Button(frm,text="Calculate Attendence",command=calculate)
btn5.grid(row=1,column=5,padx=20)

if __name__ == "__main__":
    __root__.mainloop()