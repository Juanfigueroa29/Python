def printintro():
    '''
    firma:
        recibe -- retorna
        () ->()

    sinopsis:
        la función imprime el mensaje de ahorcado en pantalla

    entradas y salidas:

    '''
    a= open("intro.txt")
    b= a.read()
    print(b)

def inputsecret():
    '''
    firma:
        ()->(string)
    sinopsis:
        la función le pide al usuario una palabra secreta y la retorna
    entradas y salidas:
    entradas: ninguna
    salidas: c: string con la palabra ingresada por el usuario
    '''
    c= input("Ingrese la palabra: ")
    return c

def loadwords():
    '''
    firma:
        ()-> (string)
    sinopsis:
        la función lee un documento y retorna un string con las palabras contenidas en este
    entradas y salidas:
    entradas: ninguna
    salidas: f: string con las palabras de un documento
    '''
    d= open("superheroes.txt")
    f=d.read()
    return f

def pickwords():
    '''
    firma:
        ()-> (string)
    sinopsis:
        la función lee un documento y retorna un string con una palabra del documento seleccionada aleatoriamente
    entradas y salidas:
    entradas: ninguna
    salidas: c: string con la palabra aleatoria
    '''
    from random import randint
    palabras=open("superheroes.txt")
    a = palabras.read()
    super=a.split(",")
    b=(randint(0,len(super)-1))
    c=super[b]
    return c

def modojuego(a):
    '''
    firma:
        (entero)-> (string)
    sinopsis:
        la función recibe un entero para escoger el modo de juego y retorna un string con la palabra secreta
    entradas y salidas:
    entradas: entero
    salidas: palabra: string con la palabra secreta
    '''
    if a == 1:
        palabra=inputsecret()
        return palabra
    else:
        palabra=pickwords()
        return palabra

def letrasdisponibles(x):
    '''
        firma:
            (string)-> (string)
        sinopsis:
            la función recibe un string con las letras ya ingresadas por el usuario y retorna un string con las letras que el usuario no ha ingresado
        entradas y salidas:
        entradas: string
        salidas: nueva: string con las letras que el usuario tiene disponibles para intentar
        '''
    nueva=""
    letras=["abcdefghijklmnopqrstuvwxyz"]
    for i in letras:
        if i not in x:
            nueva+=i
    return nueva

def guiones(palabrasecreta,letrasintentadas):
    '''
        firma:
            (string, string)-> (string)
        sinopsis:
            la función recibe un string con la palabra secreta y las letras intentadas, y retorna un string con los guiones para iniciar el juego
        entradas y salidas:
        entradas: strings
        salidas: a: string con los guiones y las letras que estan en la palabra
        '''
    a=""
    for i in palabrasecreta:
        if i in letrasintentadas:
            a+=i
        elif i==" ":
            a += i
        else:
            a+="_"
        a+=" "
    return a

def ganaste(palabrasecreta,letrasintentadas):
    '''
        firma:
            (string, string)-> (bool)
        sinopsis:
            la función recibe un string con la palabra secreta y las letras intentadas, y retorna un bool para verificar si con las letras intentadas se puede armar la palabra
        entradas y salidas:
        entradas: strings
        salidas: ban: bool
        '''
    ban=True
    for i in palabrasecreta:
        if i not in letrasintentadas:
            if i != ' ':
                ban=False
    return ban

def figura(n):
    '''
        firma:
            (entero)-> ()
        sinopsis:
            la función imprime el muñequito del ahorcado
        entradas y salidas:
        entradas: entero
        salidas:
        '''
    ban=False
    n1=str(n)
    a=open("figure.txt")
    for line in a:
        line = line[:-1]
        if line==n1:
            ban=True
        if line==str(n-1):
            ban=False

        if ban:
            print(line[1:])

def comprobarmodo():
    '''
        firma:
            ()-> (entero)
        sinopsis:
            la función se encarga de comprobar que el usuario ingrese el número correcto para escoger el modo de juego
        entradas y salidas:
        entradas:
        salidas: a: entero con el modo de juego
        '''
    while True:
        print("Seleccione el modo de juego:")
        print("1: si quiere ingresar una palabra")
        print("2: si quiere que el programa le de una")
        print("NOTA: RECUERDE USAR SOLO LETRAS MINUSCULAS")
        a=int(input("Ingrese opcion de juego: "))
        if a==1 or a==2:
             break
        else:
            print("Opción ingresada no válida")
    return a
