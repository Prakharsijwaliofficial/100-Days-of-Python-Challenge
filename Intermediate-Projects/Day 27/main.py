from tkinter import *

# ---------------------------- WINDOW ------------------------------- #

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# ---------------------------- FUNCTIONS ---------------------------- #

def miles_to_kilometer():
    try:
        miles = float(miles_entry.get())
        kilometers = round(miles * 1.60934, 2)
        kilometer_result_label.config(text=kilometers)
    except ValueError:
        kilometer_result_label.config(text="Invalid")

# ---------------------------- ENTRY ------------------------------- #

miles_entry = Entry(width=10)
miles_entry.insert(END, "0")
miles_entry.grid(column=1, row=0)

# ---------------------------- LABELS ------------------------------ #

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# ---------------------------- BUTTON ------------------------------ #

calculate_button = Button(
    text="Calculate",
    command=miles_to_kilometer
)
calculate_button.grid(column=1, row=2)

# ---------------------------- MAIN LOOP --------------------------- #

window.mainloop()
