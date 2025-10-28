def comparacion(a, b):
    if a > b:
        return "El mayor es: ", a
    elif b > a:
        return "El mayor es: ", b

salir = False

while salir == False:
    print("bienvenido al comparador de numeros")

    a = int(input("ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    resultado = comparacion(a, b)
    print(resultado)

    print("Desea comparar mas numeros? ingrese 1 si sí, 2 si desea finalizar")
    desicion = int(input())

    if desicion == 1:
        salir == False
    else:
        salir == True