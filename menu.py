from customtkinter import *
import subprocess
import json

win = CTk()
set_default_color_theme("green")
win.geometry("720x720")
win.title("Flowey-Bird menu")

def open_file(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data

data_from_file = open_file("settings.json")
print(data_from_file)

def play():
    win.destroy()
    subprocess.Popen(["python", "main.py"])

play_btn = CTkButton(
    win,
    text="Play",
    fg_color="Yellow",
    text_color="Black",
    hover_color="Orange",
    font=("Arial", 35, "bold"),
    width=200,
    height=100,
    command=play
)

play_btn.pack(pady=(120, 0))




def settings():
    settings_screen = CTkToplevel(win)
    settings_screen.geometry("400x400")
    settings_screen.title("SETTINGS")
    mode_label = CTkLabel(settings_screen, 
                            text="Settings", 
                            font=("Arial", 35, "bold"),
                            width=100,
                            height=50,)
    mode_label.pack(pady=50)

    def change_voice_mode():
        data_from_file["voice_mode"] = not data_from_file["voice_mode"]

        with open("settings.json", "w") as f:
            json.dump(data_from_file, f, indent=4)

        if data_from_file["voice_mode"]:
            mode_button.configure(text = "Voice mode on")
        else:
            mode_button.configure(text = "Voice mode off")

    if data_from_file["voice_mode"]:
       button_text = "Voice mode on"
    else:
       button_text = "Voice mode off"
 
    mode_button = CTkButton(settings_screen,
            text=button_text,
            fg_color="Yellow",
            text_color="Black",
            hover_color="Orange",
            font=("Arial", 35, "bold"),
            width=100,
            height=50,
            command=change_voice_mode
            )

    mode_button.pack(pady=20)

    music_button = CTkButton(settings_screen,
                text=button_text,
                fg_color="Yellow",
                text_color="Black",
                hover_color="Orange",
                font=("Arial", 35, "bold"),
                width=100,
                height=50,
                command=change_voice_mode
                )
    
    music_button.pack(pady=20)


sett_btn = CTkButton(
    win,
    text="Settings",
    fg_color="Yellow",
    text_color="Black",
    hover_color="Orange",
    font=("Arial", 35, "bold"),
    width=200,
    height=100,
    command=settings
)

sett_btn.pack(pady=(120, 0))

def exit_app():
    win.destroy()

exit_btn = CTkButton(
    win,
    text = "Exit",
    command = exit_app,
    width = 200,
    height = 100,
    hover_color = "Orange",
    text_color = "Black",
    fg_color = "Yellow",
    font = ("Arial", 30, "bold")
)

exit_btn.pack(pady=(120, 0))

win.mainloop()