import pyperclip

def displayClipboardHistory():
    printString = ""
    with open('clipboardHistory.txt', 'r') as f:
        data = f.readlines()
    for i in range(len(data)):
        if len(data[i]) > 20:
            dots = "..."
            lineBreak = "\n"
        else:
            dots = ""
            lineBreak = ""
        printString = printString + \
            str(i+1) + " " + data[i][0:20] + dots + lineBreak + "\n"
    return printString

def respondToInput():

    inp = int(input())
    l = []
    with open(r"clipboardHistory.txt", 'r') as f:
        lines = len(f.readlines())
    for i in range(lines):
        l.append(i+1)

    if inp not in l:
        print("Wrong option.")
        exit()
    else:
        with open('clipboardHistory.txt', 'r') as f:
            data = f.readlines()
        content = data[inp-1]
        pyperclip.copy(content)
        if len(content) > 20:
            dots = "..."
        else:
            dots = ""
        print(content[0:20] + "{dots}".format(dots="..." if dots ==
              "..." else "") + " was copied to clipboard.")

if __name__ == "__main__":
    print(displayClipboardHistory())
    respondToInput()
