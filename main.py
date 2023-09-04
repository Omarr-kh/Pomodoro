import tkinter as tk

# Constants

BG_COLOR = "#176B87"

# window setup

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG_COLOR)

# Canvas

canvas = tk.Canvas(width=200, height=224, bg=BG_COLOR,
                   highlightbackground=BG_COLOR)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas.create_text(108, 130, text="00:00", font=(
    "courier", 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Labels

tk.Label(text="Timer", font=("courier", 45, "bold"),
         fg="#FFC436", bg=BG_COLOR).grid(column=1, row=0)
tk.Label(text="✔", fg="#1A5D1A", bg=BG_COLOR, font=("courier", 30)).grid(column=1, row=3)

# Buttons

start_button = tk.Button(text="Start", font=(
    "arial", 10), highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(
    "arial", 10), highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
