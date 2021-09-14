from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Caesar Cipher")
window.geometry("300x300")

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def click1():
    cipheredtext = ""
    plaintext = num.get()
    key = int(keyenter.get())
    for c in plaintext.upper():
        if c.isalpha():
            cipheredtext += I2L[ (L2I[c] + key)%26 ]
        else:
            cipheredtext += c
    lbl = Label(tab1, font = ("Arial Bold", 12), text = (f"Result: {cipheredtext}"))
    lbl.grid(column = 0, row = 2)

def click2(): 
    cipheredtext = ""
    plaintext = num2.get()
    key = int(keyenter.get())
    for c in plaintext.upper():
        if c.isalpha():
            cipheredtext += I2L[ (L2I[c] - key)%26 ]
        else:
            cipheredtext += c
    lbl2 = Label(tab2, font = ("Arial Bold", 12), text = (f"Result: {cipheredtext}"))
    lbl2.grid(column = 0, row = 2)

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Encipher")
tab_control.add(tab2, text = "Decipher")

keyenter = Entry(tab1, width = 2, font = ("Arial Bold", 12))
keyenter2 = Entry(tab2, width = 2, font = ("Arial Bold", 12))
keylabel = Label(tab1, text = "Key: ", font = ("Arial Bold", 12))
keylabel2 = Label(tab2, text = "Key: ", font = ("Arial Bold", 12))

num = Entry(tab1, width = 10, font = ("Arial Bold", 12))
btn = Button(tab1, text = "Run", font = ("Arial Bold", 12), command = click1)
num2 = Entry(tab2, width = 10, font = ("Arial Bold", 12))
btn2 = Button(tab2, text = "Run", font = ("Arial Bold", 12), command = click2)

keylabel.grid(column = 0, row = 0)
keylabel2.grid(column = 0, row = 0)
keyenter.grid(column = 1, row = 0)
keyenter2.grid(column = 1, row = 0)
num.grid(column = 0, row = 1)
btn.grid(column = 1, row = 1)
num2.grid(column = 0, row = 1)
btn2.grid(column = 1, row = 1)
tab_control.pack(expand = 1, fill = "both")

window.mainloop()
