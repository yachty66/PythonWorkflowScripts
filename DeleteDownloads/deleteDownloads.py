import os


def deleteDownloads():
    dir = "/Users/maxhager/Downloads"
    filelist = [f for f in os.listdir(dir)]
    for f in filelist:  
        os.remove(os.path.join(dir, f))


if __name__ == "__main__":
    deleteDownloads()
