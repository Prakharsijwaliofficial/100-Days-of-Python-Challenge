from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass(website,gmail, password):
    if len(website) == 0 or  len(password) == 0:
         messagebox.showerror(title="Oops" ,  message="Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title="website", message=f"Ther are the details entered: \nEmail: {gmail}\nPassword: {password} \nIt is ok to save")

        if is_ok:
            with open("Password_file.txt", mode= "a") as file:
                file.write(f"{website} | {gmail} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0,END)
    


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1)
logo = PhotoImage(file="logo.png")
canvas.create_image(
    100,
    100,
    image=logo
)

#Labels
website_label = Label(text="Website:", font= ("",10,"bold"))
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", font= ("",10,"bold"))
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font= ("",10,"bold"))
password_label.grid(column=0,row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
website = website_entry.get()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2,columnspan=2)
email_username_entry.insert(0, "Prakharsijwaliofficial@gmail.com")
gmail = email_username_entry.get()

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)
password = password_entry.get()

#Buttons
generate_pass_button = Button(text="Generate Password", command= generate_pass)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width= 36, command=lambda: save_pass(website_entry.get(),email_username_entry.get(), password_entry.get()))
add_button.grid(column=1,row=4, columnspan=2)

window.mainloop()
