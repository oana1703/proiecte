def lista():
    l = list()
    l.append(100)
    l.append(10)
    l.append(200)
    l.append(23)
    l.append(134)
    l.append(50)
    l.append(40)
    l = [100, 10, 200, 23, 134, 50, 40]
    # varianta 1 de tiparire elemente lista
    print("v1")
    for index in range(len(l)):
        print(l[index], end=",")
    # varianta 2
    print("")
    print("v2")
    for element in l:
        print(element, end=",")
    print("")
    print(l)
    l.append(210)
    print(l)
    l.append(70)
    print(l)
    l.pop()
    print(l)
    l.pop(0)
    print(l)
    l.pop(len(l)//2)
    print(l)

def exemplu_deque():
    l1 = []
    from collections import deque
    l2 = deque()
    l2.append(100)
    l2.append(10)
    l2.append(200)
    l2.append(23)
    l2.append(134)
    l2.append(50)
    l2.append(40)
    print(type(l1))

def matrice():
    matrice = []
    nr_coloane = 3
    nr_randuri = 3
    for i in range(nr_randuri): # pentru fiecare rand
        coloane_matrice = []
        for j in range(nr_coloane): # preiau coloanele matricei mele
            print(i, ",",j,end="=")
            coloane_matrice.append(input()) # input de la tastatura
        matrice.append(coloane_matrice)
    print(matrice)
    # tiparire matrice
    for i in range(nr_randuri): # pentru fiecare rand
        for j in range(nr_coloane): # preiau coloanele matricei mele
            print("(",i,",",j,"=", matrice[i][j], end=") ")
        print("|" , end="")
        print("")


if __name__ == "__main__":
    lista()