import os
import sys
import shutil
import time

files = os.listdir(sys.argv[1])
excepts = ['.DS_Store']
files = list(set(files) - set(excepts))

for file in files:
    if file == '.DS_Store':
        os.remove('{}/{}'.format(sys.argv[1], file))
        continue
    old_file_path = os.path.join('{}/{}'.format(sys.argv[1], file))
    new_file_path = os.path.join('{}/_{}'.format(sys.argv[1], file))
    os.system(
        'ffmpeg -y -i {} -map_metadata -1 -codec copy {}'.format(
            old_file_path,
            new_file_path
        )
    )
    time.sleep(0.5)
