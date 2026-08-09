from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- DATA ------------------------------- #

# Try to load the saved learning list.
# If it doesn't exist, load the original French words.
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

# Convert the DataFrame into a list of dictionaries.
to_learn = data.to_dict(orient="records")

# Check if all words have been learned.
if len(to_learn) == 0:
    print("You learned all the words!")


# ---------------------------- RANDOM WORD ------------------------------- #

def random_french_word():
    global current_card

    # Choose a random card from the learning list.
    current_card = random.choice(to_learn)

    # Show the front of the card.
    canvas.itemconfig(
        background_image,
        image=card_image_front
    )

    # Show the French word.
    canvas.itemconfig(
        title_text,
        text="French",
        fill="black"
    )

    canvas.itemconfig(
        word_text,
        text=current_card["French"],
        fill="black"
    )

    # Flip the card after 3 seconds.
    window.after(3000, flip_card)


# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    # Change the card background to the back.
    canvas.itemconfig(
        background_image,
        image=card_image_back
    )

    # Show the English translation.
    canvas.itemconfig(
        title_text,
        text="English",
        fill="white"
    )

    canvas.itemconfig(
        word_text,
        text=current_card["English"],
        fill="white"
    )


# ---------------------------- REMOVE CARD ------------------------------- #

def remove_card():
    # Remove the current card because the user knows it.
    to_learn.remove(current_card)

    # Save the remaining cards to a new CSV file.
    pd.DataFrame(to_learn).to_csv(
        "data/words_to_learn.csv",
        index=False
    )

    # Show the next card.
    random_french_word()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOR
)


# ---------------------------- CANVAS ------------------------------- #

canvas = Canvas(
    height=526,
    width=800,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)

canvas.grid(
    row=0,
    column=0,
    columnspan=2
)


# ---------------------------- IMAGES ------------------------------- #

card_image_front = PhotoImage(
    file="images/card_front.png"
)

card_image_back = PhotoImage(
    file="images/card_back.png"
)

wrong_image = PhotoImage(
    file="images/wrong.png"
)

right_image = PhotoImage(
    file="images/right.png"
)


# ---------------------------- CARD IMAGE ------------------------------- #

background_image = canvas.create_image(
    400,
    263,
    image=card_image_front
)


# ---------------------------- BUTTONS ------------------------------- #

button_wrong = Button(
    image=wrong_image,
    highlightthickness=0,
    command=random_french_word
)

button_wrong.grid(
    row=1,
    column=0
)


button_right = Button(
    image=right_image,
    highlightthickness=0,
    command=remove_card
)

button_right.grid(
    row=1,
    column=1
)


# ---------------------------- CANVAS TEXT ------------------------------- #

title_text = canvas.create_text(
    400,
    150,
    text="Title",
    font=("Arial", 40, "italic")
)

word_text = canvas.create_text(
    400,
    263,
    text="Word",
    font=("Arial", 60, "bold")
)


# ---------------------------- START PROGRAM ------------------------------- #

random_french_word()

window.mainloop()

