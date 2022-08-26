from ast import Name
from itertools import count
from tkinter import *
import os

"""
1. Directly on some popup in listbox provide ability to move up and down with keyboard 
    - move up and down with arrow in listbox
    - set focus to field in listbox
    - enable up and down arrow key for listbox
2. Either I try to reimplement the stack over or ask 
    - try to implement the stack overlflow 
    - if above doesnt work create question on stackoverlflow 
"""

root = Tk()
root.title('Searcher')
root.geometry("500x300")
myLabel = Label(root, text="Search",
                font=("Helvetica", 14), fg="grey")
myLabel.pack(pady=20)
myEntry = Entry(root, font=("Helvetica", 20))
myEntry.pack()
myList = Listbox(root, width=50)
myList.pack(pady=40)

# Update the listbox
def update(data):
    # Clear the listbox
    myList.delete(0, END)
    # Add toppings to listbox
    for item in data:
        myList.insert(END, item)
    myList.select_set(0)
    myList.bind("<Down>", OnEntryDown)
    myList.bind("<Up>", OnEntryUp)
    #myList.bind("<Down>", onEntryDown())


# returns list of files/dirs names that match the input string (updates on every key event in search bar)
def displayer(typed):
    lWithFiles = list()

    depth = 2

    # [1] abspath() already acts as normpath() to remove trailing os.sep
    # , and we need ensures trailing os.sep not exists to make slicing accurate.
    # [2] abspath() also make /../ and ////, "." get resolved even though os.walk can returns it literally.
    # [3] expanduser() expands ~
    # [4] expandvars() expands $HOME
    # WARN: Don't use [3] expanduser and [4] expandvars if stuff contains arbitrary string out of your control.
    # stuff = os.path.expanduser(os.path.expandvars(stuff)) # if trusted source
    stuff = os.path.abspath('/Users/maxhager/Projects2022')

    for root, dirs, files in os.walk(stuff):
        if root[len(stuff):].count(os.sep) < depth:
            for dir in dirs:
                if dir.startswith(typed):
                    lWithFiles.append(os.path.join(root, dir))
    return lWithFiles

def input(e):
    typed = myEntry.get()
    lWithPaths = displayer(typed)
    update(lWithPaths)

# Create a binding on the entry box
myEntry.bind("<KeyRelease>", input)

if __name__ == "__main__":
    root.mainloop()
