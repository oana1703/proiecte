sm = 0

def adunaremetoda(*args):
    global sm
    for a in args:
        sm += a


def adunare(*a):
    s = 0
    for element in a:
        s = s + element
    return s


def adunare2lista(lista):
    listanoua =list()
    for i in range(len(lista)):
        listanoua.append(lista[i]+2)
    return listanoua


def inmultire2lista(lista):
    listanoua =list()
    for i in range(len(lista)):
        listanoua.append(lista[i]*2)
    return listanoua

def oglindit(n):
    return int(str(n)[::-1])

def adunarelista(lista, s=0):
    for i in range(len(lista)):
        s += lista[i]
    return s


def VerificarePrime(numar):
    if numar == 2:
        return True
    if numar < 2:
        return False
    if numar % 2 == 0:
        return False
    for divizor in range(3, numar//2):
        if numar % divizor == 0:
            return False
    return True


def nr_prim(numar):
    gasit = 0
    while gasit == 0:
        numar = numar + 1
        if VerificarePrime(numar):
            gasit = 1
    return numar


def meniu3(opt):
    if opt == 1:
        return "adunare"
    elif opt == 2:
        return "scadere"
    elif opt == 3:
        return "inmultire"
    else:
        return "operatie nedefinita"


def nr_cifre(n):
    sir = str(n)
    contor = 0
    for caracter in sir:
        if caracter == "0":
            contor += 1
    return contor


def produsul(*args):
    p = 1
    for a in args:
        p = p * a
    return p


def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f


if __name__ == "__main__":
    # adunaremetoda(1,2,4,5)
    # print(sm)
    # print(adunare(1,2,4,5))
    # print(adunare2lista([1, 2, 3, 4]))
    # print(oglindit(123456))
    s1 = 10
    print(adunarelista([1, 2, 3, 4], s1))