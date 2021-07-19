def NowMove(grid : list, m : tuple, n):
    #Find Princess Position
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'p':
                p = (x, y)
                break
    #Calculate Move
    h, v = (m[0] - p[0], m[1] - p[1])
    #Change Value To Output
    x = 'LEFT' if h > 0 else 'RIGHT' if h < 0 else 0
    y = 'UP' if v > 0 else 'DOWN' if v < 0 else 0
    #Return Move
    return (x if y == 0 else y)
grid = []
n = int(input())
p = ''
# Make Bot Position
m = tuple(int(i) for i in input().strip().split())[::-1]
#Make Grid
for i in range(n):
    grid.append(list(input()))
#Print Now Move
print(NowMove(grid, m, n))
