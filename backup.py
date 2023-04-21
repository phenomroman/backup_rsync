#! /usr/bin/env python3

import sys
import os
import subprocess
from multiprocessing import Pool

#define source and destination directories
src = sys.argv[1]
dest = sys.argv[2]

#define function to use rsync through subprocess module
def rsync(src):
  subprocess.run(['rsync', '-arq', src, dest])

#decide the directories to sync for backup
dir_to_sync = []
for (root, dirnames, filenames) in os.walk(src):
  for dirname in dirnames:
    dir_to_sync.append(os.path.join(root, dirname))

if __name__ == "__main__":
  #sync files using multiprocessors
  pool = Pool(processes=os.cpu_count())
  pool.map(rsync, dir_to_sync)