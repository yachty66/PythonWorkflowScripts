import subprocess
import pyautogui
import time
import webbrowser
import psutil
import os
'''
1. on start 
    - https://superuser.com/a/756866
        - options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
        - not possible because of hex code encryption
chrome_driver_binary = "/opt/homebrew/bin/chromedriver"
    - if exe gets called call instead different script
    - create a bundle which contains the script and the exe of chrome 
2. check every second
3. instead
4. create a normal script which opens chrome and the script and I use this script form cmd to start chrome in full screen
5. applescript in automator app which opens chrome and the script
    - create apple script which opens chrome and the script
    - first create apple script which opens chrome and add this to automator (on click chrome should open now)
    - add pytons scrit to applescript 
        - if this does not work create a single apple script which runs python script which opens chrome only
        - 

'''
def runScript():
    #open chrome with apple script
    #open = subprocess.Popen(['osascript', '-e', 'tell application "Google Chrome" to open location "https://www.google.com"'])
    #if on start eventually while to check if chrome is open / running
    cmd = 'osascript -e \'tell application "Google Chrome" to activate\' -e \'tell application "System Events" to tell process "Google Chrome" to keystroke "f" using {command down, control down}\''
    os.system(cmd)
    #subprocess.Popen('osascript -e \'tell application "Google Chrome" to activate\' -e \'tell application "System Events" to tell process "Google Chrome" to keystroke "f" using {command down, control down}\'', shell=True)

if __name__ == "__main__":
    runScript()
