#!/usr/bin/python3
import tkinter

BTN_WIDTH=10
BTN_HEIGHT=3
FONT="Helvetica"
root = tkinter.Tk()
root.title("Counter")
var = tkinter.IntVar()
var.set(0)

def count(value: int):
	global label
	global var
	var.set(var.get()+value)

label = tkinter.Label(root, textvariable=var, font=(("Helvetica", 40)))
button_add = tkinter.Button(root, text="+", height=BTN_HEIGHT, width=BTN_WIDTH, font=((FONT, 40)), command=lambda: count(1))
button_sub = tkinter.Button(root, text="-", height=BTN_HEIGHT, width=BTN_WIDTH, font=((FONT, 40)), command=lambda: count(-1))
button_reset = tkinter.Button(root, text="Reset", font=((FONT, 10)), command=lambda: var.set(0))

label.grid(row=0, column=0, columnspan=2)
button_sub.grid(row=1, column=0)
button_add.grid(row=1, column=1)
button_reset.grid(row=2, column=0, columnspan=2, sticky=tkinter.EW)

root.bind("<Up>", lambda x: count(1))
root.bind("<Down>", lambda x: count(-1))

root.mainloop()
