def NextMove(b,dirty):
    least = abs(b[0] - dirty[0][0]) + abs(b[1] - dirty[0][1])
    least_dirty = dirty[0]
    for d in dirty:
        move = abs(b[0] - d[0]) + abs(b[1] - d[1])
        if least > move:
            least = move
            least_dirty = d
        elif least < move:
            break
    v, h = least_dirty
    if h > b[1]:
        return least_dirty, 'RIGHT'
    elif h < b[1]:
        return least_dirty, 'LEFT'
    elif v > b[0]:
        return least_dirty, 'DOWN'
    elif v < b[0]:
        return least_dirty, 'UP'
    else:
        return least_dirty, 'CLEAN'
def FindDirty(board):
    dirty = []
    for col in range(5):
        for row in range(5):
            if board[col][row] == 'd':
                dirty.append(tuple((col, row)))
    return dirty
b = tuple(int(i) for i in input().strip().split())
Dirty = FindDirty([list(input()) for i in range(5)])
dirt, dir = NextMove(b, Dirty)
print(dir)
