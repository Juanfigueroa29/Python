from ahorcado import *
letrasintentadas=""
vidas=7
c='Si'
cont=0
while c=='Si' or c == "si" or c=="SI" or c == "sI":
    cont+=1
    printintro()
    a = comprobarmodo()
    palabrasecreta=modojuego(a)

    while True:
        figura(vidas)
        letras=letrasdisponibles(letrasintentadas)
        print("Las letras disponibles son: "+ letras)
        print("Te quedan {} vidas".format(vidas))
        print(guiones(palabrasecreta,letrasintentadas))
        while True:
            b=input("Ingrese una letra: ")
            if len(b)!=1:
                print("Entrada no válida")
            else:
                break

        if b in letrasintentadas:
            print("La letra ya fue ingresada")
        elif b in palabrasecreta:
            print("Acertaste")
            letrasintentadas+=b
        else:
            vidas-=1
            letrasintentadas+=b

        if vidas<=0:
            print("Se te acabaron las vidas, perdiste")
            print("La palabra secreta era:", palabrasecreta)
            break

        if ganaste(palabrasecreta, letrasintentadas):
            print('Has ganado')
            break
    c =input("¿Desea jugar de nuevo?: (Sí)/(No): ")
    letrasintentadas = ""
    vidas = 7

print("Jugaste ",cont,"veces")