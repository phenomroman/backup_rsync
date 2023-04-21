#! /usr/bin/env python3

import sys
import os
import subprocess
# from multiprocessing import Pool

src = sys.argv[1]
dest = sys.argv[2]

def rsync(src_file):
  subprocess.run(['rsync', '-arq', src_file, dest])

files_to_sync = []

for (dir, dirnames, filenames) in os.walk(src):
  for filename in filenames:
    src_file = os.path.join(dir, filename)
    files_to_sync.append(src_file)
    break

print(files_to_sync)