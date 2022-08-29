import pyperclip


def saveCurrentItem():
    with open(r"clipboardHistory.txt", 'r') as f:
        lines = len(f.readlines())

    if lines == 10:
        with open('clipboardHistory.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('clipboardHistory.txt', 'w') as fout:
            fout.writelines(data[1:])

    current = pyperclip.paste()
    with open('clipboardHistory.txt', 'a') as f:
        f.write(current + '\n')


def displayClipboardHistory():
    printString = ""
    with open('clipboardHistory.txt', 'r') as f:
        data = f.readlines()
    for i in range(len(data)):
        printString = printString + str(i+1) + " " + data[i][0:20] + "..." + "\n"
    return printString


def respondToInput():
    inp = int(input())
    l = []
    with open(r"clipboardHistory.txt", 'r') as f:
        lines = len(f.readlines())
    for i in range(lines):
        l.append(i+1)

    if inp not in l:
        exit()
    else:
        with open('clipboardHistory.txt', 'r') as f:
            data = f.readlines()
        content = data[inp-1]
        pyperclip.copy(content)
        print(content[0:20] + " was copied to clipboard.")

#execution and testing
#script needs to run all the time and if something was saved to CB than based on that execution
#
def keyBoardListener():
    pastContent = ""
    currentContent = pyperclip.paste()
    if currentContent != pastContent:
        pastContent = currentContent
        return True
    return False
        
        
if __name__ == "__main__":
    '''
    I need my event listener and if an event happens exe other methods
    I call this py script. this is why I need
    '''
    while True:
        trigger = keyBoardListener()
        if trigger:
            #change in CB 
    
    
