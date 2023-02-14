#!/usr/bin/env python3
 
#Author: Kora Lovdahl
#Class: CSEC.473
#Due date: 15 February, 2023

#Changes keyboard layout to random keymap for linux
import subprocess
import time
import random
import string

#Generate an Xkeymap file that maps all the letters on a standard keyboard
def generate_keymap_file():
    keycodes = [24,25,26,27,28,29,30,31,32,33,38,39,40,41,42,43,44,45,46,52,53,54,55,56,57,58]
    letters = list(string.ascii_lowercase)

    random.shuffle(keycodes)

    with open('letters.xkm', 'w') as f:
        for i in range(0,27):
            f.write('keycode ' + keycodes[i] + ' {[' + letters[i] + ']};\n')

while(True):
    generate_keymap_file()

    subprocess.run(['setxkbmap', '-layout', 'letters.xkm'])

    time.sleep(random.randint(60, 600))