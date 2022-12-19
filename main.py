# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sumanumere():
    # Use a breakpoint in the code line below to debug your script.
    print('Introduceti primul numar,a ')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar,b')
    b = input()
    print('Numarul introdus b=', b)
    print('a+b=', int(a) + int(b))
    # Press Ctrl+F8 to toggle the breakpoint.


def diferentanumere():
    # Use a breakpoint in the code line below to debug your script.
    print('Introduceti primul numar,a ')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar,b')
    b = input()
    print('Numarul introdus b=', b)
    print('a-b=', int(a) - int(b))


def inmultirenumere():
    # Use a breakpoint in the code line below to debug your script.
    print('Introduceti primul numar,a ')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar,b')
    b = input()
    print('Numarul introdus b=', b)
    print('a*b=', int(a) * int(b))


def impartirenumere():
    # Use a breakpoint in the code line below to debug your script.
    print('Introduceti primul numar,a ')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar,b')
    b = input()
    print('Numarul introdus b=', b)
    print('a/b=', int(a) / int(b))


def ariatriunghiului():
    print('Introduceti prima cateta, c1')
    c1 = input()
    print('Prima cateta c1=', c1)
    print('Introduceti a doua cateta, c2')
    c2= input()
    print('Cea de-a doua cateta c2=', c2)
    print('Aria triunghiului =', int(c1)*int(c2)/2)


def perimetrultriunghiului():
    print('Introduceti prima latura,ab ')
    ab = input()
    print('Prima latura ab=', ab)
    print('Introduceti a doua latura,bc')
    bc = input()
    print('A doua latura bc=', bc)
    print('Introduceti a treia latura, ac')
    ac = input()
    print('A treia latura ac=', ac)
    print('Perimetrul triunghiului =', int(ab)+int(bc)+int(ac))

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    sumanumere()
    diferentanumere()
    inmultirenumere()
    impartirenumere()
    perimetrultriunghiului()
    ariatriunghiului()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
