from tkinter.ttk import *
import tkinter as tk
import random

window = tk.Tk()
window.title("String Generator")
window.geometry("300x75")

frame_a = tk.Frame()
frame_b = tk.Frame()

def clicked():
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[];,./}{|:<>?"
    
    for c in range(15):
        password += random.choice(characters)
    
    pw = tk.Label(master = frame_b, text = (f"       {password}       "), font = ("Arial Bold", 12))
    pw.grid(column = 1, row = 1)
    print(password)

gen = tk.Button(master = frame_a, text = "Generate", font = ("Arial Bold", 12), command = clicked)
gen.grid()

frame_a.pack()
frame_b.pack()

window.mainloop()
