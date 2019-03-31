def h_n(xSaatIni,ySaatIni,xAkhir,yAkhir) : #saatIni= titik tersebut, akhir= titik finish
    return abs(xSaatIni - xAkhir) + abs(ySaatIni - yAkhir) #manhattan distance

def g_n(parent,xAwal,yAwal,xSaatIni,ySaatIni) : #parent = list of parent, xAwal yAwal = titik masukan
    jumlah = 1
    if (not(isParentEmpty(parent))) :
        while (not(ketemu(xAwal,yAwal,xSaatIni,ySaatIni))) :
            found = False
            i = 0
            while (not(found) and i < len(parent)) :
                if (xSaatIni == parent[i][2] and ySaatIni == parent[i][3]) :
                    found = True
                    xSaatIni = parent[i][0]
                    ySaatIni = parent[i][1]
                i = i + 1
            jumlah = jumlah + 1
    return jumlah

def f_n(parent,xAwal,yAwal,xSaatIni,ySaatIni,xAkhir,yAkhir) :
    return g_n(parent,xAwal,yAwal,xSaatIni,ySaatIni) + h_n(xSaatIni,ySaatIni,xAkhir,yAkhir)

def takef_n(elem) :
    return elem[0]

def isParentEmpty(parent) :
    return len(parent) == 0

def cekParent(parent,x,y) : #untuk ngecek apakah titik itu udh ada di list parent sbg parent atau belum
    found = False
    for i in range(len(parent)) :
        if (x == parent[i][0] and y == parent[i][1]) :
            found = True
    return found

def ketemu(xAwalBaru,yAwalBaru,xAkhir,yAkhir) :
    return (xAwalBaru == xAkhir and yAwalBaru == yAkhir)

def addPrio(prio,f_n,x,y) :
    if (len(prio) == 0) :
        prio.append([f_n,x,y])
    else :
        found = False
        i = 0
        while (not(found) and i < len(prio)) :
            if (prio[i][0] > f_n) :
                found = True
            else :
                i = i + 1
        if (found) :
            prio.insert(i,[f_n,x,y])
        else :
            prio.append([f_n,x,y])
            

def aStar(maze,xAwal,yAwal,xAkhir,yAkhir) : #awal= titik awal, akhir= titik akhir
    prio = [] #list priority queue isinya [f_n, x, y]
    parent = [] #list of titik parent isinya [x parent, y parent, x child, y child]
    xAwalBaru = xAwal 
    yAwalBaru = yAwal
    while (not(ketemu(xAwalBaru,yAwalBaru,xAkhir,yAkhir))) :
        if (maze[xAwalBaru][yAwalBaru + 1] == 0 and not(cekParent(parent,xAwalBaru,yAwalBaru + 1))) :#petak kanan
            xKanan = xAwalBaru
            yKanan = yAwalBaru + 1
            parent.append([xAwalBaru,yAwalBaru,xKanan,yKanan])
            f_nKanan = f_n(parent,xAwal,yAwal,xKanan,yKanan,xAkhir,yAkhir)
            addPrio(prio,f_nKanan,xKanan,yKanan)
            #prio.append([f_nKanan,xKanan,yKanan])

        if (yAwalBaru != 0) :
            if (maze[xAwalBaru][yAwalBaru - 1] == 0 and not(cekParent(parent,xAwalBaru,yAwalBaru - 1))) :#petak kiri
                xKiri = xAwalBaru
                yKiri = yAwalBaru - 1
                parent.append([xAwalBaru,yAwalBaru,xKiri,yKiri])
                f_nKiri = f_n(parent,xAwal,yAwal,xKiri,yKiri,xAkhir,yAkhir)
                addPrio(prio,f_nKiri,xKiri,yKiri)
                #prio.append([f_nKiri,xKiri,yKiri])

        if (maze[xAwalBaru + 1][yAwalBaru] == 0 and not(cekParent(parent,xAwalBaru + 1,yAwalBaru))) :#petak bawah
            xBawah = xAwalBaru + 1
            yBawah = yAwalBaru
            parent.append([xAwalBaru,yAwalBaru,xBawah,yBawah])
            f_nBawah = f_n(parent,xAwal,yAwal,xBawah,yBawah,xAkhir,yAkhir)
            addPrio(prio,f_nBawah,xBawah,yBawah)
            #prio.append([f_nBawah,xBawah,yBawah])

        if (xAwalBaru != 0) :
            if (maze[xAwalBaru - 1][yAwalBaru] == 0  and not(cekParent(parent,xAwalBaru - 1,yAwalBaru))) :#petak atas
                xAtas = xAwalBaru - 1
                yAtas = yAwalBaru
                parent.append([xAwalBaru,yAwalBaru,xAtas,yAtas])
                f_nAtas = f_n(parent,xAwal,yAwal,xAtas,yAtas,xAkhir,yAkhir)
                addPrio(prio,f_nAtas,xAtas,yAtas)
                #prio.append([f_nAtas,xAtas,yAtas])

        #prio.sort(key=takef_n) #sorting dengan key f_n yang berada di elem[0]

        xAwalBaru = prio[0][1]
        yAwalBaru = prio[0][2]

        del prio[0]

    printJalur = [] 
    xt = xAwalBaru
    yt = yAwalBaru
    printJalur.append([xt,yt])
    while (not(ketemu(xt,yt,xAwal,yAwal))) :
        found = False
        idx = 0
        while (not(found)) :
            if (parent[idx][2] == xt and parent[idx][3] == yt) :
                found = True
                xt = parent[idx][0]
                yt = parent[idx][1]
                printJalur.append([xt,yt])
                j = idx
            else :
                idx = idx + 1

    for i in range(len(printJalur)) :
        x = printJalur[i][0]
        y = printJalur[i][1]
        maze[x][y] = 8

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j]==8):
                print(" ", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

    print("\nAda sebanyak", len(printJalur), "langkah")