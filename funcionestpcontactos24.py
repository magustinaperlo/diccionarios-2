import funcionestpcontactos24
def menu_principal():
    print("---- MENU PRINCIPAL ----")
    print("1. Rectas paralela y perpendicular a una dada")
    print("2. Analisis de una funcion lineal")
    print("3. Analisis de una funcion cuadratica")
    print("4. Salir")
    opcion = input("Selecciona una opcion: ")
    return opcion

def menu_agregarContacto():
    print("---Menu agregar contacto ----")
    contactos_telefono={}
    msj=""
    c=0
    msj="Ingrese la cantidad de contactos a agregar"
    cantidad=input(int())
    while c<=cantidad:
            msj="Ingresa el nombre de la persona que desea agendar"
            print(msj)
            contactos_telefono["Nombre"] = (input(""))
            msj= "Ingresa el telefono de la persona que desea agendar"
            print(msj)
            contactos_telefono["Telefono"] =(input(""))
            c=c+1
            print(contactos_telefono)
            return contactos_telefono
    funcionestpcontactos24.menu_agregarContacto()
            
            
    
    print ("\nIngrese el termino independiente\n")
    b = fractions.Fraction(input(""))
    print("Rectas paralelas:")
    print("\nLa ecuacion es: " + "y = " + str(a) + "x " + " + " +  str(b))
    print ("\n")
    print ("A continuación verás tres paralelas a la ecuación dada y sus respectivas perpendiculares.\n")
    while (c < 3):
        d = random.randint(-1, 2)
        if (d != b and  d != di):
            if (d >= 0):
                print("\nParalela " + str(c+1) + "\n")
                msj = "" + "y = " +  str(a) + "x" + " + " + str(d)
                print (msj)
                print ("\nPerpendicular " + str(c+1))
                msj2 = "" + "y = " + "-" +  str(fractions.Fraction(1/a)) + "x" + " + " + str(d)
                print ("\n")
                print (msj2)
                c = c + 1
                di = d
            if (d < 0):
                print("\nParalela " + str(c+1) + "\n")
                msj = "" + "y = " +  str(a) + "x" + " + " + "(" + str(d) + ")"
                print (msj)
                print ("\nPerpendicular " + str(c+1))
                msj2 = "" + "y = " +  "(" + "-" + str(fractions.Fraction(1/a)) + ")" + "x" + " + " + "(" + str(d) + ")" + ""
                print ("\n")
                print (msj2)
                c = c + 1
                di = d
    volver_al_menu()

def menu_funcion_lineal():
    print("---- MENU DE FUNCION LINEAL ----")
    print ("\n")
    a1 = 0
    b2 = 0
    corte_x = 0

    print ("Ingrese el coeficiente principal (distinto de cero): \n")
    a1 = fractions.Fraction(input())
    if (a1 == 0):
        print ("El coeficiente principal tiene que ser distinto de cero")
        menu_funcion_lineal()
    print ("Ingrese el termino independiente: \n")
    b1 = fractions.Fraction(input())
    corte_x = fractions.Fraction(-1 * a1 / b1)
    print ("El corte con el eje x es igual a: " + str(fractions.Fraction(corte_x)))
    print ("\nEl corte con el eje y es igual a: " + str(b1))
    if (b1 > 0):
        print ("\nLa recta es creciente")
    else:
        print("\nLa recta es decreciente")
    volver_al_menu()

def menu_funcion_cuadratica():
    print("---- MENU DE FUNCION CUADRATICA ----\n")
    print ("Ingrese el coeficiente principal (que sea distinto de cero): \n")
    aj = fractions.Fraction(input())
    if (aj == 0):
        print ("El valor del coeficiente principal tiene que ser distinto de cero. Ingrese de nuevo el valor: ")
        menu_funcion_cuadratica()  
    
    print ("Ingrese el coeficiente lineal: \n")
    bj = fractions.Fraction(input())
    print ("Ingrese el termino independiente: \n")
    cj = fractions.Fraction(input())
    dj = fractions.Fraction((-bj**2) - (4*aj*cj))

    if (dj < 0):
        print ("La ecuación cuadrática tiene raíces complejas")
    elif (dj == 0):
        print ("La ecuación tiene una raíz doble: ")
        discrim = fractions.Fraction(-bj / (2*aj))
        print ("x = " + str(fractions.Fraction(discrim)))
    else:
        discrim = dj**0.5
        print ("La ecuación cuadratica tiene dos soluciones: ")
        rootOne = (fractions.Fraction(-bj + discrim) / (2*aj))
        print ("x1 = " + str(rootOne))
        rootTwo = (fractions.Fraction(-bj - discrim) / (2*aj))
        print ("x2 = " + str(rootTwo))

        print ("El punto de corte con el eje y: " + str(cj))

    x_vertice = fractions.Fraction(-bj / (2*aj))
    y_vertice = fractions.Fraction((x_vertice**2 * aj) + (x_vertice*bj) + cj)
    print ("La coordenada del vertice es: (" + str(x_vertice) + ", " + str(y_vertice) + ")")
    

    if (aj > 0):
        #conArriba = aj
        print ("La parabola es concava hacia arriba")
    elif (aj < 0):
        #conAbajo = aj 
        print ("La parabola es concava hacia abajo")
    volver_al_menu()

def volver_al_menu():
    input("Presiona ENTER para volver al menu principal...")
    mostrar_menu_principal()

def mostrar_menu_principal():
    opcion = ''
    while opcion == '4':
        print ("Hasta la vista baby")
        break
