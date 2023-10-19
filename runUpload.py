import tarfile
from dirManagament import *
import os
from datetime import datetime
import shutil
today = datetime.today()
year = today.strftime('%Y')
month = today.strftime('%m')
day = today.strftime('%d')
orgYTFolder = "YouTubeDownloads"
#starts with decompressing TAR files in target directory

#checks for videos directory to verify we are in the correct node
def findDir():
    if os.path.exists("videos"):
        decompressVids()
    else:
        print("Video Folder not found")

def decompressVids():
    with tarfile.open(tarFile, 'r:bz2')as tar:
        tar.extractall()
        tar.close()
    moveFiles()

# Verifies files are placed in the correct file path. YouTube node makes use of a YYYY/MM/DD folder hierarchy.
# This script creates this hierachy based on the current date.
def moveFiles():
    basedir = "videos"
    todaysDate = [year,month,day]
    for component in todaysDate:
        sourcedir = os.path.join(basedir,component)
        if not os.path.exists(sourcedir):
            os.makedirs(sourcedir)
        basedir = sourcedir

    for video in os.listdir(orgYTFolder):
        sourceVid = os.path.join(orgYTFolder,video)
        finalDestination = os.path.join(basedir, video)
        shutil.move(sourceVid ,finalDestination)


