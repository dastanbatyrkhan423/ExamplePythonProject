from tkinter import *
# all-,barlygi
window= Tk()
window.title("calculator")
window.minsize(400,300)

# dastan_label=Label(text="my name is Dastan",font=("Arial",18, "bold"))
# dastan_label.pack()
# a_label=Label(text="my name is a",font=("Arial",18, "bold"))
# a_label.pack()

# def clicked():
#     a_label.config(text="my names is Arman")
#
#
input=Entry(width=15,background="black",highlightcolor="red")
input.grid(row=95,column=9)
button=Button(text="C",font=("Arial",18, "bold"))
button.grid(row=9,column=5)


def ooo():
    x = input.get()
    a_label.config(text=x)

button=Button(text="press me",command=ooo)
button.pack()

input=Entry(width=15,background="yellow",highlightcolor="red")
input.pack()













window.mainloop()



