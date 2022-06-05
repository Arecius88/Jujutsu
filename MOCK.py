import random
from Modules import uke_wasa, atemi_wasa, kansetsu_wasa, nage_wasa, kihon

start = False
uke = uke_wasa()


def stop_condition():
    if x == 0:
        start =True



def kihon_group(technic_group):
    technic = random.choice(technic_group)
    print(f"\n Tekniken är {technic} \n")
    #print(len(technic_group))
    technic_group.remove(technic)
    #print(len(technic_group))

    return technic_group


def new_exercise(answer):
    answer = input("New technic? (y/n) ")



    

while start != True:
    val = input("> ")

    if val == "u":
        test1 = kihon_group(uke)
        print(len(test1))


        if len(test1) == 0:
            start = True   


'''
        
        new_exercice =input("New technic? (y/n) ")


        while new_exercice == "y":
            print(random.choice(uke_wasa()))
            new_exercice = input("New technic? (y/n) ")

            if new_exercice == "n":
                break
'''

#Tinker test app
'''
from cProfile import label
from faulthandler import disable
from optparse import Option
import tkinter as tk

from setuptools import Command

root = tk.Tk()

def my_click():
    my_label = tk.Label(root, text="I'm clicked")
    my_label.pack()

button_1 = tk.Button(root, text="Click me", state= "normal", padx=50, pady=50, command=my_click, fg="Red", bg="Black")

button_1.pack()

#Drop Down Boxes
def show ():
    mylabel = tk.Label(root, text= clicked.get()).pack()


options = ["Atemi", "Uke",]

clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(root, clicked, *options)
drop.pack()


my_button = tk.Button(root, text= "Välj teknik", command=show).pack()


#Creating a label widget
my_label1 = tk.Label(root, text="Hello World")
my_label2 = tk.Label(root, text="Jag heter Linus")

#Gridsystem
my_label1.grid(row= 0, column=0)
my_label2.grid(row=1, column=1) #Column is relative. 

#Showing on screen
my_label1.pack()
my_label2.pack()

root.mainloop()

'''