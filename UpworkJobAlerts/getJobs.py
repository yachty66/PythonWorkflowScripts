from distutils import config
import feedparser
from plyer import notification

NewsFeed = feedparser.parse(config.feed)


# get last title of first entry


def getCurrentTitle():
    entry = NewsFeed.entries[1]
    current = entry.title
    return current


def getLastTitle():
    with open('~/Projects2022/PythonWorkflowScripts/UpworkJobAlerts/lastTitle.txt', 'r') as f:
        lastTitle = f.read()
        return lastTitle


# check if new title is different than last title
def checkTitle():
    current = getCurrentTitle()
    last = getLastTitle()
    if current != last:
        return True

# empty file and write current title to file


def writeToFile():
    with open('~/Projects2022/PythonWorkflowScripts/UpworkJobAlerts/lastTitle.txt', 'w') as f:
        f.write(getCurrentTitle())


def sendNotification():
    with open('~/Projects2022/PythonWorkflowScripts/UpworkJobAlerts/lastTitle.txt', 'r') as f:
        title = f.read()
    notification.notify(title='Upwork Job Alert', message=title)


# main which calls all functions
if __name__ == "__main__":
    sendNotification()
    if checkTitle():
        writeToFile()
        sendNotification()
