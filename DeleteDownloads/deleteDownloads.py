import os
import shutil


def deleteDownloads():
    dir = "/Users/maxhager/Downloads"
    shutil.rmtree(dir, ignore_errors=True)
    print("Deleted '%s' directory successfully" % dir)


if __name__ == "__main__":
    deleteDownloads()
