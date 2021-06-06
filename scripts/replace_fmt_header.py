filename = 'DI_Floor__Tom_Rim_1111.1.wav'

with open(filename, 'rb') as f:
    # header = f.read(44)  # big/ little/ big
    header_riff = f.read(12)
    header_corrupted = f.read(4) # to replace as fmt
    body = f.read()
    result = header_riff + bytearray(b'fmt ') + body

with open('result.wav', 'wb') as f:
    f.write(result)
