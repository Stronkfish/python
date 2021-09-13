from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Converter")
window.geometry("300x300")

beans = 0
beans2 = 0

def click1():
    beans = int(num.get())
    lbl = Label(tab1, font = ("Arial Bold", 12), text = (f"K(PH): {beans * 1.6093}"))
    lbl.grid(column = 0, row = 1)

def click2(): 
    beans2 = int(num2.get())
    lbl2 = Label(tab2, font = ("Arial Bold", 12), text = (f"M(PH): {beans2 * 0.6214}"))
    lbl2.grid(column = 0, row = 1)

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text = "To K(PH)")
tab_control.add(tab2, text = "To M(PH)")

num = Entry(tab1, width = 10, font = ("Arial Bold", 12))
btn = Button(tab1, text = "Convert", font = ("Arial Bold", 12), command = click1)
num2 = Entry(tab2, width = 10, font = ("Arial Bold", 12))
btn2 = Button(tab2, text = "Convert", font = ("Arial Bold", 12), command = click2)

num.grid(column = 0, row = 0)
btn.grid(column = 1, row = 0)
num2.grid(column = 0, row = 0)
btn2.grid(column = 1, row = 0)
tab_control.pack(expand = 1, fill = "both")

window.mainloop()
