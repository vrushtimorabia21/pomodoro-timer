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
REPS = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(count_down)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    my_check.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    count_down(work_sec)
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0: 
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        
        # count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    if count_sec < 10: #dynamic type conversion from int to
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        my_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
my_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
my_check.grid(column=1, row=3)


canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img )
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



btm_start = Button(text="Start", highlightthickness=0, command=start_timer)
btm_start.grid(column=0, row=2)

btm_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
btm_reset.grid(column=2, row=2)


window.mainloop()