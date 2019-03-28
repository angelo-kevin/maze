import sys

def main():
    with open(sys.argv[1],"r") as f: #membaca nama file sebagai argumen program
        mat = [[int(num) for num in line if num!="\n"] for line in f]
    f.close()
    for i in range(len(mat)):
        print(mat[i])

if __name__ == "__main__":
    main()