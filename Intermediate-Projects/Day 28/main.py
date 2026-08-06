from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 2
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text= "Timer", fg= GREEN)
    tick_label.config(text= "")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_Sec = LONG_BREAK_MIN * 60
    
    if reps % 2 == 0 and reps % 8 != 0 :
        timer_time = short_break_sec
        label_timer.config(text = "Break", fg= PINK)

    elif reps % 8 == 0:
        timer_time = long_break_Sec
        label_timer.config(text="Long Break", fg = GREEN)

    elif reps % 2 != 0:
        timer_time = work_min_sec
        label_timer.config(text = "Work", fg = RED )
    count_down(timer_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
       timer =  window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW, highlightthickness=0)

canvas = Canvas(width= 200, height= 224, bg=YELLOW)
tomato_ing = PhotoImage(file= "tomato.png")
canvas.create_image(102, 112, image=tomato_ing)
timer_text = canvas.create_text(102,130, text= "00:00", fill= "white" ,  font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)


#Timer Label
label_timer = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg= YELLOW )
label_timer.grid(column=1, row=0)
#Tick Label
tick_label = Label(fg=GREEN, bg=YELLOW , font=("",15,))
tick_label.grid(column=1,row=3)

#Start Button
start_button = Button(text="Start", command=start_timer )
start_button.grid(column=0, row=2)
#Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
