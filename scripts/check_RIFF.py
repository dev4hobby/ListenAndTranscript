from os import listdir, remove
from sys import argv
from tensorflow.io import read_file
from tensorflow.audio import decode_wav

files = listdir(argv[1])
excepts = ['.DS_Store']
files = list(set(files) - set(excepts))

for file in files:
    filepath = '{}/{}'.format(argv[1], file)
    with open(filepath, 'rb') as f:
        try:
            raw_audio = read_file(filepath)
            waveform = decode_wav(raw_audio)
        except Exception as e:
            print('{}: {}'.format(filepath, e))
