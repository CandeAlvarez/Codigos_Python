#                   Juego de lógica
# Objetivo: Adivinar un número desconocido de N dígitos distintos.
# El valor N es ingresado por el usuario, debe estar en el rango [2,9]
# El número ingresado se compara con el generado. Luego, se indica la 
# cantidad de dígitos que cumplen las siguientes condiciones:
#   a) Perfecto: dígito correcto en la posicipon correcta
#   b) Bien: dígito correcto pero en posición incorrecta
#   c) Mal: dígito incorrecto, no pertenece a la solución


import random

digitos = [0,1,2,3,4,5,6,7,8,9]
intentos = 0
juego_finalizado = False


#Se repite el ingreso de cantidad de dígitos mientras el valor no
#sea numérico o bien no esté en el rango [2,9]
while True:
    try:
        cant_digitos = int(input("Ingrese la cantidad de dígitos (entre 2 y 9): "))
        if cant_digitos in range(2,10):
            #Genera el número a adivinar sin repetir dígitos
            lista_numero_adivinar = random.sample(digitos,cant_digitos)
            #Se almacena el resultado como un string para printf
            numero_adivinar = ''.join([str(e) for e in lista_numero_adivinar])
            break
    except ValueError:
        print("El valor ingresado no es numérico, intente nuevamente")

print("\n---------------------------------------------\n")

while (not juego_finalizado):
    #Obtiene la lista de la predicción del usuario
    lista_numero_ingresado = list(map(int, str(input("Predicción: "))))
    
    #Si la longitud de la lista coincide con los dígitos, se analiza
    if (len(lista_numero_ingresado)==cant_digitos):
        intentos = intentos+1       
        #Si las listas son iguales, el usuario adivinó el número
        if (lista_numero_ingresado == lista_numero_adivinar) :
            juego_finalizado = True
            print("Felicitaciones! Adivinó el número",numero_adivinar,"en",str(intentos),"intentos")
        else:
            cant_bien = 0
            cant_mal = 0
            cant_perfecto = 0
            for e in range(0,cant_digitos):
                #Si coincide el valor y la posición es un dígito perfecto
                if (lista_numero_adivinar[e]==lista_numero_ingresado[e]):
                    cant_perfecto = cant_perfecto + 1
                else:
                    #Si no es perfecto pero se encuentra en la lista del
                    #número a adivinar, es un digito bien
                    if(lista_numero_ingresado[e] in lista_numero_adivinar):
                        cant_bien = cant_bien+1
                    #Si no es perfecto ni bien, es mal
                    else:
                        cant_mal = cant_mal+1
            #Se imprime sobre la misma línea
            print("\033[A\t\t\tB =",str(cant_bien),"  M =",str(cant_mal),"  P =",str(cant_perfecto))
            
        
