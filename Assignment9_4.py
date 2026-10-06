#Accept 2  File Names from User & compare contents from files if both have same contents then display Success otherwise Failure.

import sys
import hashlib

def hashfile(file):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:

        while True:
            data = f.read(BUF_SIZE)

            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

f1_hash = hashfile(sys.argv[1])
f2_hash = hashfile(sys.argv[2])

if f1_hash == f2_hash:
    print("Both files are same,","It's a Success")

else:
    print("Files are different,","It's a Failure.")

#command:python Assignment9_4.py Demo.txt Hello.txt.
#sha256 algorithm is used instead of MD5.