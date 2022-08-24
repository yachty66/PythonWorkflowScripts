from itertools import count
from tkinter import *
import os

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

# returns list of files/dirs names that match the input string (updates on every key event in search bar)



def displayer(typed):  
    lWithFiles = []
    counter = 0
    for path, currentDirectory, files in os.walk("/Users/maxhager/Projects2022"):
        if counter == 2:
                break
        for dir in currentDirectory:
            counter += 1
            print(dir)
            if dir.startswith(typed):
                lWithFiles.append(os.path.join(path, dir))
            if counter == 2:
                break
    print(str(counter)+"----------------------------------------------------------------------------------------------------------------")
    return lWithFiles

# gets input from search field


def input(e):
    typed = myEntry.get()
    lWithPaths = displayer(typed)
    print(lWithPaths)
    update(lWithPaths)

# Create a binding on the entry box
myEntry.bind("<KeyRelease>", input)

if __name__ == "__main__":
    root.mainloop()
