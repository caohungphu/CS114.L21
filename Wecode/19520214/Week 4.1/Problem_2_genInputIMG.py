_namefileinput = 'input.txt'
_namefilesave = 'Result.jpg'

f = open(_namefileinput, 'r')
n = int(f.readline())
_map = []
for r in range(n):
    _map.append([str(x) for x in f.readline().strip()])
m = len(_map[0])

import os
from PIL import Image
pathFile = 'Problem_2/'
list_file = [
    '0.png',
    '1.png',
    '2.png',
    '3.png',
    '4.png',
    '5.png',
    '6.png',
    '7.png',
]

def getListImage(a):
    result = []
    num_chars = ['0', '1', '2', '3', '4', '5', '6', '7']
    for i in range(n):
        for j in range(len(a[i])):
            if a[i][j].isupper():
                result.append(pathFile + a[i][j] + ".png")
            elif a[i][j].islower():
                result.append(pathFile + "_" + a[i][j] + ".png")
            else:
                result.append(pathFile + list_file[int(a[i][j])])
    return result

def getMapImage(a, namefile):
    _n = len(a) * 80
    _m = len(a[0]) * 80
    listFiles = getListImage(_map)
    result = Image.new("RGB", (_m, _n))
    for index, file in enumerate(listFiles):
        path = os.path.expanduser(file)
        img = Image.open(path).resize((80, 80))
        x = (index % m) * 80
        y = ((index // m) % n * 80)
        w, h = img.size
        result.paste(img, (x, y, x + w, y + h))
    result.save(namefile)

getMapImage(_map, _namefilesave)