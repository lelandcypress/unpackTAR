import hashlib
from runUpload import *
from runchecksum import *
import ctypes
if __name__ == '__main__':
    if runCheckSum():
        findDir()
    else:
        print("Checksum failed")
        exit()

