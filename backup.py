#! /usr/bin/env python3

#import sys
import os
import subprocess
# from multiprocessing import Pool

src = "change_domain"
dest = "backup_change_domain"

def rsync(src_file):
  subprocess.run(['rsync', '-arq', src_file, dest])

files_to_sync = []

for (dir, dirnames, filenames) in os.walk(src):
  for filename in filenames:
    src_file = os.path.join(dir, filename)
    files_to_sync.append(src_file)
    break

