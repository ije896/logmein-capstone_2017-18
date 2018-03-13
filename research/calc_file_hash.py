#!/usr/bin/env python3

# credit to https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

import sys
import hashlib



import glob

root_dir = "/Users/user/CS189AB/logmein-capstone_2017-18/research"

candidates = []

for filename in glob.iglob(root_dir + '**/*.mov', recursive=True):
    candidates.append(filename)

for filename in glob.iglob(root_dir + '**/*.mp4', recursive=True):
    candidates.append(filename)


BUF_SIZE = 65536  # read stuff in 64kb chunks!
for vid in candidates:
    print("candidate={}".format(vid))

    sha256 = hashlib.sha256()

    with open(vid, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    name = vid[len(root_dir)+1:] # get just the filename
    print("\nVideo={} => SHA256={}\n".format(name, sha256.hexdigest()))