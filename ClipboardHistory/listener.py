import pyperclip
from hashlib import sha256

sha = sha256("s".encode('utf-8')).hexdigest()


def test():
    with open('clipboardHistory.txt', 'r') as f:
        data = f.readlines()
    print(len(data))


def saveCurrentItem(current):
    with open(r"clipboardHistory.txt", 'r') as f:
        lines = len(f.readlines())

    if lines == 10:
        with open('clipboardHistory.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('clipboardHistory.txt', 'w') as fout:
            fout.writelines(data[1:])

    with open('clipboardHistory.txt', 'a') as f:
        print(current)
        f.write(sha + "\n" + str(current) + "\n" + sha + "\n")

globalVarOne = 1
globalVarTwo = 2

if __name__ == "__main__":

    # i could use dollar signs or unique hashes to mark beginning and end of line
    # i can just generate one 256hash which i than use all the time
    # add hash, add content, add hash...2
    # extract content between hashes and
    #i search for something where i can save my CBH to. txt file is suboptimal because i can only read lines from it 
    #better would be a var which i pass 
    #i could define variables for every number and than access them from the other script. that works. 
    pastContent = ""
    while True:
        currentContent = pyperclip.paste()
        if currentContent != pastContent:

            saveCurrentItem(currentContent)
            pastContent = currentContent
            # i save
