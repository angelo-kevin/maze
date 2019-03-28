def h_n(xSaatIni,ySaatIni,xAkhir,yAkhir) : #saatIni= titik tersebut, akhir= titik finish
    return abs(xSaatIni - xAkhir) + abs(ySaatIni - yAkhir) #manhattan distance

def g_n(parent,xAwal,yAwal,xSaatIni,ySaatIni) : #parent = list of parent, xAwal yAwal = titik masukan
    jumlah = 1
    while (xSaatIni != xAwal and ySaatIni != yAwal) :
        found = False
        i = 0
        while (not(found)) :
            if (xSaatIni == parent[i][0] and ySaatIni == parent[i][1]) :
                found = True
                xSaatIni = parent[i][2]
                ySaatIni = parent[i][3]
        jumlah = jumlah + 1
    return jumlah

def f_n(parent,xAwal,yAwal,xSaatIni,ySaatIni,xAkhir,yAkhir) :
    return g_n(parent,xAwal,yAwal,xSaatIni,ySaatIni) + h_n(xSaatIni,ySaatIni,xAkhir,yAkhir)

def takef_n(elem) :
    return elem[0]

def aStar(maze,xAwal,yAwal,xAkhir,yAkhir) : #awal= titik awal, akhir= titik akhir
    prio = [] #list priority queue isinya [f_n, x, y]
    awal = maze[xAwal][yAwal] #titik mulai
    parent = [] #list of titik parent isinya [x parent, y parent, x child, y child]
    xAwalBaru = xAwal 
    yAwalBaru = yAwal
    
    while (xAwalBaru != xAkhir and yAwalBaru != yAkhir) :
        if (maze[xAwalBaru][yAwalBaru + 1] == 0) :#petak atas
            xAtas = xAwalBaru
            yAtas = yAwalBaru + 1
            parent.append([xAwalBaru,yAwalBaru,xAtas,yAtas])
            f_nAtas = f_n(parent,xAwal,yAwal,xAtas,yAtas,xAkhir,yAkhir)
            prio.append([f_nAtas,xAtas,yAtas])

        if (maze[xAwalBaru][yAwalBaru - 1] == 0) :#petak bawah
            xBawah = xAwalBaru
            yBawah = yAwalBaru - 1
            parent.append([xAwalBaru,yAwalBaru,xBawah,yBawah])
            f_nBawah = f_n(parent,xAwal,yAwal,xBawah,yBawah,xAkhir,yAkhir)
            prio.append([f_nBawah,xBawah,yBawah])

        if (maze[xAwalBaru + 1][yAwalBaru] == 0) :#petak kanan
            xKanan = xAwalBaru + 1
            yKanan = yAwalBaru
            parent.append([xAwalBaru,yAwalBaru,xKanan,yKanan])
            f_nKanan = f_n(parent,xAwal,yAwal,xKanan,yKanan,xAkhir,yAkhir)
            prio.append([f_nKanan,xKanan,yKanan])

        if (maze[xAwalBaru - 1][yAwalBaru] == 0) :#petak kiri
            xKiri = xAwalBaru - 1
            yKiri = yAwalBaru
            parent.append([xAwalBaru,yAwalBaru,xKiri,yKiri])
            f_nKiri = f_n(parent,xAwal,yAwal,xKiri,yKiri,xAkhir,yAkhir)
            prio.append(f_nKiri,xKiri,yKiri)
        
        prio.sort(key=takef_n) #sorting dengan key f_n yang berada di elem[0]

        xAwalBaru = prio[0][1] 
        yAwalBaru = prio[0][2]
    
    printJalur = [] 
    xt = xAkhir
    yt = yAkhir
    i = 0
    found = False
    while (xt != xAwal and yt != yAwal) :
        while (not(found)) :
            if (parent[i][2] == xt and parent[i][3] == yt) :
                found = True
                printJalur.append([xt,yt])
                xt = parent[i][0] #x parent
                yt = parent[i][1] #y parent
    printJalur.append([xAwal,yAwal]) #masih terurut dari titik akhir ke titik awal
    printJalur.reverse() #sudah terurut dari titik awal ke titik akhir

    xt = xAwal
    yt = yAwal
    while (xt != xAkhir and yt != yAkhir) : #membentuk track
        maze[xt][yt] = "="
    maze[xAkhir][yAkhir] = "="