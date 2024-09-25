import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        print(len(website))
        messagebox.showwarning(title="Fields Empty", message="Please complete all necessary fields.")

    else:
        data_save = messagebox.askokcancel(title=website, message=f"Username: {username}\nPassword: {password}\n "
                                                                  f"\nIs this okay to save?")

        if data_save:
            f = open("password_data.txt", "a")
            f.write(f"Site: {website} | Username: {username} | Password: {password}\n")
            f.close()

            website_entry.delete(0, "end")
            user_entry.delete(0, "end")
            pass_entry.delete(0, "end")

            messagebox.showinfo(title="Password Saved", message="User credentials successfully saved.")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg="#D3D3D3")

# -- LOGO IMAGE -- #
canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg="#D3D3D3")
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# -- LABELS -- #
website_label = tk.Label(text="Website:", bg="#D3D3D3")
website_label.grid(row=1, column=0)
website_label.config(pady=2)

user_label = tk.Label(text="Username:", bg="#D3D3D3")
user_label.grid(row=2, column=0)
user_label.config(pady=2)

pass_label = tk.Label(text="Password:", bg="#D3D3D3")
pass_label.grid(row=3, column=0)
pass_label.config(pady=2)

# -- ENTRIES -- #
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

user_entry = tk.Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

pass_entry = tk.Entry(width=24)
pass_entry.grid(row=3, column=1, sticky="w")

# -- BUTTONS -- #
gen_pass_button = tk.Button(text="Generate Password", width=14, command=generate_password)
gen_pass_button.grid(row=3, column=2, sticky="e")

add_button = tk.Button(text="Add User Credentials", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

# -- MAIN LOOP -- #
window.mainloop()



