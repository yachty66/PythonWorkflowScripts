import pyperclip

clipBoard = {}

def saveCurrentItem(current):
    #find out how to make vars thread safe and test with example
    #could set every var to sha and iter over var if var == sha set var to current and stop
    #else if name var == 10 and 10 != sha set var1 to value
    
    #in display access respective var name and print this one out
    
    #same problem with saving content to variables but i have everything seberated
    #instead of doing variables i could do a dict
    

'''def saveCurrentItem(current):
    with open(r"clipboardHistory.txt", 'r') as f:
        lines = len(f.readlines())

    if lines == 10:
        with open('clipboardHistory.txt', 'r') as fin:
            data = fin.read().splitlines(True)
        with open('clipboardHistory.txt', 'w') as fout:
            fout.writelines(data[1:])

    with open('clipboardHistory.txt', 'a') as f:
        print(current)
        f.write(str(current) + "\n")'''


if __name__ == "__main__":
    # i could use dollar signs or unique hashes to mark beginning and end of line
    # i can just generate one 256hash which i than use all the time
    # add hash, add content, add hash...2
    # extract content between hashes and
    # i search for something where i can save my CBH to. txt file is suboptimal because i can only read lines from it
    # better would be a var which i pass
    # i could define variables for every number and than access them from the other script. that works.
    pastContent = ""
    while True:
        currentContent = pyperclip.paste()
        if currentContent != pastContent:
            saveCurrentItem(currentContent)
            pastContent = currentContent
            # i save
