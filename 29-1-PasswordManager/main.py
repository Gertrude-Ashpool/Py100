from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # get inputs
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please complete all fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                        f"\nPassword: {password}\n Press ok to save.")
        if is_ok:
            # append to data.txt
            new_entry = f"{website} | {email} | {password}\n"
            with open("data.txt", mode="a") as data_file:
                data_file.write(new_entry)
            # clear entry fields
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
website_label = Label(text="Website:", font=('Arial', 14, "normal"))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=('Arial', 14, "normal"))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=('Arial', 14, "normal"))
password_label.grid(column=0, row=3)

# Entry fields
website_input = Entry(width=38)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = Entry(width=38)
email_input.insert(0, "name@mail.com")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=22)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password, width=12)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save, width=35)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
