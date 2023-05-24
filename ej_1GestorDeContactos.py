#Ejercicio 1:
#Gestor de Contactos Crea un programa que funcione como un gestor de contactos. El
#programa debe permitir al usuario almacenar nombres y números de teléfono en un
#diccionario, así como buscar, agregar y eliminar contactos. Debe mostrar un menú con las
#siguientes opciones:
#1. Agregar contacto
#2. Buscar contacto
#3. Eliminar contacto
#4. Mostrar todos los contactos
#5. Salir
#El programa debe ejecutarse hasta que el usuario elija la opción "Salir" del menú.

contactos_telefono = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre de la persona que desea agregar: ")
    telefono = input("Ingrese el teléfono de la persona que desea agregar: ")
    contactos_telefono[nombre] = telefono
    print("Contacto agregado con éxito.")

def buscar_contacto():
    nombreBuscado = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombreBuscado in contactos_telefono:
        telefonoEncontrado = contactos_telefono[nombreBuscado]
        print("La persona", nombreBuscado, "se encuentra en la lista y su teléfono es:", telefonoEncontrado)
    else:
        print("El contacto", nombreBuscado, "no se encuentra en la lista de contactos.")

def eliminar_contacto():
    eliminarNombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if eliminarNombre in contactos_telefono:
        del contactos_telefono[eliminarNombre]
        print("Contacto eliminado con éxito.")
    else:
        print("El contacto", eliminarNombre, "no se encuentra en la lista de contactos.")

def mostrar_contactos():
    if len(contactos_telefono) == 0:
        print("No hay contactos en la lista.")
    else:
        print("Lista de contactos:")
        for nombre, telefono in contactos_telefono.items():
            print(nombre + ":", telefono)


while True:
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        mostrar_contactos()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.")
