import tkinter as tk

# window setup
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

# Canvas
canvas = tk.Canvas(width=200, height=224)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas.pack()

window.mainloop()