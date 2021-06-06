import wave
import numpy as np
from os import listdir, remove
from sys import argv

# 1 channel RIFF @ 32000 bps, 16000 Hz, 1.seconds


def save_wav_channel(fn, wav, channel):
    '''
    Take Wave_read object as an input and save one of its
    channels into a separate .wav file.
    '''
    # Read data
    nch = wav.getnchannels()
    print(nch)
    depth = wav.getsampwidth()
    wav.setpos(0)
    sdata = wav.readframes(wav.getnframes())

    # Extract channel data (24-bit data not supported)
    typ = {1: np.uint8, 2: np.uint16, 4: np.uint32}.get(depth)
    if not typ:
        raise ValueError("sample width {} not supported".format(depth))
    if channel >= nch:
        raise ValueError(
            "cannot extract channel {} out of {}".format(channel+1, nch))
    print("Extracting channel {} out of {} channels, {}-bit depth".format(channel+1, nch, depth*8))
    data = np.fromstring(sdata, dtype=typ)
    ch_data = data[channel::nch]

    # Save channel to a separate file
    outwav = wave.open(fn, 'w')
    outwav.setparams(wav.getparams())
    outwav.setnchannels(1)
    outwav.writeframes(ch_data.tostring())
    outwav.close()


files = listdir(argv[1])
except_list = ['_DI', '_MN']
for f in files:
    try:
        if f[:3] in except_list or f == '.DS_Store':
            continue
        wav = wave.open('{}/{}'.format(argv[1], f))
        save_wav_channel('{}/_{}_ch1.wav'.format(argv[1], f), wav, 0)
        save_wav_channel('{}/_{}_ch2.wav'.format(argv[1], f), wav, 1)
    except Exception as e:
        print('{}: {}'.format(f, e))
        remove('{}/{}'.format(argv[1], f))
        remove('{}/_{}_ch1.wav'.format(argv[1], f))
        remove('{}/_{}_ch2.wav'.format(argv[1], f))
