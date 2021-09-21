from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import random

window = Tk()
window.iconbitmap('C:\\Users\\adriel.yetman.00\\Downloads\\epicon.ico')
window.title("Rock Paper Scissors")
window.geometry("500x100")
selected = IntVar()
frame_a = tk.Frame()
frame_b = tk.Frame()

rockselect = tk.Radiobutton(master = frame_a, text = "Rock", value = 1, variable = selected, font = ("Arial Bold", 12))
paperselect = tk.Radiobutton(master = frame_a, text = "Paper", value = 2, variable = selected, font = ("Arial Bold", 12))
scissorselect = tk.Radiobutton(master = frame_a, text = "Scissors", value = 3, variable = selected, font = ("Arial Bold", 12))
    
def clicked():
    user = int(selected.get())
    rps = [1, 2, 3]
    computer = random.choice(rps)
    if computer == 1:
        compselected = "Rock"
    if computer == 2:
        compselected = "Paper"
    if computer == 3:
        compselected = "Scissors"
    if user == computer:
        result = tk.Label(master = frame_b, text = (f"       You Both Selected {compselected}, You Tied!       "), font = ("Arial", 12))
        result.grid(column = 0, row = 2)
        print(f"user: {compselected}\npc: {compselected}\nwinner: null\n")
    if user == 1:
        if computer == 2:
            result = tk.Label(master = frame_b, text = "       Paper Covers Rock, You Lost.       ", font = ("Arial", 12))
            result.grid(column = 0, row = 2)
            print("user: rock\npc: paper\nwinner: pc\n")
        if computer == 3:
            result = tk.Label(master = frame_b, text = "       Rock Smashes Scissors, You Won!       ", font = ("Arial", 12))
            result.grid(column = 0, row = 2)
            print("user: rock\npc: scissors\nwinner: user\n")
    if user == 2:
        if computer == 1:
            result = tk.Label(master = frame_b, text = "       Paper Covers Rock, You Won!       ", font = ("Arial", 12))
            result.grid(column = 0, row = 2)
            print("user: paper\npc: rock\nwinner: user\n")
        if computer == 3:
            result = tk.Label(master = frame_b, text = "       Scissors Cuts Paper, You Lost.       ", font = ("Arial", 12))
            result.grid(column = 0, row = 2)
            print("user: paper\npc: scissors\nwinner: pc\n")
    if user == 3:
        if computer == 1:
            result = tk.Label(master = frame_b, text = "       Rock Smashes Scissors, You Lost.       ", font = ("Arial", 12))
            result.grid(column = 0, row = 2)
            print("user: scissors\npc: rock\nwinner: pc\n")
        if computer == 2:
            result = tk.Label(master = frame_b, text = "       Scissors Cuts Paper, You Won!       ", font = ("Arial", 12))
            result.grid(column = 0, row = 2)
            print("user: scissors\npc: paper\nwinner: user\n")

btn = tk.Button(master = frame_a, text = "Select", font = ("Arial Bold", 12), command = clicked)

rockselect.grid(column = 0, row = 1)
paperselect.grid(column = 1, row = 1)
scissorselect.grid(column = 2, row = 1)
btn.grid(column = 3, row = 1)
frame_a.pack()
frame_b.pack()

window.mainloop()
