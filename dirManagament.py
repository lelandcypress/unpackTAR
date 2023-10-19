import os
tarFile = "CompressedYT"
checksumFile = "TarHash.txt"


def file_path(targetDir,*file):
    home = os.path.expanduser('~')
    if file:
        download_path = os.path.join(home, targetDir, *file)
    else:
        download_path = os.path.join(home, targetDir)
    return download_path




