def adunare2():
    print("Introduceti va rog un numar de doua cifre:")
    a = int(input())
    z = a // 10
    u = a % 10
    print("Numarul rezultat prin adunarea zecilor si a unitatilor este:", z+u)


def adunare3():
        print("Introduceti va rog un numar de trei cifre:")
        a = int(input())
        s = a // 100
        z = a // 10 % 10
        u = a % 10
        print("Numarul rezultat prin adunarea sutelor, zecilor si a unitatilor este:", s + z + u)


def capetesipicioare():
    print("Introduceti va rog numarul de oi:")
    o = int(input())
    print("Introduceti va rog numarul de gaini:")
    g=int(input())
    print("Numarul de capete este:", g+o, ",iar numarul de picioare este:", 2*g+4*o)


def eliminare():
        print("Introduceti va rog un numar de trei cifre:")
        a = int(input())
        s = a // 100
        z = a // 10 % 10
        u = a % 10
        print("Numarul rezultat prin eliminarea cifrei zecilor este:", s*10+u)

def sumagauss():
    print("Introduceti un numar natural n:")
    n = int(input())
    print("Suma lui Gauss este:", n*(n+1)/2)


def ora():
    print("Introduceti ora:")
    h=int(input())
    print("Introduceti minutele")
    m=int(input())
    print("Introduceti numarul de minute care se vor aduna la ora si minutele introduse anterior:")
    x=int(input())
    ov = h*60+m+x
    print("Ora va fi", ov//60)


if __name__ == "__main__":
        sumagauss()
