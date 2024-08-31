def clasificarEdades():

    edad = int(input("Ingrese la edad: "))

    def esMayor():
        msg = ""
        if edad >= 18:
            msg = "Felicidades eres mayor de edad"
        else:
            msg = f"Eres menor de edad, te faltan {18-edad} años para ser mayor de edad"
        print(msg)

    def determinarGeneracion():
        anioNacimiento = 2024 - edad
        print(f"Naciste en el año: {anioNacimiento}")
        if 1928 <= anioNacimiento <= 1945:
            msg = "Eres de la generacion silent"
        elif 1945 < anioNacimiento <= 1964:
            msg = "Eres de la generacion baby boomer"
        elif 1964 < anioNacimiento <= 1980:
            msg = "Eres de la generacion x"
        elif 1980 < anioNacimiento <= 1993:
            msg = "Eres de la generacion millenial"
        elif 1993 < anioNacimiento <= 2010:
            msg = "Eres de la generacion z"
        elif 2010 < anioNacimiento <= 2024:
            msg = "Eres de la generacion alpha"
        print(msg)

    def numeroRedondo():
        msg = ""
        if edad % 10 == 0:
            msg = "Tu edad es un numero redondo"
        else:
            msg = "Tu edad no es un numero redondo"
        print(msg)

    def mostrarInfo():
        print(f"Tu edad es: {edad}")
        esMayor()
        determinarGeneracion()
        numeroRedondo()

    return mostrarInfo


mostarInfo = clasificarEdades()
mostarInfo()
