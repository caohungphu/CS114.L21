from sys import maxsize

ruleConnects = {
    'L': {  
        '2': 'L',     
        '3': 'D', 
        '6': 'U',
        '7': 'L'
    },

    'R': {
        '2': 'R', 
        '4': 'D',
        '5': 'U',
        '7': 'R'
    },
    
    'D': { 
        '1': 'D', 
        '5': 'L',
        '6': 'R',
        '7': 'D'
    },

    'U': {
        '1': 'U', 
        '3': 'R', 
        '4': 'L',
        '7': 'U'
    }
}

ruleMoves = {
    "L": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1)
}


def getMapInput(a):
    tramBom = {}
    hoChua = {}
    num_chars = ['0', '1', '2', '3', '4', '5', '6', '7']
    for i in range(n):
        for j in range(len(a[i])):
            if a[i][j].islower():
                tramBom[a[i][j]] = (i, j)
            elif a[i][j].isupper():
                hoChua[a[i][j]] = (i, j)
    return tramBom, hoChua

def checkPoint(point):
    global n, m
    return 0 <= point[0] < n and 0 <= point[1] < m

def getPath(control, current_path, end, result):
    global _map, _map_bool
    error = 0
    x, y = tuple(map(sum, zip(current_path[-1], ruleMoves[control])))
    if checkPoint((x, y)) and (x, y) == end:
        result = current_path
    elif checkPoint((x, y)) and _map[x][y] in ruleConnects[control]:
        return getPath(ruleConnects[control][_map[x][y]], current_path + [(x, y)], end, result)
    else:  
        error = 1
        result = current_path
    return result, error 

def getResult(fullPath, fullPath_bool):
    result = set()
    error, _min_error = 0, maxsize
    for path, path_bool in zip(fullPath, fullPath_bool):
        if path_bool == 1:
            _min_error = min(_min_error, len(path))
            error = 1
    for path in fullPath:
        if error:
            path = path[:_min_error]
        result |= set(path)
    return len(result) * (-1 if error else 1)


# f = open('input_2.txt', 'r')
# n = int(f.readline())
# _map = []
# for r in range(n):
#     _map.append([str(x) for x in f.readline().strip()])
# m = len(_map[0])

n = int(input())
_map = []
for r in range(n):
    _map.append([str(x) for x in input().strip()])
m = len(_map[0])

tramBom, hoChua = getMapInput(_map)

fullPath = []
fullPath_bool = []

for i in tramBom:
    start = tramBom[i]
    end = hoChua[i.upper()]
    for rule in ruleMoves:
        x, y = tuple(map(sum, zip(start, ruleMoves[rule])))
        if checkPoint((x, y)) and _map[x][y] in ruleConnects[rule]:
            subPath, error = getPath(ruleConnects[rule][_map[x][y]], [(x, y)], end, [])
            fullPath.append(subPath)
            fullPath_bool.append(error)         
    
print(getResult(fullPath, fullPath_bool))