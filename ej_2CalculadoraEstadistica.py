#Ejercicio2:
#Calculadora de Estadísticas de Números
#Escribe un programa que permita al usuario ingresar una lista de números y realice los
#siguientes cálculos estadísticos:
#1. Calcular la suma de los números.
#2. Calcular el promedio de los números.
#3. Encontrar el número mínimo y el número máximo de la lista.
#4. Calcular la desviación estándar de los números.
#El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
#luego imprimir los resultados de los cálculos estadísticos.

numeroUsuario =[]
def agregar_numeros():
    c=0
    while c!=10:    
        num = input("Ingrese 10 números que luego utilizaremos para realizar los calculos: ")
        num=(int(num))
        numeroUsuario.append(num)
        c=c+1
    print(numeroUsuario)


def calcular_suma():
    suma=0
    for num in numeroUsuario:
        suma=int(suma+num)
    print(f"La suma de los numeros ingresados es {suma}")




def encontrar_numeroMinMax():
    numMax=0
    numMin=0
    for num in numeroUsuario:
        if num > numMax:
            numMax=num
        if numMin == 0 or num < numMin:
            numMin=num
    print(f"El numero minimo es:  {numMin}")
    print(f"El numero maximo es:  {numMax}")

def promedioNum():
    suma=0
    c=0
    promedioNum=0
    for numero in numeroUsuario:
        suma=int(suma+numero)
        c=c+1
        promedioNum=(suma/c)
    print(f"El promedio de los numeros es: {promedioNum}")


while True:
    print("\n--- Calculadora ---")
    print("1. Agregar 10 numeros")
    print("2. Calcular la suma de los números")
    print("3. Encontrar numero maximo y minimo")
    print("4. Calcular el promedio de los numeros")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        agregar_numeros()
    elif opcion == "2":
        calcular_suma()
    elif opcion == "3":
        encontrar_numeroMinMax()
    elif opcion == "4":
        promedioNum()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.")
