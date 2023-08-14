from tkinter import *
cal=Tk()

cal.geometry("400x650")
cal.title("Calculator")


def click(event):
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get()) 

        scvalue.set(value)
        int(screen.update())        
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

def click1(event):
    global value
    text1 = event.widget.cget("text")
    if scvalue.get().isdigit():
        screen.update()

    square = (int(scvalue.get()) * int(scvalue.get()))

    if text1 == "x²":
        scvalue.set(square)
        

scvalue=StringVar()
scvalue.set("")
screen=Entry(cal,textvar=scvalue,font="lucida 35 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f1=Frame(cal,bg="grey")
b1=Button(f1,text="C",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="%",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="x²",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click1)
b1=Button(f1,text="/",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(cal,bg="grey")
b1=Button(f1,text="7",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="8",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="9",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="*",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(cal,bg="grey")
b1=Button(f1,text="4",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="5",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="6",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="-",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(cal,bg="grey")
b1=Button(f1,text="3",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="2",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="1",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="+",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

f1=Frame(cal,bg="grey")
b1=Button(f1,text="00",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="0",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text=".",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
b1=Button(f1,text="=",height=2,width=4,font="lucida 25 bold")
b1.pack(side=LEFT)
b1.bind("<Button-1>",click)
f1.pack()

cal.mainloop()