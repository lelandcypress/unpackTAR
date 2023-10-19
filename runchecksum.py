import hashlib
from dirManagament import *
def runCheckSum():
    block = 65000
    file_hash = hashlib.sha256()
    with open(tarFile,'rb') as f:
        blockread= f.read(block)
        while len(blockread) > 0:
            file_hash.update(blockread)
            blockread = f.read(block)
    final_digest = file_hash.hexdigest()
    try:
        with open(checksumFile, 'r') as f:
            YTChecksum = f.read()
            if final_digest == YTChecksum:
                return True
    except Exception as e:
                exit(e)
