#¿Qué información debe proporcionar la resolución del problema?
#·         Recibir las dimensiones de la superficie donde se utilizará el hormigón.
#·         Calcular la cantidad de metros cúbicos requeridos de hormigón.
#·         Manejar diferentes unidades de medida, como metros, pies, centímetros, etc., para adaptarse a las preferencias de los clientes.
#·         Imprimir un archivo para entregárselo al cliente con los datos ofrecidos, el cálculo realizado y el total de metros de hormigón que le serán entregado.
#¿Qué datos se necesitan para resolver el problema? Si los tengo ¿Cuáles son?
#·         Dimensiones de la superficie, no las tengo, debo pedirlas.
#·         Calcular los metros cúbicos de hormigón, tengo la formula, longitud * altura * espesor.
#·         Unidades de medidas, las tengo, metros, centímetros, pies, etc.
#¿Qué pasos debo realizar para llegar a la solución del problema?
#·         Escribir las dimensiones sobre las cuales se va a utilizar el hormigón.
#·         Escribir la fórmula para realizar el cálculo de los metros cúbicos.
#·         Escribir las unidades de medidas que vamos a utilizar para llevar a cabo el cálculo.
#Diseño del algoritmo:
#  Pedir los datos de la superficie donde se utilizará el hormigón
#Aplicar la fórmula para el cálculo requerido
#Escribir los resultados más detalles importantes
#Registrar el pedido del cliente (detalles cliente y metros solicitados)

#######################################################################################################################

import os
unidad_a_utilizar = 0
numero_cliente = ""
ciclo = 1
nombre= str
                             #limpiar consola al finalizar/iniciar la secuencia
while ciclo != 0:

    os.system("cls")
#######################################################################################################################

    numero_cliente = ""                            #reinicio numero de cliente

#######################################################################################################################

    nombre= input("Ingrese su nombre porfavor: ")



    while len(numero_cliente) != 8:
        numero_cliente=input("ingrese su DNI: ")                         #Verifica que el dni
        if len(numero_cliente) < 8 or len(numero_cliente) > 8:
            print("El numero ingresado no concuerda con un documento, vuelva a intentarlo")
        try:
            int(numero_cliente)
        except ValueError:                                                #verifica que sean numeros
            print("los caracteres son incorrectos, ingrese exclusivamente numeros")
            numero_cliente = str(numero_cliente) + " "

        
############################################################################################################

    print("=" * 90)
    print(f"BIENVENDIDO/A {nombre}, ¿QUE UNIDAD DE MEDIDA VA A UTILIZAR?: ")
    print("1 - METROS")
    print("2 - CENTÍMETROS")                                               #pedido de parametros inciales
    print("3 - PIES")

############################################################################################################

    while unidad_a_utilizar < 1 or unidad_a_utilizar > 3:
        try:
            unidad_a_utilizar = int(input("Por favor ingrese el numero correspondiente para continuar: "))  #validador de datos (parametros iniciales)
        except ValueError:
            print("LO SIENTO, INGRESE EL VALOR CORRESPONDIENTE A LA UNIDAD DE MEDIDA (1, 2 o 3), GRACIAS.")

#######################################################################################################################

    print("MUCHAS GRACIAS, CONTINUEMOS: ")
    dato_anch= 0
    dato_long= 0
    dato_alt= 0

    while dato_long <= 0 or dato_anch <= 0 or dato_alt <= 0:
        try:
            dato_long = float(input("Ingrese la longuitud de la superficie donde utilizara el concreto: "))
            dato_anch = float(input("Ingrese el ancho de la superficie donde ultilizara el concreto: "))      #pedido de datos para la resolucion de la incognita
            dato_alt = float(input("Ingrese la altura de la superficie donde utilizara el concretro: "))
            if dato_long <= 0 or dato_anch <= 0 or dato_alt <= 0:
                print("POR FAVOR INGRESE CORRECTAMENTE LOS VALORES")            #validacion de parametros
                print("NO SE PUEDE CALCULAR CON VALORES EN '0'")
        except ValueError:
            print ("Ingrese un valor correcto")
        else:
            break

#######################################################################################################################

    print("=" * 90) #printea dibujitos para entender mejor la consola

#######################################################################################################################


    if unidad_a_utilizar == 2:                     #conversor centimetro a metro
        dato_long /= 100
        dato_anch /= 100
        dato_alt /= 100

#######################################################################################################################

    elif unidad_a_utilizar == 3:                   #conversor pie a metro
        dato_long *= 0,3048
        dato_anch *= 0,3048
        dato_alt *= 0,3048

#######################################################################################################################

    metros_Cubicos = dato_long * dato_anch * dato_alt

    print(f"Usted va a trabajar en una superficie de {metros_Cubicos} metros cubicos.")      #escribo la resolucion del problema,
    print("="*90)                                                                            #en metros cubicos y con la cantidad de materiales
    print("Usted necesitara la siguiente cantidad de materiales: ")


    volumen_total_concreto = (metros_Cubicos*7)*1.05
    volumen_total_arena = metros_Cubicos*0.56
    volumen_total_grava = metros_Cubicos*0.84
    volumen_total_agua = metros_Cubicos*180

#######################################################################################################################

    print("=" * 90)

    print(f"BOLSAS DE CONCRETO: {volumen_total_concreto*100//10/10} bolsas de concreto.")
    print(f"ARENA: {volumen_total_arena*100//10/10} metros cubicos.")                       #escribe el ticket final al consumidor, expresando los datos
    print(f"GRAVA: {volumen_total_grava*100//10/10} metros cubicos.")                       #que fueron solicitados en la consigna del problema.
    print(f"AGUA: {volumen_total_agua} litros/metros cubicos.")

    print("=" * 90)

#######################################################################################################################

    ticket = open("tabla-" + str(numero_cliente) + ".txt", "w")
    ticket.write(str(f"BOLSAS DE CONCRETO: {volumen_total_concreto*100//10/10} bolsas de concreto.\n"))
    ticket.write(str(f"ARENA: {volumen_total_arena*100//10/10} metros cubicos.\n"))          #creación del ticket impreso que se dará al cliente
    ticket.write(str(f"GRAVA: {volumen_total_grava*100//10/10} metros cubicos.\n"))
    ticket.write(str(f"AGUA: {volumen_total_agua} litros/metros cubicos.\n"))
    ticket.close()

#######################################################################################################################

    base_data = open("BASE DE DATOS.txt", "a")
    base_data.write(str(f"El pedido del cliente n°"+ str(numero_cliente) + "a nombre de: " + str(nombre) + ".\n"))
    base_data.write(str(f"BOLSAS DE CONCRETO: {volumen_total_concreto * 100 // 10 / 10} bolsas de concreto.\n"))
    base_data.write(str(f"ARENA: {volumen_total_arena * 100 // 10 / 10} metros cubicos.\n"))  # creación del ticket impreso que se agregara a la base de datos de la empresa
    base_data.write(str(f"GRAVA: {volumen_total_grava * 100 // 10 / 10} metros cubicos.\n"))
    base_data.write(str(f"AGUA: {volumen_total_agua} litros/metros cubicos.\n"))
    base_data.close()

#######################################################################################################################

    while True:
        try:
            ciclo = int(input("¿Desea continuar con otro pedido? Si[1] No[0]: "))
            if ciclo > 1 or ciclo <0:
                print("Valor fuera de rango, intente nuevamente.")                          #bucle para pedir nuevo pedido o terminar el programa
            else:
                break
        except ValueError:
            print("Porfavor ingrese un numero para SI siendo 1 o NO siendo 0")

#######################################################################################################################