from tkinter import *
from tkinter import messagebox
import random
from random import randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_safe_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for char in range(randint(8, 10))]
    password_list += [random.choice(symbols) for character in range(randint(2, 4))]
    password_list += [random.choice(numbers) for item in range(randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# def safe_password():
#
#     password = generate_safe_password()
#     password_entry.config(password)


def save():
    website = website_entry.get()
    email = email_user_entry.get()
    user_password = password_entry.get()

    if len(website) == 0 or len(user_password) == 0:
        empty_entry = messagebox.showerror(title="Error", message="Please dont leave any empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                          f"\nPassword: {user_password} \n Is ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file_content = file.writelines(f"{website} | {email} | {user_password} \n")

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_name = Label(text="Website: ")
website_name.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

email_user_entry = Entry(width=50)
email_user_entry.insert(0, "suelen@matos.com")
email_user_entry.grid(column=1, row=2, columnspan=2)

password_user = Label(text="Password:")
password_user.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", width=15, command=generate_safe_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=50, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
