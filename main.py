import encoder
import os
for root, dirs, files in os.walk("./input/", topdown=False):
    for name in files:
        print('Encoding', root, name)
        encoder.toUTF8(root.replace('./input/', '') + '\\' + name)
