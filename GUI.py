from cProfile import label
from faulthandler import disable
import tkinter as tk

root = tk.Tk()

def my_click():
    my_label = tk.Label(root, text="I'm clicked")
    my_label.pack()

button_1 = tk.Button(root, text="Click me", state= "normal", padx=50, pady=50, command=my_click, fg="Red", bg="Black")

button_1.pack()






'''
#Creating a label widget
my_label1 = tk.Label(root, text="Hello World")
my_label2 = tk.Label(root, text="Jag heter Linus")

#Gridsystem
my_label1.grid(row= 0, column=0)
my_label2.grid(row=1, column=1) #Column is relative. 

#Showing on screen
my_label1.pack()
my_label2.pack()
'''


root.mainloop()