
# ---------------------------- CONSTANTS ------------------------------- #
import math
from tkinter import Button, Canvas, Label, PhotoImage, Tk
import time


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def reset_timer():
    global timer
    if timer is not None:
        window.after(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text="Timer")
    check_markss.config(text="")
    global reps
    reps = 0

def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text="Break" , fg= RED)
    elif reps %2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break" , fg= PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work" , fg= GREEN)


def count_down(count):
    date_time = time.strftime("%M:%S", time.gmtime(count))
    
    canvas.itemconfig(timer_text, text=date_time)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_markss.config(text=marks)
        



window = Tk()
window.title("Pomodor")
window.config(padx=100, pady=50 , bg = YELLOW )



title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)


canvas = Canvas(width = 400, height =224, bg = YELLOW,highlightbackground= YELLOW)
tomato = PhotoImage(file ="pomodoro/tomato.png")
canvas.create_image(180, 112 , image =tomato)
timer_text = canvas.create_text(180,112,text="00:00" , fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)




star_button = Button(text="Start", highlightthickness=0 , command =start_timer)
star_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0 , command = reset_timer)

reset_button.grid(column=2,row=2)

check_markss = Label(text="✔", fg=GREEN, bg=YELLOW)
check_markss.grid(column=1,row=3)

window.mainloop()