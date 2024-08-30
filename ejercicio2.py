def contactos():

    contactos = []

    def agregar_contacto():
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        contactos.append({"nombre": nombre, "telefono": telefono})
        print(f"Se ha agregado el contacto: {nombre} - {telefono}")

    def buscar_contacto():
        nombre = input("Nombre: ")
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                print(
                    f"Nombre: {contacto['nombre']} - Telefono: {contacto['telefono']}"
                )
                break
        else:
            print(f"No se ha encontrado el contacto: {nombre}")

    def eliminar_contacto():
        nombre = input("Nombre: ")
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                contactos.remove(contacto)
                print(f"Se ha eliminado el contacto: {nombre}")
                break
        else:
            print(f"No se ha encontrado el contacto: {nombre}")

    def mostrar_contactos():
        for contacto in contactos:
            print(f"Nombre: {contacto['nombre']} - Telefono: {contacto['telefono']}")

    def editar_contacto():
        nombre = input("Nombre del contacto a editar: ")
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_telefono = input("Nuevo telefono: ")
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                contacto["nombre"] = nuevo_nombre
                contacto["telefono"] = nuevo_telefono
                print(f"Se ha actualizado el contacto: {nombre} por {nuevo_nombre}")
                break
        else:
            print(f"No se ha encontrado el contacto: {nombre}")

    def menuContactos():
        while True:
            print("1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Eliminar contacto")
            print("4. Mostrar contactos")
            print("5. Editar contacto")
            print("6. Salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                agregar_contacto()
            elif opcion == 2:
                buscar_contacto()
            elif opcion == 3:
                eliminar_contacto()
            elif opcion == 4:
                mostrar_contactos()
            elif opcion == 5:
                editar_contacto()
            elif opcion == 6:
                break
            else:
                print("Opcion no valida")

    return menuContactos


menuContactos = contactos()
menuContactos()
