from bs4 import UnicodeDammit
import os.path


def toUTF8(filePath):
    with open('input\\' + filePath, 'rb') as file:
        string = file.read()
        dammit = UnicodeDammit(string)
        encoding = dammit.original_encoding
        string = string.decode(encoding).encode('utf8')
        dirName = os.path.dirname('output\\' + filePath)
        if os.path.exists(dirName) == False:
            os.makedirs(dirName)
        with open('output\\' + filePath, 'wb+') as output:
            output.write(string)
