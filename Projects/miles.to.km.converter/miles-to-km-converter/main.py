from tkinter import *

# Button function to convert miles to km
def convert_unit():
    mile_unit = float(input.get())
    convert_result = mile_unit * 1.609344
    km_value.config(text=f"{round(convert_result)}")

# GUI window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry widget
input = Entry(width=7)
input.grid(column=1,row=0)

#Miles label widget
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

#Equal to label widget
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

#Km value label widget
km_value = Label(text="0")
km_value.grid(column=1, row=1)

#Km unit label widget
km_unit = Label(text="Km")
km_unit.grid(column=2, row=1)

#Calculate button
button = Button(text="Calculate", command=convert_unit)
button.grid(column=1, row=2)

window.mainloop()