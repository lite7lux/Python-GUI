# add calculator
from tkinter import *
root = Tk()
root.geometry("300x200")

l1 = Label(root,text=" Enter first number")
l1.grid(row=0,column=0)

e1 = Entry(root,text="first number")
e1.grid(row=1,column=0,padx=10)

l2 = Label(root,text=" Enter second number")
l2.grid(row=2,column=0)

e2 = Entry(root,text="second number ")
e2.grid(row=3,column=0, padx=10)

def fclickme():
    x= getdouble(e1.get())+getdouble(e2.get())
    l2 = Label(root,text = "The addition result = "+str(x))
    l2.grid(row=5,column=0)

b1 = Button(root,text="Click me", command = fclickme)
b1.grid(row=4,column=0)
root.mainloop()





