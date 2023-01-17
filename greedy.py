def spectacol(lista): # lista mea va fi de forma [ [1,8] , [8,12], [8,10]...]
    lista = sorted(lista, key = lambda el: el[1])
    final = [lista[0]]
    ultimaora = lista[0][1]
    for el in specs:
        if el[0]>=ultimaora:
            ultimaora = el[1]
            final.append(el)
    print("numar spectacole:", len(final))



if __name__=="__main__":
    specs = list()
    n = int(input("Numar spectacole:"))
    for i in range(n):
        oi = int(input("Ora in."))
        os = int(input("Ora sf."))
        specs.append([oi, os])
    specs = [[1,8], [8,10], [8,12], [12,13], [15,17], [18,20], [17,21]]
    spectacol(specs)
