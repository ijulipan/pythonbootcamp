## TKinter workshop

from tkinter import *

def button_clicked():
    # print("I got clicked")
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady= 20)

# Label
# Packer Documentation: https://docs.python.org/3/library/tkinter.html#the-packer, https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)
# my_label["text"] = "New text"
# my_label.config(text="New text")

# Button
button1 = Button(text="Click me", command=button_clicked)
button1.grid(column=2, row=2)

button2 = Button(text="Click me too", command=button_clicked)
button2.grid(column=3, row=1)

# Entry
# Entry Documentation: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
input = Entry(width=10)
input.grid(column=4, row=3)
# input.get()


window.mainloop()