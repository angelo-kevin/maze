import queue

# menampilkan matriks maze yang ada
def out(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if (mat[i][j]==8):
                print(" ", end=" ")
            else:
                print(mat[i][j], end=" ")
        print()

# mengecek apakah suatu koordinat merupakan jalur yang dapat dilalui
def avail(x,y,bx,by,mat):
    return ((x>=0 and x<len(mat)) and (y>=0 and y<len(mat[x])) and (mat[x][y]==0 or (x==bx and y==by)))

# melakukan bfs dari a ke b, sekaligus mengeset bobot pada tiap titik untuk mencari jalur yang ditempuh
def bfs(ax,ay,bx,by,mat):
    print("Penelusuran: ")
    bbt = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    antri = queue.Queue(0)
    antri.put((ax,ay))
    ctr = 0
    while not (antri.empty()):
        (x,y) = antri.get()
        mat[x][y] = 8
        bbt[x][y] = ctr
        ctr += 1
        if (x==bx and y==by):
            return bbt
        
        if (avail(x+1,y,bx,by,mat)):
            antri.put((x+1,y))

        if (avail(x-1,y,bx,by,mat)):
            antri.put((x-1,y))

        if (avail(x,y+1,bx,by,mat)):
            antri.put((x,y+1))

        if (avail(x,y-1,bx,by,mat)):
            antri.put((x,y-1))
    return None

# mengecek apakah suatu titik merupakan jalur dari penelusuran yang terjadi saat bfs
def avail2(x,y,bx,by,mat):
    return ((x>=0 and x<len(mat)) and (y>=0 and y<len(mat[x])) and (mat[x][y]==8 or (x==bx and y==by)))

# mencari titik awal dari titik akhir dengan mengikuti arah jalur yang dibentuk karena bfs
def jalur(bbt,ax,ay,x,y,mat):
    mat[x][y] = 5
    if (x==ax and y==ay):
        return
    else:
        if (avail2(x+1,y,ax,ay,mat) and (bbt[x][y]>=bbt[x+1][y])):
            jalur(bbt,ax,ay,x+1,y,mat)

        elif (avail2(x-1,y,ax,ay,mat) and (bbt[x][y]>=bbt[x-1][y])):
            jalur(bbt,ax,ay,x-1,y,mat)

        elif (avail2(x,y+1,ax,ay,mat) and (bbt[x][y]>=bbt[x][y+1])):
            jalur(bbt,ax,ay,x,y+1,mat)

        elif (avail2(x,y-1,ax,ay,mat) and (bbt[x][y]>=bbt[x][y-1])):
            jalur(bbt,ax,ay,x,y-1,mat)

# menghitung jumlah langkah yang yang dilalui dari titik awal ke titik akhir maze
def jumlah(mat):
    ctr = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j]==5):
                ctr += 1
    return ctr