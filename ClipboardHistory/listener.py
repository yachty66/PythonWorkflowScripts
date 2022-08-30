import pyperclip
from hashlib import sha256
import time
import pickle

sha = sha256("s".encode('utf-8')).hexdigest()

clipBoard = []

def writeToFile(current):
    with open("clipboardHistory.txt", "wb") as outfile:
        pickle.dump(current, outfile)

def saveCurrentItem(current):
    bool = True
    global clipBoard
    for i in range(len(clipBoard)):
        if clipBoard[i] == sha:
            clipBoard[i] = current
            bool = False
            writeToFile(clipBoard)
            break
    if bool:
        clipBoard = clipBoard[1:]
        clipBoard.append(current)
        writeToFile(clipBoard)
        # is added at right place second and at end
        # gets filled up from back to front but needs to be filled up from forth to back
        #kann nix von rennenden python script abfragen 
        #was gibt es denn noch so für input output formate für python?


if __name__ == "__main__":
    for i in range(10):
        clipBoard.append(sha)
    pastContent = ""
    while True:
        currentContent = pyperclip.paste()  
        if currentContent != pastContent:
            if currentContent != None:
                saveCurrentItem(currentContent)
            pastContent = currentContent
        #print(clipBoard)
