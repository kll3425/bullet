#!/usr/bin/env python3
 
#Author: Kora Lovdahl
#Class: CSEC.473
#Due date: 15 February, 2023

import tkinter as tk

bullet = tk.PhotoImage(file='.\bullethole.png')

def create_popup():
    popup = tk.Toplevel()
    popup.protocol("WM_DELETE_WINDOW", lambda: create_popup())
    label=tk.Label(popup, image=bullet)
    label.pack()


root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", lambda: create_popup())

label = tk.Label(root, image=bullet)
label.pack()

root.mainloop()