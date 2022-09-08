import os
import shutil
import glob


def deleteScreenshots():
    files = glob.glob("/Users/maxhager/Screenshots/*")
    for f in files:
        os.remove(f)


if __name__ == "__main__":
    deleteScreenshots()
