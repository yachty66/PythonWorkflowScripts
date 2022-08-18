import requests
import os

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


def getFilename():
    r = requests.get(url)
    path = "/Users/maxhager/Projects2022/PythonWorkflowScripts/BackgroundImage/backgroundImage/"
    titleUrl = r.json()['title'].replace(" ", "")
    filename = path + titleUrl + ".png"
    return filename


def downloadImageToday():
    r = requests.get(url)
    if r.status_code != 200:
        print('error')
        return
    pictureUrl = r.json()['url']
    if "jpg" not in pictureUrl:
        print("No image for today, must be a video")
    else:
        pic = requests.get(pictureUrl, allow_redirects=True)
        filename = getFilename()
        open(filename, 'wb').write(pic.content)
        print(f"saved picture of the day to {filename}!")


if __name__ == '__main__':
    downloadImageToday()
    filename = getFilename()
    cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + filename + "\"'"
    os.system(cmd)
