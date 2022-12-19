def matrice():
    matrice = [[0]*n for m in range(n)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i<j: # sunt deasupra diagonalei principale
                sdp = sdp + matrice[i][j]
            if i+j<n-1: # sunt deasupra diagonalei secundare
                sds = sds + matrice[i][j]
    print(sdp)
    print(sds)


def matrice2():
    matrice2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for element in matrice2:
        print(element)
    for element in matrice2:
        print(1*1, 2*2, 3*3, 4*4, 5*5, 6*6, 7*7, 8*8, 9*9)


if __name__ == "__main__":
    matrice2()


