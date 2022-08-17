'''
1. main 
2. def deleteD
3. delete all files from downloads folder
4. setup crontab for every sunday 0:01 (before check if it works with crontab)
4. add readme + clean code
5. push to github
6. watch video from python automation guy
'''
import os


def deleteDownloads():
    dir = "/Users/maxhager/Downloads"
    filelist = [f for f in os.listdir(dir)]
    for f in filelist:
        os.remove(os.path.join(dir, f))


if __name__ == "__main__":
    # execute only if run as a script
    deleteDownloads()
