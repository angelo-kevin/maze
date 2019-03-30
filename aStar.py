def h_n(xSaatIni,ySaatIni,xAkhir,yAkhir) : #saatIni= titik tersebut, akhir= titik finish
    return abs(xSaatIni - xAkhir) + abs(ySaatIni - yAkhir) #manhattan distance

def g_n(parent,xAwal,yAwal,xSaatIni,ySaatIni) : #parent = list of parent, xAwal yAwal = titik masukan
    jumlah = 1
    if (not(isParentEmpty(parent))) :
        while (xSaatIni != xAwal and ySaatIni != yAwal) :
            found = False
            i = 0
            while (not(found) and i < len(parent)) :
                if (xSaatIni == parent[i][2] and ySaatIni == parent[i][3]) :
                    found = True
                    xSaatIni = parent[i][0]
                    ySaatIni = parent[i][1]
                    #print(xSaatIni)
                    #print(ySaatIni)
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
            

def aStar(maze,xAwal,yAwal,xAkhir,yAkhir) : #awal= titik awal, akhir= titik akhir
    prio = [] #list priority queue isinya [f_n, x, y]
    parent = [] #list of titik parent isinya [x parent, y parent, x child, y child]
    xAwalBaru = xAwal 
    yAwalBaru = yAwal
    while (not(ketemu(xAwalBaru,yAwalBaru,xAkhir,yAkhir))) :
        if (maze[xAwalBaru][yAwalBaru + 1] == 0 and not(cekParent(parent,xAwalBaru,yAwalBaru + 1))) :#petak atas
            xKanan = xAwalBaru
            yKanan = yAwalBaru + 1
            #print("masuk kanan")
            #print("untuk ",xKanan," ",yKanan)
            #print("nilai ",maze[xKanan][xKanan])
            parent.append([xAwalBaru,yAwalBaru,xKanan,yKanan])
            #print("panjang parent ",len(parent))
            f_nKanan = f_n(parent,xAwal,yAwal,xKanan,yKanan,xAkhir,yAkhir)
            #print("udah fn segini ", f_nBawah)
            prio.append([f_nKanan,xKanan,yKanan])

        if (yAwalBaru != 0) :
            if (maze[xAwalBaru][yAwalBaru - 1] == 0 and not(cekParent(parent,xAwalBaru,yAwalBaru - 1))) :#petak bawah
                xKiri = xAwalBaru
                yKiri = yAwalBaru - 1
                #print("masuk kiri")
                #print("untuk ",xKiri," ",yKiri) #ini kenapa maze[1][0] nilainya 0?
                #print("nilai ",maze[#xKiri][yKiri])
                parent.append([xAwalBaru,yAwalBaru,xKiri,yKiri])
                #print("panjang parent ",len(parent))
                f_nKiri = f_n(parent,xAwal,yAwal,xKiri,yKiri,xAkhir,yAkhir)
                #print("udah fn segini ", f_nAtas)
                prio.append([f_nKiri,xKiri,yKiri])

        if (maze[xAwalBaru + 1][yAwalBaru] == 0 and not(cekParent(parent,xAwalBaru + 1,yAwalBaru))) :#petak kanan
            #print("masuk bawah")
            xBawah = xAwalBaru + 1
            yBawah = yAwalBaru
            #print("untuk ",xBawah," ",yBawah)
            #print("nilai ",maze[xBawah][yBawah])
            parent.append([xAwalBaru,yAwalBaru,xBawah,yBawah])
            #print("panjang parent ",len(parent))
            f_nBawah = f_n(parent,xAwal,yAwal,xBawah,yBawah,xAkhir,yAkhir)
            #print("udah fn segini ", f_nKanan)
            prio.append([f_nBawah,xBawah,yBawah])

        if (xAwalBaru != 0) :
            if (maze[xAwalBaru - 1][yAwalBaru] == 0  and not(cekParent(parent,xAwalBaru - 1,yAwalBaru))) :#petak kiri
                #print("masuk atas")
                xAtas = xAwalBaru - 1
                yAtas = yAwalBaru
                #print("untuk ",xAtas," ",yAtas)
                #print("nilai ",maze[xAtas][yAtas])
                parent.append([xAwalBaru,yAwalBaru,xAtas,yAtas])
                #print("panjang parent ",len(parent))
                f_nAtas = f_n(parent,xAwal,yAwal,xAtas,yAtas,xAkhir,yAkhir)
                #print("udah fn segini ", f_nKiri)
                prio.append([f_nAtas,xAtas,yAtas])

        prio.sort(key=takef_n) #sorting dengan key f_n yang berada di elem[0]

        xAwalBaru = prio[0][1] #masalah
        yAwalBaru = prio[0][2]

        del prio[0]

    print("kelar nyari jalur")

    printJalur = [] 
    xt = xAwalBaru
    yt = yAwalBaru
    printJalur.append([xt,yt])
    print("mau mulai backtrack dari ", xAwalBaru, ",", yAwalBaru)
    while (not(ketemu(xt,yt,xAwal,yAwal))) :
        found = False
        idx = 0
        while (not(found)) :
            if (parent[idx][2] == xt and parent[idx][3] == yt) :
                found = True
                xt = parent[idx][0]
                yt = parent[idx][1]
                printJalur.append([xt,yt])
            else :
                idx = idx + 1
    
    print("kelar backtrack")
    printJalur.reverse() #sudah terurut dari titik awal ke titik akhir
    for i in printJalur :
        print(i)
    print("ada sebanyak ", len(printJalur), " langkah")
    #kurang gambarin