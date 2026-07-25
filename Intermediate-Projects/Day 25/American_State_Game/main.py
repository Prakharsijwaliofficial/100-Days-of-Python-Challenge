import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "American_State_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load CSV data
data = pd.read_csv("American_State_game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Writer turtle setup (keep one instance off-screen to draw labels)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

while len(guessed_states) < 50:
    answer_st = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    # Handle user canceling the prompt or closing the window
    if answer_st is None:
        break

    # Normalize user input to Title Case (e.g., "new york" -> "New York")
    answer_st = answer_st.title().strip()

    # Exit mechanism for studying missed states
    if answer_st == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("American_State_game/states_to_learn.csv")
        break

    # Check if guess is valid and hasn't been guessed already
    if answer_st in all_states and answer_st not in guessed_states:
        guessed_states.append(answer_st)
        
        # Extract x, y coordinates using Pandas
        state_data = data[data.state == answer_st]
        x_pos = int(state_data.x.item())
        y_pos = int(state_data.y.item())

        # Write state name on the map
        writer.goto(x_pos, y_pos)
        writer.write(answer_st, align="center", font=("Arial", 8, "normal"))
