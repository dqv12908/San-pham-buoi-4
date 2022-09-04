from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image,ImageTk

def login():
    pass
def forget():
    pass

wn = Tk()
wn.geometry("500x700")
wn.title("window1")
wn.config(background="#5e99f7")


Title = Label(wn,text="LOGIN",font=("Arial Black",30),background="#5e99f7")
username = Label(wn,text="Username:",font=("Arial Black",15),pady=20,background="#5e99f7")
entry1 = Entry(wn,font=("Arial Black",15),width=20,background="white")
passqord = Label(wn,text="Password:",font=("Arial Black",15),pady=20,background="#5e99f7")
entry2 = Entry(wn,font=("Arial Black",15),width=20,background="white",show="*")
login_btn = Button(wn,text="LOGIN",font=("Arial Black",15),command=login)
login_btn.configure(width = 10, activebackground = "#33B5E5")
forgetpassword = Button(wn,text="FORGET PASSWORD",font=("Arial Black",15),command=forget)
combobox = Combobox(wn,width=30)
combobox['values']=("Hanoi","Hai Phong","Ho Chi Minh ")
combobox.current(0)
combobox.grid(column=0,row=4)
img = Image.open()

Title.grid(column=0,row=0)
username.grid(column=0,row=1)
entry1.grid(column=1,row=1)
passqord.grid(column=0,row=2)
entry2.grid(column=1,row=2)
login_btn.grid(column=0,row=3)
forgetpassword.grid(column=1,row=3)

wn.mainloop()