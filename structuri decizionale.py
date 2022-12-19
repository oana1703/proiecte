def sir5():
    print("Va rog introduceti un sir de numere naturale:")
    sir = input()
    contor = 0
    for index in range(0, len(sir)):
        if int(sir[index]) == 5:
            contor += 1
    print("contor=", contor)

def lista5():
    print("Va rog introduceti un sir de numere naturale despartite prin spatiu:")
    lista = input().split(" ")
    print(lista)
    contor = 0
    for index in range(0, len(lista)):
        if int(lista[index]) == 5:
            contor += 1
    print("contor=", contor)

def incadrare():
    print("Introduceti valoarea:")
    o = int(input())
    if o <= 3500:
        print("mic")
    else:
        if o <= 7000:
            print("mediu")
        else:
            if o >= 7000:
                print("mare")

def adunare():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a+b=", a+b)

def scadere():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a-b=", a-b)

def inmultire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a*b=", a * b)

def impartire():
    print("a=", end="")
    a = int(input())
    print("b=", end="")
    b = int(input())
    print("a/b=", a / b)

def meniu():
    print("Apasati tasta 1 pentru adunare, 2 pentru scadere, 3 pentru inmultire, 4 pentru impartire")
    o = input().strip()
    if o == "1":
        print("adunare")
        adunare()
    else:
        if o == "2":
            print("scadere")
            scadere()
        else:
            if o == "3":
                print("inmultire")
                inmultire()
            else:
                if o == "4":
                    print("impartire")
                    impartire()
                else:
                    print("Tastati doar 1,2,3,4")


if __name__ == "__main__":
    lista5()
