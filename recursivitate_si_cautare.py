def cautaresir(sirprincipal, subsir):
    i = 0 # indice pentru parcurgerea sirului principal
    n = len(sirprincipal)-len(subsir) # cat de mult din sirul principal are sens sa parcurg
    while i <=n:
        j = 0
        flg = True
        while flg and j<len(subsir): # verific daca subsirul meu il gasesc in sirul principal
            if sirprincipal[i+j]!=subsir[j]:
                flg = False
            j = j + 1
        # daca din while ul precedent s-a iesit cu flg == True inseamna ca e posibil ca subsirul sa fi fost gasit
        # daca j == lungimea subsirului meu atunci sigur am gasit potrivirea si pot iesi din functie
        if flg and j ==len(subsir):
            return i
        # ma mut in sirul principal cu valoarea lui j pt care nu am gasit potrivire
        i = i + j
    return -1


# doresc o functie care aduna numerele naturale pana la n
# 1
def adunare(n):
    s = 0
    i = 1
    while i<=n:
        s=s+i
        i= i+1
    return s


def adunarerec(n): # adunarerec(5) = 5 + adunarerec(4)
                        #adunarerec(4) = 4 + adunarerec(3) ...
    if n<=1:
        return 1
    else:
        return n + adunarerec(n-1)


def factrec(n):
    if n <= 1:
        return 1
    else:
        return n * factrec(n-1)


def fib(n): # al n-lea termen in sirul lui fibonacci
    s = 0
    i = 0
    while i<n:
        if i == 0:
            t1 = 0
        else:
            t1 = t2
        if i ==1:
            t2 = 1
        else:
            t2 = s
        s = t1 + t2
        i = i+1
    return s


def fibrec(n):
    if n<0:
        return 0
    if n==0:
        return 0
    if n==1:
        return 1
    return fibrec(n-1) + fibrec(n-2)


def nr_cifre(n):
    c = 0
    if str(n)[len(str(n))-1]=='0':
        c = 1
    if len(str(n))-1 <0:
        return c
    return c + nr_cifre(int(str(n)))


if __name__ == "__main__":
    print(fibrec(15))
