def listaInvitados():

    invitados = []

    def agregar_invitado():
        nombre = input(
            "Ingrese el nombre del invitado a agregar:"
        ).capitalize()  # JUAN -> Juan
        invitados.append(nombre)
        print(f"Se ha agregado {nombre} a la lista")

    def eliminar_invitado():
        nombre = input("Ingrese el nombre de la invitado a eliminar:").capitalize()
        if nombre in invitados:
            invitados.remove(nombre)
        else:
            print("La persona no esta en la lista")

    def verificar_invitado():
        nombre = input("Ingrese el nombre del invitado a consultar:").capitalize()
        if nombre in invitados:
            print(f"La persona {nombre} se encuentra en la lista")
        else:
            print(f"La persona{nombre} no se encuentra en la lista")

    def editar_invitado():
        nombre = input("Ingrese el invitado que desea editar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del invitado: ").capitalize()

        if nombre.capitalize() in invitados:
            index_nombre = invitados.index(nombre)
            invitados[index_nombre] = nuevo_nombre
            print(f"El nombre de {nombre} ha sido cambiado por {nuevo_nombre}")
        else:
            print(f"La persona {nombre} no se encuentra en la lista")

    def mostar_invitados():
        print("Invitados")
        for invitado in invitados:
            print(f"- {invitado}")
        print()

    def menuInvitados():
        while True:
            print("\n1. Agregar invitado")
            print("2. Eliminar invitado")
            print("3. Editar invitado")
            print("4. Verificar invitado")
            print("5. Mostrar invitado")
            print("6. Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                agregar_invitado()
            elif opcion == 2:
                eliminar_invitado()
            elif opcion == 3:
                editar_invitado()
            elif opcion == 4:
                verificar_invitado()
            elif opcion == 5:
                mostar_invitados()
            elif opcion == 6:
                break
            else:
                print("Opcion incorrecta")

    return menuInvitados


aplicacionInvitados = listaInvitados()
aplicacionInvitados()
