"""
Gestor de Contactos Crea un programa que funcione como un gestor de contactos. El
programa debe permitir al usuario almacenar nombres y números de teléfono en un
diccionario, así como buscar, agregar y eliminar contactos. Debe mostrar un menú con las
siguientes opciones:
1. Agregar contacto
2. Buscar contacto
3. Eliminar contacto
4. Mostrar todos los contactos
5. Salir
"""

contactos = {}
bandera = 1
opcion = 0
opciones_validas = [1, 2, 3, 4, 5]
encontrado = False

while bandera == 1:
    while True:
        try: 
            opcion = int(input("""\n1. Agregar contacto\n2. Buscar contacto\n3. Eliminar contacto\n4. Mostrar todos los contactos\n5. Salir\n"""))
            if opcion in opciones_validas:
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    
    if (opcion == 1):
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el teléfono: "))
        contactos[nombre] = telefono
    
    if (opcion == 2):
        nombreBuscado = input("Ingrese el nombre que desea buscar: ")
        if nombreBuscado in contactos:
            telefono = contactos[nombreBuscado]
            print("El teléfono de " + nombreBuscado + " es " + str(telefono))
        else:
            print("El nombre ingresado no se encuentra en el diccionario.")
    
    if (opcion == 3):
        nombreBuscado = input("Ingrese el nombre que desea eliminar: ")
        if nombreBuscado in contactos:
            del contactos[nombreBuscado]
            print("El contacto ha sido eliminado")
        else:
            print("El nombre ingresado no se encuentra en el diccionario.")
    
    if (opcion == 4):
        for nombre, telefono in contactos.items():
            print("Nombre: " + nombre + ", Teléfono: " + str(telefono))
    
    if (opcion == 5):
        print("programa finalizado con éxito.")
        bandera == 0
        break
        
           
            
 #SUGERENCIA PEQUEÑA CORRECIÒN: 

contactos = {}
bandera = 1
opcion = 0
opciones_validas = [1, 2, 3, 4, 5]
encontrado = False

while bandera == 1:
    while True:
        try: 
            opcion = int(input("""\n1. Agregar contacto\n2. Buscar contacto\n3. Eliminar contacto\n4. Mostrar todos los contactos\n5. Salir\n"""))
            if opcion in opciones_validas:
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido. Intente nuevamente.")
    
    if opcion == 1:
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el teléfono: "))
        contactos[nombre] = telefono
    
    if opcion == 2:
        nombreBuscado = input("Ingrese el nombre que desea buscar: ")
        if nombreBuscado in contactos:
            telefono = contactos[nombreBuscado]
            print("El teléfono de " + nombreBuscado + " es " + str(telefono))
        else:
            print("El nombre ingresado no se encuentra en el diccionario.")
    
    if opcion == 3:
        nombreBuscado = input("Ingrese el nombre que desea eliminar: ")
        if nombreBuscado in contactos:
            del contactos[nombreBuscado]
            print("El contacto ha sido eliminado")
        else:
            print("El nombre ingresado no se encuentra en el diccionario.")
    
    if opcion == 4:
        for nombre, telefono in contactos.items():
            print("Nombre: " + nombre + ", Teléfono: " + str(telefono))
    
    if opcion == 5:
        print("¡Hasta luego!")
        bandera = 0
        break
