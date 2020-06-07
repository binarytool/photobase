import os
from tkinter import *
from PIL import Image, ImageTk

photoPath = r'E:\photo\Новая папка (2)\DCIM\Camera'

for folderName, subfolders, filenames in os.walk(photoPath):
    print(' > ' + folderName)

    if subfolders:
        raise ValueError("subfolders")

    for filename in filenames:
        print(' >> ' + filename)



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open(r"E:\photo\!НГ_10 1.1.10\DSC07734.JPG")
        load = load.resize((250, 250), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.pack(side = "bottom", fill = "both", expand = "yes")
        img.image = render
        img.place(x=0, y=0, relheight = 0.5, relwidth = 0.5)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()