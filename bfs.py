import queue

# menampilkan matriks maze yang ada
def out(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (mat[i][j]==8):
                print(" ", end=" ")
            else:
                print(mat[i][j], end=" ")
        print()

# mengecek apakah suatu koordinat merupakan jalur yang dapat dilalui
def avail(x,y,bx,by,mat):
    return ((x>=0 and x<len(mat)) and (y>=0 and y<len(mat[x])) and (mat[x][y]==0 or (x==bx and y==by)))

# melakukan bfs dari a ke b
def bfs(ax,ay,bx,by,mat):
    antri = queue.Queue(0)
    antri.put((ax,ay))
    while not (antri.empty()):
        (x,y) = antri.get()
        mat[x][y] = 8
        if (x==bx and y==by):
            return True
        
        if (avail(x+1,y,bx,by,mat)):
            antri.put((x+1,y))

        if (avail(x-1,y,bx,by,mat)):
            antri.put((x-1,y))

        if (avail(x,y+1,bx,by,mat)):
            antri.put((x,y+1))

        if (avail(x,y-1,bx,by,mat)):
            antri.put((x,y-1))
    return False