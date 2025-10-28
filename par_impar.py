def num_par(numero):
    if numero % 2 == 0:
        return "el numero es par"
    else :
        return "el numero NO es par"
    
salir = 0

while salir == 0 :
    numero = int(input("Ingresa un numero: "))
    validacion = num_par(numero)
    print (validacion)
    
    salir = int(input("Desea salir? Si = presiona cualquier tecla. No = presiona el numero 0: "))

print("Has salido del programa, gracias por utilizar nuestros servicios")

