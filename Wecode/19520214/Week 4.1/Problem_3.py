def getsnakePoints():
    ruleChars = ['<', '^', '>', 'v']
    global n, m, _map
    headPoint = (-1, -1)
    bodyPoints = []
    for i in range(n):
        for j in range(m):
            if _map[i][j] in ruleChars:
                headPoint = (i, j)
            if _map[i][j] == '*':
                bodyPoints.append((i, j))
    return headPoint, bodyPoints

def getDirHeadsnake(headPoint):
    global _map
    x = _map[headPoint[0]][headPoint[1]]
    if x == '<':
        return 0
    elif x == '^':
        return 1
    elif x == '>':
        return 2
    elif x == 'v':
        return 3
    return 0

def checkPoint(point):
    global n, m, _map
    return 0 <= point[0] < n and 0 <= point[1] < m

def getCharHeadsnake(x):
    ruleChars = ['<', '^', '>', 'v']
    if x < 0:
        x += 4
    return ruleChars[x % 4]

def printResult():
    global _map
    for i in _map:
        print(*i, sep="")
    exit()

def printResultExit():
    global _map, snakePoints
    for point in snakePoints:
        _map[point[0]][point[1]] = 'X'
    for i in _map:
        print(*i, sep="")
    exit()

def getNearPoint(listPoint, point):
    _l = (point[0], point[1] - 1)
    _u = (point[0] - 1, point[1])
    _r = (point[0], point[1] + 1)
    _d = (point[0] + 1, point[1])
    if _l in listPoint:
        return _l
    if _u in listPoint:
        return _u
    if _r in listPoint:
        return _r
    if _d in listPoint:
        return _d

def getFullsnakePoints(headPoint, bodyPoints):
    result = [headPoint]
    tmp = headPoint
    while len(bodyPoints) > 0:
        tmp = getNearPoint(bodyPoints, tmp)
        result.append(tmp)
        del bodyPoints[bodyPoints.index(tmp)]
    result.reverse()
    return result

def checkHeadPoint(newHeadPoint, snakePoints):
    global _map, n, m
    if newHeadPoint in snakePoints[1:]:
        printResultExit()
    if newHeadPoint[0] < 0 or newHeadPoint[0] > n - 1:
        printResultExit()
    if newHeadPoint[1] < 0 or newHeadPoint[1] > m - 1:
        printResultExit() 
    return  

def checkAfterRotate(headPoint, snakePoints):
    rulesPoints = [
        (0, -1),    #L
        (-1, 0),    #U
        (0, 1),     #R
        (1, 0)      #D
    ]
    x = getDirHeadsnake(headPoint)
    newHeadPoint = tuple(map(sum, zip(headPoint, rulesPoints[x])))
    checkHeadPoint(newHeadPoint, snakePoints)

def movesnake(snakePoints, control):
    global _map
    rulesPoints = [
        (0, -1),    #L
        (-1, 0),    #U
        (0, 1),     #R
        (1, 0)      #D
    ]
    headPoint = snakePoints[len(snakePoints) - 1]
    dirHeadsnake = getDirHeadsnake(headPoint) 
    if control == 'L':
        _map[headPoint[0]][headPoint[1]] = getCharHeadsnake(dirHeadsnake - 1)
        # checkAfterRotate(headPoint, snakePoints)
    elif control == 'R':
        _map[headPoint[0]][headPoint[1]] = getCharHeadsnake(dirHeadsnake + 1)
        # checkAfterRotate(headPoint, snakePoints)
    elif control == 'F':
        newHeadPoint = tuple(map(sum, zip(headPoint, rulesPoints[dirHeadsnake])))
        checkHeadPoint(newHeadPoint, snakePoints)
        snakePoints.append(newHeadPoint)
        _map[newHeadPoint[0]][newHeadPoint[1]] = getCharHeadsnake(dirHeadsnake)
        lastPoint = snakePoints[0]
        if newHeadPoint == lastPoint:
            snakePoints.pop(0)
            lastPoint = snakePoints[0]
            _map[lastPoint[0]][lastPoint[1]] = '*'
        else:
            lastPoint = snakePoints.pop(0)
            _map[headPoint[0]][headPoint[1]] = '*'
            _map[lastPoint[0]][lastPoint[1]] = '.'

n, m, c = [int(x) for x in input().split()]
_map = []
for r in range(n):
    _map.append([str(x) for x in input().strip()])
s = input()

headPoint, bodyPoints = getsnakePoints()

snakePoints = getFullsnakePoints(headPoint, bodyPoints)

for i in s:   
    movesnake(snakePoints, i.upper())

printResult()