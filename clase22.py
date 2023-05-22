'''
def contar_palabras(oracion):
    contador = {}
    palabras = oracion.split()
    for palabra in palabras: 
        if palabra in contador:
            contador[palabra]+=1
        else:
            contador[palabra] = 1
    return contador

oracion = input("Ingrese una oración: ")

resultado = contar_palabras(oracion)
print(resultado)
'''

def obtener_persona_mas_joven():
    num_personas = int(input("Ingrese el número de personas: "))
    
    datos = {}
    
    for i in range(num_personas):
        nombre = input("Ingrese el nombre de la persona " + str(i+1) + ": ")
        edad = int(input("Ingrese la edad de la persona " + str(i+1) + ": "))
        datos[nombre] = edad
    
    persona_mas_joven = None
    edad_mas_joven = None
    
    for nombre, edad in datos.items():
        if edad_mas_joven is None or edad < edad_mas_joven:
            edad_mas_joven = edad
            persona_mas_joven = nombre
    
    return persona_mas_joven

persona_joven = obtener_persona_mas_joven()
print("La persona más joven es: " + persona_joven)




