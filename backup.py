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

if __name__ == "__main__":
  #get the number of processors to use
  pool = Pool(processes=os.cpu_count())
  #decide the directories to sync for backup
  dir_to_sync = []
  for (root, dirnames, filenames) in os.walk(src):
    for dirname in dirnames:
      dir = os.path.join(root, dirname)
      dir_to_sync.append(dir)
    break
  #sync files using multiprocessors
  pool.map(rsync, dir_to_sync)