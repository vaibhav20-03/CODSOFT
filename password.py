from tkinter import *
from random import randint

def generate():
    dis2.delete(0,END)
    len=int(dis1.get())
    mypass=""

    for x in range(len):
       mypass+=chr(randint(33,126))

    dis2.insert(0,mypass)       

paswrd=Tk()
paswrd.title("Password Generator")
paswrd.geometry("500x300")



lab1=LabelFrame(paswrd,text="How many characters?",font=("lucida 15 bold"))
lab1.pack(pady=20)

dis1=Entry(lab1,font=("lucida 25 bold"))
dis1.pack(pady=20,padx=20)

dis2=Entry(paswrd,text="" ,font=("lucida 25 bold"),bd=0,bg="systembuttonface")
dis2.pack(pady=20,padx=20)

frm=Frame(paswrd)
frm.pack(pady=20)

button1=Button(frm,text="Generate Password!",font=("lucida 15 bold"),command=generate)
button1.pack(pady=1,padx=1)

paswrd.mainloop()


