from tkinter import *
root = Tk()
root.geometry("500x550")
root.minsize(500,550)
root.maxsize(500,600)
def click(event):
    text= event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text == "AC":
        val = scvalue.get()
        scvalue.set(val[0:len(val)-1])
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root.title("Calculator ---> Avani Baheti")
root.wm_iconbitmap("icon1.ico")
scvalue=StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 22 bold")
screen.pack(fill=X,padx=10,pady=12,ipadx=9)
f=Frame(root,bg="black")
b=Button(f,text="9",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 20 bold",padx=18,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="6",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text=" *",font="lucida 20 bold",padx=13,pady=14,bg="black",fg="lightblue")
b.bind("<Button-1>",click)
b.pack(side=LEFT)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="3",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 20 bold",padx=14,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 20 bold",padx=14.1,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 20 bold",padx=14.5,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="-",font="lucida 20 bold",padx=16.5,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="lucida 20 bold",padx=13,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="lucida 20 bold",padx=9.5,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="00",font="lucida 20 bold",padx=8,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()



f = Frame(root,bg="black")
b=Button(f,text="C",font="lucida 20 bold",padx=10.5,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 20 bold",padx=17,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="0",font="lucida 20 bold",padx=14.5,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="AC",font="lucida 20 bold",padx=3.5,pady=14,bg="black",fg="lightblue")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()
root.mainloop()