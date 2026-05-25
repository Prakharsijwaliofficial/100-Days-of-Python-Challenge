import colorgram
import turtle as t
import random

# --- 1. SETUP COLOR EXTRACTION ---
# Using your absolute file path directly to avoid any os/path issues
image_path = "C:/Engineering/04_Computer-Science/02_Coding-Learning/Intermediate-From-Day15-to-Day57-Python/Day_18-Turtle-Graphics/image.jpg"

# Extract 30 colors from the image
colours = colorgram.extract(image_path, 30)
rgb_colors = []

# Convert extracted colors into clean RGB tuples
for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    # Filter out extremely bright white/cream background colors
    if r < 240 and g < 240 and b < 240:
        rgb_colors.append((r, g, b))


# --- 2. SETUP TURTLE GRAPHICS ---
t.colormode(255)  # Enables standard RGB color values
painter = t.Turtle()
painter.speed("fastest")
painter.penup()       # Prevent drawing lines between dots
painter.hideturtle()  # Hide the turtle arrow icon

# Starting position (bottom-left corner of the grid)
start_x = -250
start_y = -250
painter.setposition(start_x, start_y)


# --- 3. DRAW THE 10x10 GRID ---
dot_count = 100
dots_per_row = 10
dot_size = 20
spacing = 50

for dot in range(1, dot_count + 1):
    # Draw a dot with a random color from your list
    painter.dot(dot_size, random.choice(rgb_colors))
    painter.forward(spacing)
    
    # Check if a row is completed
    if dot % dots_per_row == 0:
        # Calculate the Y position for the next row
        current_row = dot // dots_per_row
        next_y = start_y + (current_row * spacing)
        
        # Reset position back to the start of the next row
        painter.setposition(start_x, next_y)


# --- 4. KEEP WINDOW OPEN ---
screen = t.Screen()
screen.exitonclick()
