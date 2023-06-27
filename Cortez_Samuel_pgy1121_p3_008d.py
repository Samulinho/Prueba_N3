import Funciones_prueba as fn

lista_ruts = []
lista_identificador = []

fn.validar_menu()
opcion= fn.validar_opcion()   
if opcion==1:
    fn.validar_nombre()
    fn.validar_rut()
    fn.identificador()
    fn.validar_nombre_mascota()
    fn.validar_cantidad_dias()
    fn.habitaciones()
elif opcion==2:
    fn.validar_rut()
    
elif opcion==3:
    fn.monto()

else:
    print("Gracias por su estadia")