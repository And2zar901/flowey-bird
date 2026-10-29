from customtkinter import *
import subprocess

win = CTk()
set_default_color_theme("green")
win.geometry("720x720")
win.title("Flowey-Bird menu")

def play():
    win.destroy()
    subprocess.Popen(["python", "main.py"])

play_btn = CTkButton(
    win,
    text="Play",
    fg_color="Lime",
    text_color="White",
    hover_color="Green",
    font=("Arial", 35, "bold"),
    width=200,
    height=100,
    command=play
)

play_btn.pack(pady=(120, 0))

def exit_app():
    win.destroy()

exit_btn = CTkButton(
    win,
    text = "Exit",
    command = exit_app,
    width = 200,
    height = 100,
    hover_color = "green",
    text_color = "white",
    fg_color = "lime",
    font = ("Arial", 30, "bold")
)

exit_btn.pack(pady=(120, 0))

win.mainloop()