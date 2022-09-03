import os

def runScript():
    cmd = 'osascript -e \'tell application "Google Chrome" to activate\' -e \'tell application "System Events" to tell process "Google Chrome" to keystroke "f" using {command down, control down}\''
    os.system(cmd)

if __name__ == "__main__":
    runScript()
