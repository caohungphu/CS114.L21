colors = input().split()
moves = input().split()
dot = input()

def init_pyraminx(colors):
    return [[i] * 9 for i in colors]

def get_newColors(pyraminx, listPos, isLeft):
    oldColors = [pyraminx[r][c] for r, c in listPos]
    i = len(oldColors) // 3
    if isLeft:
        return oldColors[i:] + oldColors[:i]
    return oldColors[-i:] + oldColors[:-i] 

def move_pyraminx(pyraminx, moves):
    moves_step = {
        "U": [
            (0, 0),
            (3, 8),
            (2, 4)
        ],
        "u": [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (3, 8), (3, 3), (3, 7), (3, 6),
            (2, 4), (2, 6), (2, 5), (2, 1)
        ],
        "B": [
            (1, 0),
            (2, 8),
            (3, 4)
        ],
        "b": [
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 8), (2, 3), (2, 7), (2, 6),
            (3, 4), (3, 6), (3, 5), (3, 1)
        ],
        "L": [
            (2, 0),
            (1, 8),
            (0, 4)
        ],
        "l": [
            (2, 0), (2, 1), (2, 2), (2, 3),
            (1, 8), (1, 3), (1, 7), (1, 6),
            (0, 4), (0, 6), (0, 5), (0, 1)
        ],
        "R": [
            (3, 0),
            (0, 8),
            (1, 4)
        ],
        "r": [
            (3, 0), (3, 1), (3, 2), (3, 3),
            (0, 8), (0, 3), (0, 7), (0, 6),
            (1, 4), (1, 6), (1, 5), (1, 1)
        ],
        
    }
    for move in reversed(moves):
        isLeft = "'" not in move
        listPos = moves_step[move[0]]
        newColors = get_newColors(pyraminx, listPos, isLeft)
        for (r, c), color in zip(listPos, newColors):
            pyraminx[r][c] = color
    return pyraminx

_py = init_pyraminx(colors)
move_pyraminx(_py, moves)

for i in _py:
    print(*i, sep=" ")