import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *

root=Tk()
''' 
root.title("First GUI using python")
ttk.Button(root, text = "Hello world!").grid()
root.mainloop() 
'''

frame = Frame(root)
labelText = StringVar(
)
label = Label(frame, textvariable = labelText)
button = Button(frame, text="I am a button")

labelText.set("Hey! what's app")

label.pack()
button.pack()
frame.pack()

root.mainloop()

frame = Frame(root)
label(frame, text = "Hey!").pack()
