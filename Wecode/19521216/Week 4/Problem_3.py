DIRECTION = {
    '^':[-1,0],
    'v':[1,0],
    '<':[0,-1],
    '>':[0,1],
    }
def get_key(val):
    for key, value in DIRECTION.items():
         if val == value:
             return key

def turn_direct(old_direct,direct):
    key_ = DIRECTION.keys()
    if (old_direct == '<' and direct == 'L') or (old_direct == '^' and direct =='R'):
        new_direct = [DIRECTION[old_direct][0] + 1,DIRECTION[old_direct][1] + 1]
    elif (old_direct == '>' and direct == 'L') or (old_direct == 'v' and direct =='R')  :
        new_direct = [DIRECTION[old_direct][0] - 1,DIRECTION[old_direct][1] - 1]
    elif (old_direct == '^'and direct == 'L') or (old_direct == '>' and direct =='R'):
        new_direct = [DIRECTION[old_direct][0] + 1,DIRECTION[old_direct][1] - 1]
    elif (old_direct == 'v'and direct == 'L') or (old_direct == '<' and direct =='R'):
        new_direct = [DIRECTION[old_direct][0] - 1,DIRECTION[old_direct][1] + 1]
    new_direct = get_key(new_direct)
    return new_direct
def find_head_position(matrix,n,m):
    for i in range (0,n):
        for j in range (0,m):
            if matrix[i][j] != '.' and matrix[i][j]!='*':
                return [i,j] ,matrix[i][j]
def find_body(matrix,head,n,m):
    up = [head[0]-1,head[1]]
    down = [head[0]+1,head[1]]
    left = [head[0],head[1]-1]
    right = [head[0],head[1]+1]
    if right[1] < m and matrix[right[0]][right[1]] == '*':
        return right
    if left[1] > 0 and matrix[left[0]][left[1]] == '*':
        return left
    if up[0] >0 and matrix[up[0]][up[1]] == '*':
        return up
    if down[0] < n and matrix[down[0]][down[1]] == '*' :
        return down
    return -1
def add_body(matrix,n,m,head):
    snake = []
    head_tmp = head
    snake.append(head_tmp)
    while True :      
        head_tmp = find_body(matrix,head_tmp,n,m)
        if head_tmp == -1:
            return snake
        else:           
            snake.append(head_tmp)
            matrix[head_tmp[0]][head_tmp[1]] = '/'

def move(snake,command,direct,n,m):
    step = DIRECTION[direct]
    if command =='F':
        snake_next =[snake[0][0] + step[0],snake[0][1] + step[1]]
        if snake_next[0] < 0 or snake_next[0] > n-1 or snake_next[1] < 0 or snake_next[1] > m-1: 
                return snake,direct,-1
        if snake_next not in snake[:-1]:
            old = snake[0]
            snake[0] = snake_next
            for i in range (0,len(snake)-1):
                before_change = snake[i+1]
                snake[i+1] = old
                old = before_change
        else:
            return snake,direct,-1  
    else:
        direct = turn_direct(direct,command)
    return snake,direct,0
def draw_snake(snake,n,m,direct):
    for i in range(0,n):
        for j in range(0,m):
            if [i,j] not in snake:
                print('.',end='')
            else:
                if [i,j] == snake[0]:
                    print(direct,end='')
                else:
                    print('*',end='')
        print()
def draw_snake_dead(snake,n,m,direct):
    for i in range(0,n):
        for j in range(0,m):
            if [i,j] not in snake:
                print('.',end='')
            else:
                print('X',end='')
        print() 
matrix_position = []
matrix =[]
n,m,c = [int(x) for x in input().split()]
head_position = []
snake = []
for i in range(0,n):
    matrix_position = [str(x) for x in input()]
    matrix.append(matrix_position)
move_direct = [str(x) for x in input()]
head_position,direct=find_head_position(matrix,n,m)

snake = add_body(matrix,n,m,head_position)

for i in move_direct:
    snake,direct,next = move(snake,i,direct,n,m)
    if next == -1:
        draw_snake_dead(snake,n,m,direct)
        exit()
draw_snake(snake,n,m,direct)

#while True:
#    try:
#        i = input()
#        snake,direct,next = move(snake,i,direct,n,m)
#        if next == -1:
#            draw_snake_dead(snake,n,m,direct)
#        else:
#            draw_snake(snake,n,m,direct)
#    except :
#        pass