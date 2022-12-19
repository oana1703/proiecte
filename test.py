def suma_lista():
    l=[1, 2, 3, 4, 5, 6, 7]
    print("Calculati patratul numerelor introduse:")
    suma = int(input())
    for i in range(len(l)):
        if l[i] == suma:
            print("Afisati elementul:", suma)
            print("Afisati elementul la patrat:", suma**2)


def suma2():
    l=[1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    suma = 0
    for i in range(len(l)):
        if i  <= 3 or i <=7:
            s+= l[i]

if __name__ == "__main__":
    suma2()


if __name__ == "__main__":
    suma_lista()
