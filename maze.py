import sys
import aStar as ast
import bfs as bfs
import copy

def main():
    mat = [[]]
    xawal, yawal = map(int, input("Masukkan point awal maze (format= x <spasi> y): ").split())
    xakhir, yakhir = map(int, input("Masukkan point akhir maze (format= x <spasi> y): ").split())

    with open(sys.argv[1],"r") as f: #membaca nama file sebagai argumen program
        mat = [[int(num) for num in line if num!="\n"] for line in f]
    f.close()
    mazemat = copy.deepcopy(mat)

    bfs.out(mat)
    print()
    sol = bfs.bfs(xawal,yawal,xakhir,yakhir,mat)
    if (sol):
        print("BFS menemukan jalur keluar")
    else:
        print("Tidak ditemukan jalur keluar")
    bfs.out(mat)
    print("\nini astar\n")
    ast.aStar(mazemat,xawal,yawal,xakhir,yakhir)

if __name__ == "__main__":
    main()