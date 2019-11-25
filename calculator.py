from tkinter import *
def calculate(a):
    try:
        z=eval(a)
        input.set(z)
    except:
        input.set("Error!!!")

root=Tk()
root.title("Calculator")
root.geometry("250x150")
root.resizable(0,0)
input=StringVar()
Entry(root,background="red",fg="black",font="TkFixedFont",textvariable=input).grid(row=0,column=0,columnspan=4)
Button(root,text="1",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"1"),height=1,width=4,bg="pink").grid(row=1,column=0)
Button(root,text="2",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"2"),height=1,width=4,bg="green").grid(row=1,column=1)
Button(root,text="3",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"3"),height=1,width=4,bg="yellow").grid(row=1,column=2)
Button(root,text="/",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"/"),height=1,width=4,bg="white").grid(row=1,column=3)
Button(root,text="4",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"4"),height=1,width=4,bg="white").grid(row=2,column=0)
Button(root,text="5",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"5"),height=1,width=4,bg="yellow").grid(row=2,column=1)
Button(root,text="6",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"6"),height=1,width=4,bg="green").grid(row=2,column=2)
Button(root,text="*",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"*"),height=1,width=4,bg="pink").grid(row=2,column=3)
Button(root,text="7",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"7"),height=1,width=4,bg="green").grid(row=3,column=0)
Button(root,text="8",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"8"),height=1,width=4,bg="pink").grid(row=3,column=1)
Button(root,text="9",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"9"),height=1,width=4,bg="white").grid(row=3,column=2)
Button(root,text="+",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"+"),height=1,width=4,bg="yellow").grid(row=3,column=3)
Button(root,text="c",fg="black",font="TkFixedFont",command=lambda:input.set(""),height=1,width=4,bg="yellow").grid(row=4,column=0)
Button(root,text="0",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"0"),height=1,width=4,bg="white").grid(row=4,column=1)
Button(root,text="-",fg="black",font="TkFixedFont",command=lambda:input.set(input.get()+"-"),height=1,width=4,bg="pink").grid(row=4,column=2)
Button(root,text="=",fg="black",font="TkFixedFont",command=lambda:calculate(input.get()),height=1,width=4,bg="green").grid(row=4,column=3)

root.mainloop()

