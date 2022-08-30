import pyperclip
import pickle


def displayClipboardHistory(reconstructed):
    printString = ""
    for i in range(len(reconstructed)):
        if len(reconstructed[i]) > 20:
            dots = "..."
            lineBreak = "\n"
        else:
            dots = ""
            lineBreak = ""
        printString = printString + \
            str(i+1) + " " + reconstructed[i][0:20] + dots + lineBreak + "\n"
    return printString


def respondToInput(reconstructed):

    inp = int(input())
    l = []

    for i in range(len(reconstructed)):
        l.append(i+1)

    if inp not in l:
        print("Wrong option.")
        exit()
    else:
        content = reconstructed[inp-1]
        pyperclip.copy(content)
        if len(content) > 20:
            dots = "..."
        else:
            dots = ""
        print(content[0:20] + "{dots}".format(dots="..." if dots ==
              "..." else "") + " was copied to clipboard.")


if __name__ == "__main__":
    with open("clipboardHistory.txt", "rb") as infile:
        reconstructed = pickle.load(infile)

    print(displayClipboardHistory(reconstructed))
    respondToInput(reconstructed)
