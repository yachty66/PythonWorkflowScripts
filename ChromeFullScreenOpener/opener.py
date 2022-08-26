"""
Options:
    - Open chrome with selenium in maximized window
        - Gch opens up but not for python
    - Open chrome with subprocess(webbrowser) and if this happens execute shortcut for maximizing with pyautogui
"""
# approach selenium
'''import subprocess
from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/opt/homebrew/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#driver = webdriver.Chrome("/opt/homebrew/bin/chromedriver")
driver.get('https://google.com')

driver.maximize_window()'''

# approach pyautogui


"""
Options for executing script if google chrome launches
    1. Python script which gets executed every second with cron and checks if chrome is running if yes execute full screen code
        - schedule cronjob directly from python script
    2. Research for applications which check faster than one second
        - https://apple.stackexchange.com/questions/210910/run-automator-workflow-or-shell-script-at-application-launch-shutdown
    3. Research if there exist something like an binding to an app
        - https://superuser.com/questions/756853/how-to-automate-shell-script-to-run-when-i-open-a-particular-app-in-osx
        - https://apple.stackexchange.com/questions/224394/how-to-make-a-mac-os-x-app-with-a-shell-script
        - using automator for doing this
        - https://apple.stackexchange.com/questions/153286/can-launching-an-app-trigger-the-launch-of-another-app
        
        
        /Applications/AppicationsMe/Google\ Chrome.app/Contents/MacOS/Google\ Chrome ; exit && python3 /Users/maxhager/Projects2022/PythonWorkflowScripts/ChromeFullScreenOpener/opener.py ;
    
"""

#subprocess.call(["open", "-a", "Google Chrome"])
#p1 = subprocess.Popen(["open", "https://www.google.com/"])
# p1.wait()
# while window size is not full size

# the problem is on pyautogui side
# what if i use instead of shortcuts my mouse for increasing screen size?
# i need to figure the exact position and than click with mouse. is a problem if this mouse does not move independent from my mouse
# i can create two functions and make them sync together




import subprocess
import pyautogui
import time
import webbrowser
import psutil
def openChrome():
    webbrowser.open('https://www.google.com/')


def fullScreen():
    while(True):
        if ("Google Chrome" in (i.name() for i in psutil.process_iter())):
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('command')
            pyautogui.keyDown('f')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('command')
            pyautogui.keyUp('f')
            break


if __name__ == "__main__":
    openChrome()
    fullScreen()


# i could check if a process is running and than execute my code. i need
# pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copya
#pyautogui.hotkey('command', 'v')
# pyautogui.screenshot()
