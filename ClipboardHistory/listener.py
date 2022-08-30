import pyperclip
from hashlib import sha256
from curses import keyname
import pickle
from pynput import keyboard

sha = sha256("s".encode('utf-8')).hexdigest()
clipBoard = []
pastContent = ""


def writeToFile(current):
    with open("/Users/maxhager/Projects2022/PythonWorkflowScripts/ClipboardHistory/clipboardHistory.txt", "wb") as outfile:
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


def on_press(key):
    global pastContent
    currentContent = pyperclip.paste()
    if currentContent != pastContent:
        if currentContent != None:
            saveCurrentItem(currentContent)
        pastContent = currentContent


if __name__ == "__main__":
    for i in range(10):
        clipBoard.append(sha)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
