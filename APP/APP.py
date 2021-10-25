# TITULO


def printintro():
    a= open("intro.txt")
    b= a.read()
    print(b)



# ======================= FUNCION VERIFICAR COMPRA ==========================
def compraexitosa():
    comprarsi = input("COMPRAR (SI/NO): ")
    # SI EL USARIO MARCA (SI) SE EFECTUA LA COMPRA
    if comprarsi == "SI" or comprarsi == "Si" or comprarsi == "si":
        print ("")
        print ("SU COMPRA HA SIDO EXITOSA")
    # DE LO CONTRARIO IMPRIME "COMPRA CANCELADA"
    else:
        print ("")
        print ("COMPRA CANCELADA")
# ======================= FUNCION COMPRA ==========================
def comprar ():
    objeto = input("ESCOGA OBJETO A COMPRAR (1/2/3): ")# USUARIO ESCOGE ENTRE LOS 3 PRODUCTOS DEFINIDOS COMO 1, 2 Y 3
    print ("")
    # POR CADA OPCION IMPRIME EL TOTAL Y LLAMAMOS A LA FUNCION (COMPRAEXITOSA) PARA VERIFICAR LA COMPRA

    if objeto in OP:
        print ("TOTAL:", OP[objeto])
        print ("")

#===================================================================

# INICIAMOS EL CICLO PREGUNTANDO SI DESA COMPRAR O NO
printintro()

comenzar = input("INGRESE SI DESEA COMPRAR (SI/NO): ")
print ("")

while True: # LA SENTENCIA TRUE PERMITE QUE EL CICLO SIEMPRE SE CUMPLA


    if comenzar == "SI" or comenzar == "Si" or comenzar == "si": #SI LA OPCION ES (SI) COMIENZA LA APP

        # IMPRIMIMOS CATEGORIAS

        print ("A CONTINUACION SELECCIONE UNA CATEGORIA DE PRODUCTO")

        # DEFINIMOS LAS CATEGORIAS COMO (1/2/3) O POR SU NOMBRE RESPECTIVO

        print ("1 - Tecnologia")
        print ("2 - Calzado")
        print ("3 - Ropa")
        print ("")

        # PEDIMOS CATEGORIA A COMPRAR

        categoria = input("INGRESE CATEGORIA: ")
        print ("")
   # ============================================================================

        # 1 ES IGUAL A LA OPCION TECNOLOGIA
        if categoria == "1" or categoria == "Tecnologia" or categoria == "tecnologia" or categoria == "TECNOLOGIA":

            # DEFINIMOS CADA OPCION DE PRODUCTO COMO: OP1, OP2, OP3 Y SUS RESPECTIVOS VALORES
            OP = {'1': 500000, '2': 950000, '3': 2000000}



            # IMPRIMIMOS PRODUCTOS

            print ("         TECNOLOGIA      ")
            print ("OBJETO   ----------    VALOR")
            print ("")
            print ("1 - TV       ----------   $500.000")
            print ("2 - CELULAR  ----------   $950.000")
            print ("3 - PC       ----------   $1.500.000")

            # LLAMAMOS A LA FUNCION COMPRAR

            comprar()

            # AL FINAL VOLVEMOS A PREGUNTAR SI EL USUARIO QUIERE SEGUIR COMPRANDO

            comenzar = input("SEGUIR COMPRANDO (SI/NO): ")


            # 2 ES IGUAL A LA OPCION CALZADO
        elif categoria == "2" or categoria == "Calzado" or categoria == "calzado" or categoria == "CALZADO":

                # DEFINIMOS CADA OPCION DE PRODUCTO COMO: OP1, OP2, OP3 Y SUS RESPECTIVOS VALORES
                OP = {'1': 100000, '2': 150000, '3': 200000}



                # IMPRIMIMOS PRODUCTOS

                print ("          CALZADO      ")
                print ("OBJETO   ----------    VALOR")
                print ("")
                print ("1 - ZAPATO 1  ----------   $100.000")
                print ("2 - ZAPATO 2  ----------   $150.000")
                print ("3 - ZAPATO 3  ----------   $200.000")

                # LLAMAMOS A LA FUNCION COMPRAR

                comprar()

                # AL FINAL VOLVEMOS A PREGUNTAR SI EL USUARIO QUIERE SEGUIR COMPRANDO

                comenzar = input("SEGUIR COMPRANDO (SI/NO): ")
        else:
            # 3 ES IGUAL A LA OPCION ROPA

            if categoria == "3" or categoria == "Ropa" or categoria == "ropa" or categoria == "ROPA":

                # DEFINIMOS CADA OPCION DE PRODUCTO COMO: OP1, OP2, OP3 Y SUS RESPECTIVOS VALORES
                OP = {'1': 45000, '2': 100000, '3': 80000}



                print ("            ROPA      ")
                print ("OBJETO   ----------    VALOR")
                print ("")
                print ("1 - SUETER    ----------   $45.000")
                print ("2 - CHAQUETA  ----------   $100.000")
                print ("3 - JEAN      ----------   $80.000")

                #LLAMAMOS A LA FUNCION COMPRAR

                comprar()

                # AL FINAL VOLVEMOS A PREGUNTAR SI EL USUARIO QUIERE SEGUIR COMPRANDO

                comenzar = input("SEGUIR COMPRANDO (SI/NO): ")


    else: #SI LA OPCION ES (NO) LA APP NO CORRE
        if comenzar == "NO" or comenzar == "No" or comenzar == "no":
            print ("")
            print ("GRACIAS POR VISITAR APP CORONAVIRUS")
            break