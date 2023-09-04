import tkinter as tk
import math

# Constants
BG_COLOR = "#176B87"
STUDY_DURATION = 25
BREAK_DURATION = 5
LONG_BREAK_DURATION = 15
cycles_count = 0
window_timer = None


# Reset function
def reset():
    global cycles_count
    cycles_count = 0

    window.after_cancel(window_timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer", font=("courier", 45, "bold"),
                       fg="#FFC436", bg=BG_COLOR)
    marks_label.config(text="")


# timer function
def timer():
    global cycles_count
    cycles_count += 1

    study_seconds = STUDY_DURATION * 60
    break_seconds = BREAK_DURATION * 60
    long_break_seconds = LONG_BREAK_DURATION * 60

    if cycles_count % 8 == 0:
        timer_label.config(text="BREAK", fg="pink")
        count_down(long_break_seconds)
        cycles_count = 0
    elif cycles_count % 2 == 0:
        timer_label.config(text="BREAK", fg="pink")
        count_down(break_seconds)
    else:
        timer_label.config(text="STUDY", fg="darkgrey")
        count_down(study_seconds)


# count down function
def count_down(time):
    minutes = math.floor(time / 60)
    seconds = time % 60
    canvas.itemconfig(time_text, text=f"{minutes:02d}:{seconds:02d}")

    if time > 0:
        global window_timer
        window_timer = window.after(1000, count_down, time - 1)

    else:
        timer()
        num_of_checks = math.floor(cycles_count / 2)
        marks_label.config(text=f"✔"*num_of_checks)


# window setup
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=BG_COLOR)

window_width = 450
window_height = 500

# Set the desired x and y positions
x_position = 500
y_position = 150

# Use the geometry method to set the window's position and size
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


# Canvas
canvas = tk.Canvas(width=200, height=224, bg=BG_COLOR,
                   highlightbackground=BG_COLOR)

tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)

time_text = canvas.create_text(108, 130, text="00:00", font=(
    "courier", 30, "bold"), fill="white")

canvas.grid(column=1, row=1)


# Labels
timer_label = tk.Label(text="Timer", font=("courier", 45, "bold"),
                       fg="#FFC436", bg=BG_COLOR)
timer_label.grid(column=1, row=0)

marks_label = tk.Label(fg="#1A5D1A", bg=BG_COLOR,
                       font=("courier", 30))
marks_label.grid(column=1, row=3)


# Buttons
start_button = tk.Button(text="Start", command=timer, font=(
    "arial", 12, "bold"), padx=8, pady=3, borderwidth=3, highlightthickness=2, relief="flat", bg="#8C3333", fg="white")
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset, font=(
    "arial", 12, "bold"), padx=8, pady=3, borderwidth=3, highlightthickness=2, relief="flat", bg="#8C3333", fg="white")
reset_button.grid(column=2, row=2)

window.mainloop()
