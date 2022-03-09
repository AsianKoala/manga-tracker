from tkinter import Tk, Label
import tkinter as tk
from PIL import Image, ImageTk

class Notification:
    def start(self):
        root = Tk()
        root.title('nyatification')
        img = ImageTk.PhotoImage(Image.open("nekomimi.jpg"))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        root.mainloop()

noti = Notification()
noti.start()