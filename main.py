from tkinter import *
from tkinter import messagebox
import random
from random import randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_safe_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

def save():
    website = website_entry.get()
    email = email_user_entry.get()
    user_password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": user_password,
        }
    }

    if len(website) == 0 or len(user_password) == 0:
        empty_entry = messagebox.showerror(title="Error", message="Please dont leave any empty fields")
    else:
        try:  # this can fail
            with open("data.json", "r") as file_data:
                # reading old data
                data = json.load(file_data)
        except FileNotFoundError:  # deal with any fail that happen
            with open("data.json", "w") as file_data:
                # Saving updated data
                json.dump(new_data, file_data, indent=4)
        else:  # code that needs to run if there are no issues
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file_data:
                # Saving updated data
                json.dump(data, file_data, indent=4)
        finally:  # doesn't matter if there are issue or no issue, this will run anyway
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            password_dict = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message="No data file found")
    else:
        if website in password_dict:
            email = password_dict[website]["email"]
            password = password_dict[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")


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

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

email_user_entry = Entry(width=43)
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

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
