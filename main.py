# install packages
import random
import time 
from time import sleep 
import tkinter #GUI

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
grey = (123,123,123)

houses = ["Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw"]

# function 
def allocateHouse():
  label.configure(text=(random.choice(houses)))

# configure the tkinter Graphical User Interface (GUI).
root = tkinter.Tk()

# Set the tkinter window title.
root.title("Sorting Hat")

# Set the tkinter window size.
root.geometry("600x100")

# Set the font style and size for tkinter.

label = tkinter.Label(root, text="", font=("Helvetica", 32))

label.pack()

# Create a button with label 
insultButton = tkinter.Button(text="See results", command=allocateHouse)
insultButton.pack()

root.mainloop()