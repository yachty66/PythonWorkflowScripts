'''
2. GUI like https://codepen.io/adrianlambertz/pen/bNQjvp
    1. Pops up on shortcut
    2. Suggests when typing (on top name of file/dir and below the path)
    2. Forwards input to search function    
        1. On click of displayed file/dir or hit enter on choosen file/dir send name to first function
    4. up and down keys is doing results hackergreen
    4. opens up search field on fixed position on the screen and opens up till 50% of the screen height

3. Displayer
    1. Gets as input string from gui text field 
    2. Search every file in the directory and subdirectories with the input string 
    2. returns list of files/dirs names that match the input string (updates on every key event in search bar) 
    3. Forwards the list of files/dirs names to the gui
    
3. Executer 
    1. Gets as input the name which was clicked or choosen via mouse of the file/dir from GUI to execute
    2. Open file/dir in VSC but if input == Books just open the directory
'''

import os
from tkinter import *
from tkinter import ttk
import glob


def displayer(textInput):
    lWithFiles = []
    for path, currentDirectory, files in os.walk("/Users/maxhager/Projects2022"):
        for file in files:
            if file.startswith(textInput) and file.endswith(".meta") == False and file.endswith(".mat") == False and file.endswith(".cs") == False:
                lWithFiles.append(os.path.join(path, file))
    return lWithFiles


def gui():
    # i need a search bar
    '''
    1. google for display bar, display search bar
        1. https://pythonguides.com/python-tkinter-search-box/ could be modified 
        2. https://stackoverflow.com/questions/28031329/how-do-i-display-search-results-in-python-tkinter-window he is planning to do exactly the same what i plan to do
    2. Implement 1.2x
    3. Implement search bar on top of the screen
        1. https://www.youtube.com/watch?v=0CXQ3bbBLVk can be directly combined with the input from 2.
    '''

    search = '*log'

    found_files = []

    for dirname, dirnames, filenames in os.walk('/Users/maxhager/Projects2022'):
        for i in glob.glob(dirname+'/'+search+'*'):
            print(i)
            found_files.append(i)

    root = Tk()
    root.geometry("640x480")

    listbox = Listbox(root)

    for a_file in found_files:
        listbox.insert(END, a_file)

    listbox.pack(fill=BOTH, expand=YES)

    root.mainloop()


if __name__ == "__main__":

    #print(displayer("P"))
    print(gui())
