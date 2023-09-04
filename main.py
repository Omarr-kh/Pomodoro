import tkinter as tk

# Constants
BG_COLOR = "#176B87"

# window setup
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG_COLOR)

# Canvas
canvas = tk.Canvas(width=200, height=224, bg=BG_COLOR, highlightbackground=BG_COLOR)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas.create_text(108, 130, text="00:00", font=("courier", 30, "bold"), fill="white")
canvas.pack()

window.mainloop()