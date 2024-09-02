from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    
    #Copy generated password to clipboard
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    # Fetch the entries data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
    #Messagebox
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    
        if is_okay:
        #Creates & writes to data.txt file the entries data and deletes after add button pressed
            with open("Projects\project27\data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#Create a window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Create a canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"Projects\project27\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=0)

#Create labels
website_label = Label(text="Website:")
website_label.grid(column=1, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=2)
password_label = Label(text="Password:")
password_label.grid(column=1, row=3)

#Create Entries
website_entry = Entry()
website_entry.grid(column=2, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry()
email_entry.grid(column=2, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "dummyemail@email.com")
password_entry = Entry()
password_entry.grid(column=2, row=3, sticky="EW")

#Create buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=3, row=3, sticky="EW")
add_button = Button(text="Add", command=save)
add_button.grid(column=2, row=4, columnspan=2, sticky="EW")


window.mainloop()