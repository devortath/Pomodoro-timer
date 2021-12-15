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
reps = 0
check = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    """Reset de todos los elementos"""
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    label_check.config(text="")
    global reps
    reps = 0
    global check
    check = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    """Inicializador pomodoro"""
    global reps
    reps += 1
    print(reps)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Rep 8 solo
    if reps % 8 == 0:
        countdown(long_break_sec)
        label_timer.config(text="Break", fg=RED)
        # print("Long")
    # Reps 2,4 y 6
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
        # print("Short")
    else:
        # Vuelta 1,3,5 y 7
        countdown(work_sec)
        label_timer.config(text="Work", fg=GREEN)
        # print("Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """Contador de tiempo hasta 0"""
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()

        # Sumar un check cada sesion de trabajo+pausa corta
        if reps % 2 == 0:
            global check
            check = f"{check}✓"
        label_check.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
# Ventana
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold")
)
canvas.grid(column=1, row=1)


# Etiquetas
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label_timer.grid(column=1, row=0)

label_check = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "normal"))
label_check.grid(column=1, row=3)

# Botones
button_start = Button(text="Start", command=start, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset, highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()
