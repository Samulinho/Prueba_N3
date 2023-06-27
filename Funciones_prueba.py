def validar_menu():
    print("""Menu
    1.Grabar
    2.Buscar
    3.Retirarse
    4.Salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def identificador():
    while True:
        try:
            num_identificador = int(input("Ingrese numero identificador: "))
            if num_identificador >= 1:
                return num_identificador
            else:
                print("ERROR! Ingrese un numero positivo")
        except:
            print("Tiene ser un numero positivo")



def validar_nombre_mascota():
        while True:
            nombre = input("Ingrese nombre de su mascota: ")
            if len(nombre.strip()) >= 3 and nombre.isalpha():
                return nombre
            else:
                print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_cantidad_dias():
    while True:
        try:
            cantidad_dias = int(input("Ingrese cantidad de dias que se quedara: "))
            if cantidad_dias >= 0:
                return cantidad_dias
            else:
                print("Ingrese una cantidad positiva")
        except:
            print("ERROR! Ingrese numero entero")

def habitaciones():
    while True:
        try:
            habitaciones = int(input("Ingrese la habitacion que quiere: "))
            if habitaciones >= 0:
                return habitaciones
            else:
                print("Ingrese un numero positivo")
        except:
            print("ERROR! Ingrese un numero entero")



def monto():
    while True:
        try:
            monto = int(input("Ingrese cantidad de dias: "))
            monto = 15000 * validar_cantidad_dias
            return monto
        except:
            print("Su total a pagar es: ")