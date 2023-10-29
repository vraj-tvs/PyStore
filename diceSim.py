import random
from tkinter import *

root = Tk()
root.title("Dice Simulator")
root.geometry("700x450")

l1 = Label(root, font=("times new roman", 200))


def roll():

    num = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(num)}{random.choice(num)}')
    l1.pack()


b1 = Button(root, text="Let's Roll...", width=7, command=roll)
b1.place(x=310, y=10)

root.mainloop()
