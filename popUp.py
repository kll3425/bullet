#Author: Kora Lovdahl
#Class: CSEC.473
#Due date: 15 February, 2023

import tkinter as tk
import random as r
import playsound as p
import time

root = tk.Tk()

#Bullet hole image item
bullet = tk.PhotoImage(file='./bullethole.png')

#Pop up creation function
def create_popup():
    for i in range(r.randint(2,6)):
        #Random placement on screen
        x = r.randint(0, root.winfo_screenwidth() - bullet.width())
        y = r.randint(0, root.winfo_screenheight() - bullet.height())
        popup = tk.Toplevel()
        popup.geometry(f"+{x}+{y}")

        #Creates more popups when user tries to close the window
        popup.protocol("WM_DELETE_WINDOW", lambda: create_popup())
        #Keeps the window on top
        popup.attributes("-topmost", True)
        #Creates more windows when clicked on
        popup.bind("<Button-1>", lambda event: create_popup())
        #Removes window manager toolbar
        popup.overrideredirect(1)

        #Creates label
        label=tk.Label(popup, image=bullet, bg='white')
        #Makes background transparent
        popup.wm_attributes('-transparentcolor', 'white')
        label.pack()
    sound()

def sound():
    p.playsound(sound='./pew-pew.mp3')

#Parent bullethole

#Starts in the center of the screen
x = (root.winfo_screenwidth() - bullet.width())//2
y = (root.winfo_screenheight() - bullet.height())//2
root.geometry(f"+{x}+{y}")

#Creates more popups when user tries to close window
root.protocol("WM_DELETE_WINDOW", lambda: create_popup())
#Keeps window on top
root.attributes("-topmost", True)
#Creates more popups when clicked on
root.bind("<Button-1>", lambda event: create_popup())
#Removes window manager toolbar
root.overrideredirect(1)

p.playsound(sound='./pew-pew.mp3')

#Formats the display
label = tk.Label(root, image=bullet, bg='white')
root.wm_attributes('-transparentcolor', 'white')
label.pack()

root.mainloop()