def PrintMove(grid : list, n):
    #Find Bot Position
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'm':
                m = (x, y)
                break
    #Find Princess Position
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'p':
                p = (x, y)
                break
    #Calculate Move
    h, v = (m[0] - p[0], m[1] - p[1])
    #Change Value To Output
    x = 'LEFT' if h > 0 else 'RIGHT'
    y = 'UP' if v > 0 else 'DOWN'
    #Print Horizontal Move
    for i in range(abs(h)):
        print(x)
    #Print Vertical Move
    for i in range(abs(v)):
        print(y)
grid = []
p = ''
m = ''
n = int(input())
#Make Grid
for i in range(n):
    grid.append(list(input()))
FindPosition(grid, n)def FindPosition(grid : list, n):
    #Find Bot Position
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'm':
                m = (x, y)
                break
    #Find Princess Position
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'p':
                p = (x, y)
                break
    #Calculate Move
    h, v = (m[0] - p[0], m[1] - p[1])
    #Change Value To Output
    x = 'LEFT' if h > 0 else 'RIGHT'
    y = 'UP' if v > 0 else 'DOWN'
    #Print Horizontal Move
    for i in range(abs(h)):
        print(x)
    #Print Vertical Move
    for i in range(abs(v)):
        print(y)
grid = []
p = ''
m = ''
n = int(input())
#Make Grid
for i in range(n):
    grid.append(list(input()))
#Print Move
PrintMove(grid, n)
