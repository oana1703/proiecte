def lista():
    lista = [1, 2, 3]
    for i in range(len(lista)):
        print(lista[i])


def abc():
    dic1 = { 'a':10, 'b':20, 'c':300}

    suma = 0
    cuvant = "abc"
    for i in range(len(cuvant)):
        suma+= dic1[cuvant[i]]
    print("suma este:", suma)


def crypt_hash():
    dict3crypt = { 'a': 'd', 'b':'e', 'c':'f', 'd':'g', 'e':'h', 'f':'i', 'g':'j', 'h':'k', 'i':'l', 'j':'m',
        'k':'n', 'l':'o', 'm':'p', 'n':'q', 'o':'r', 'p':'s', 'q':'t', 'r':'u', 's':'v',
        't':'w', 'u':'x', 'v':'y', 'w':'z', 'x':'a', 'y':'b', 'z':'c'}


    propozitie= input("Introduceti o propozitie:")
    rezultat =''
    for element in propozitie:
        if element in(' ', ',', '-', '?', '!', '1', '2', '3', '4'):
            rezultat += element
        else:
            rezultat += dict3crypt[element]
    return rezultat


    for element in dict3crypt.items():
        print(element)


def decrypt_hash(propozitie):
    dict3decrypt = {'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
                  'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v',
                  't': 'w', 'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c'}
    rezultat = ''
    for element in propozitie:
        if element in (' ', ',', '-', '?', '!', '1', '2', '3', '4'):
            rezultat += element
        else:
            rezultat += dict3decrypt[element]
    return rezultat


if __name__=="__main__":
    propozitie = input("Introduceti o propozitie:")
    c1 = crypt_hash(propozitie)
    print(c1)
    c2 = decrypt_hash(c1)
    print(c2)

