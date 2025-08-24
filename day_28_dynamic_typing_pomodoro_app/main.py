from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer_reset = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    root.after_cancel(timer_reset)
    canvas.itemconfig(timing, text="00:00")
    timer.config(text='Timer')
    check.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        count_down(work_secs)
        timer.config(text="Work", fg=GREEN)
    elif reps % 4 == 0:
        count_down(long_break_secs)
        timer.config(text="LONG Break", fg=PINK)
    else:
        count_down(short_break_secs)
        timer.config(text="Break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    global timer_reset
    global reps
    canvas.itemconfig(timing, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer_reset = root.after(1000, count_down, count - 1)
    else:
        start_count()
        if reps % 2 == 0:
            check.config(text="✔" * reps)


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"))
timer.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(row= 0, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timing = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row= 1, column=2)

start = Button(text="Start", bg='white', command=start_count)
start.grid(row= 2, column=1)

check = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
check.grid(row= 3, column= 2)

reset = Button(text="Reset", bg="white", command=reset)
reset.grid(row= 2, column=3)


root.mainloop()
