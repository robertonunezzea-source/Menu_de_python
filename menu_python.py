#Código de Roberto Nuñez Zea 


seleccion_de_usuario = 0
lista_de_clientes= {} #Lista vacía 
paise_del_mundo = {
    "ES" : "España",
    "EC" : "Ecuador",
    "JP" : "Japón",
    "AR" : "Argentina",
    "AL" : "Alemania"}


while seleccion_de_usuario <=0 or seleccion_de_usuario> 6:
    print("Bienvenido usuario//////////////////////////////////////////////////////////////////////////////////////////////////")
    opcion_menu = ["Agregar Cliente(1)", "Eliminar Cliente(2)", "Listar Clientes(3)", "Buscar Cliente(4)", "Determinar país(5)", "Salir(6)"]


    #Para mostar el menú de opciones
    for opcion in opcion_menu:
        print(opcion)
    
    seleccion = input("Seleccione una opción: ")
    seleccion_de_usuario = int(seleccion)
    if seleccion_de_usuario ==1: #Agregar cliente
        clave_clt = input("Ingrese nombre: ".capitalize())
        valor_clt = input("Ingrese cédula (Ingrese las dos primeras letras): ")
        lista_de_clientes[clave_clt] = valor_clt
        seleccion_de_usuario =  0 #Regresa al bucle
    elif seleccion_de_usuario == 2:
        borrar_clt = input("Ingrese clave del cliente (nombre): ".capitalize())
        del lista_de_clientes[borrar_clt]# borra clave y su valor
        for clave in lista_de_clientes:
            print(clave)
        seleccion_de_usuario = 0 #Regresa al bucle
    elif seleccion_de_usuario == 3:
        for clave, valor in lista_de_clientes.items():
            print(f"{clave}: {valor}")
        seleccion_de_usuario = 0 #Regresa al bucle
    elif seleccion_de_usuario == 4: 
        existe_clt = input("Ingrese nombre a consultar: ")
        print(lista_de_clientes.get(existe_clt))
        seleccion_de_usuario = 0 #Regresa al bucle
    elif seleccion_de_usuario == 5:
        cedula_buscar= input("Ingrese la cédula a buscar: ".capitalize())
        dos_primeras_letras = ""
        i = 0#variable de control del for 
        for cedula in cedula_buscar:
            dos_primeras_letras += cedula
            i = i +1
            if i == 2:
                break
        print(paise_del_mundo.get(dos_primeras_letras))   
if seleccion_de_usuario == 6:
    print("Gracias")

