import pyperclip

def test():
    with open('clipboardHistory.txt', 'a') as f:
        f.write("hdshhd")
        f.write("\nNAECHST\n")

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
        f.write(current)
        f.write("\nNAECHSTE")

def keyBoardListener():
    with open('clipboardHistory.txt', 'r') as f:
        data = f.readlines()
    if len(data) == 0:
        pastContent = " "
    else:
        pastContent = data[-1]
    # todo check that \n does not make a difference here
    currentContent = pyperclip.paste()
    if currentContent.split() != pastContent.split():
        print("should not appear more than once")
        pastContent = currentContent
        return True
    return False

if __name__ == "__main__":
    #test()
    #what is the problem here now? 
    #i need to check if the input from clibboard is the same or not from last line of txt file 
    #i could try to put everything into one file. 
    with open('clipboardHistory.txt', 'r') as f:
        data = f.readlines()
    print([data[4]])
    '''while True:
        trigger = keyBoardListener()
        if trigger:
            saveCurrentItem()'''
