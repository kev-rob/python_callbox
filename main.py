import os
from pynput.keyboard import Key, Controller
from guizero import App, PushButton, Picture, Text, Box

def help():
    help_button.hide()
    os.system("python _request.py")
    cancel_button.show()
    help_text1.hide()
    help_text2.hide()
    cancel_text.show()

def cancel():
    help_button.show()
    os.system("python _cancel.py")
    cancel_button.hide()
    cancel_text.hide()
    help_text1.show()
    help_text2.show()

keyboard = Controller()

def exit():
    keyboard.press(Key.alt_l)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.f4)

app = App(title="Help Callbox", bg="white")

left_pad = Box(app, align="left", height="fill", width=5)
right_pad = Box(app, align="right", height="fill", width=5)
top_pad = Box(app, align="top", width="fill", height=5)
bottom_pad = Box(app, align="bottom", width="fill", height=5)
title_box = Box(app, width="fill", align="top")
wordmark = Picture(title_box, image="banner.png", align="left")
help_text1 = Text(app, text="\rDo you need assistance?\r\r", color="#0e67b5", size="18")
cancel_text = Text(app, text="\rHelp is on the way.\r\r If you can no longer wait, please press \"Cancel\".\r\r", visible=False, color="#0e67b5", size="18")
cancel_button = PushButton(app, command=cancel, text="Cancel", visible=False, width=20)
help_button = PushButton(app, image="logo.png", command=help, text="Help")
help_text2 = Text(app, text="\r Press the button and we will be with you ASAP.\r\r", color="#0e67b5", size="18")
bottom_box = Box(app, width="fill", align="bottom")
exit_button = PushButton(bottom_box, command=exit, text="Exit", align="left", width=20)


app.set_full_screen()
app.display()
