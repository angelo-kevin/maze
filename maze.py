import sys
import aStar as ast
import bfs as bfs
import copy

def main():
    try:
        with open(sys.argv[1],"r") as f: #membaca nama file sebagai argumen program
            mat = [[int(num) for num in line if num!="\n"] for line in f]
        f.close()
        xawal, yawal = map(int, input("Masukkan point awal maze (format= x <spasi> y): ").split())
        xakhir, yakhir = map(int, input("Masukkan point akhir maze (format= x <spasi> y): ").split())
        mazemat = copy.deepcopy(mat)

        print("\nMatriks yang diinput: ")
        bfs.out(mat)
        print("\n\nDengan BFS: ")
        bobot = bfs.bfs(xawal,yawal,xakhir,yakhir,mat)
        bfs.out(mat)
        print("\nJalur yang ditempuh: ")
        bfs.jalur(bobot,xawal,yawal,xakhir,yakhir,mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if (mat[i][j]==8):
                    print(0, end=" ")
                elif (mat[i][j]==5):
                    print(" ", end=" ")
                else:
                    print(mat[i][j], end=" ")
            print()
        print("\nAda sebanyak",bfs.jumlah(mat),"langkah")

        print("\n\nDengan A*: ")
        ast.aStar(mazemat,xawal,yawal,xakhir,yakhir)
    except IndexError:
        print("Tidak ditemukan jalur yang tepat\nStarting point ataupun ending point salah")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()