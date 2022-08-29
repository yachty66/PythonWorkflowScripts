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

#execution and testing
# script needs to run all the time and if something was saved to CB than based on that execution
#


def keyBoardListener():
    # last line from file
    with open('clipboardHistory.txt', 'r') as f:
        data = f.readlines()
    if len(data) == 0:
        pastContent = " "
    else:
        pastContent = data[-1]
    #todo check that \n does not make a difference here 
    currentContent = pyperclip.paste()
    if currentContent != pastContent:
        pastContent = currentContent
        return True
    return False


if __name__ == "__main__":
    '''
    I need my event listener and if an event happens exe other methods
    I call this py script. this is why I need
    
    1. check if last item saved to file is different to current item --> if yes than write current to txt file 
    this adds new item to txt file if new item was added to history
    '''
    while True:
        trigger = keyBoardListener()
        if trigger:
            saveCurrentItem()
