def crear_cantante():
    
    print("\n  INGRESE LA INFORMACION DEL CANTANTE\n")
    codigo = input("  Codigo: ")
    nombre = input("  Nombre Cantante: ")
    origen = input("  Pais de origen: ")
    genero = input("  Asignatura que dicta: ")
    discos_vendidos= input("  Promedio discos vendidos: ")
        
    try:
        path = "./cantante.txt"
        archivo_escritura_abierto = open(path,mode="a") 
        archivo_escritura_abierto.writelines([f"{codigo},{nombre},{origen},{genero},{discos_vendidos}\n"])
        archivo_escritura_abierto.close()
        print("\n INFORMACION INGRESADA CORRECTAMENTE \n")
    except Exception as error:
        print(f"Error en el ingreso: {error}")

def crear_disco():
    
    print("\n  INGRESE LA INFORMACION DEL DISCO\n")
    codigo = input("  Codigo: ")
    nombre_disco = input("  Nombre Disco: ")
    pais = input("  Pais: ")
    estilo = input("  Estilo: ")
    precio = input("  Precio: ")
        
    try:
        path = "./disco.txt"
        archivo_escritura_abierto = open(path,mode="a") 
        archivo_escritura_abierto.writelines([f"{codigo},{nombre_disco},{pais},{estilo},{precio}\n"])
        archivo_escritura_abierto.close()
        print("\n INFORMACION INGRESADA CORRECTAMENTE \n")
    except Exception as error:
        print(f"Error en el ingreso: {error}")


def leer_cantante():
    try:
        path='./cantante.txt'
        archivo_abierto = open(path)
        lineas= archivo_abierto.readlines()
        print("\nCANTANTE\n")
        for linea in lineas:
            print(f"  {linea}")
        archivo_abierto.close
    except Exception as error:
        print(f"ERROR AL CARGAR LOS CANTANTE: {error}")
    
    
def leer_Disco():
    try:
        path='./disco.txt'
        archivo_abierto = open(path)
        lineas= archivo_abierto.readlines()
        print("\nDISCO\n")
        for linea in lineas:
            print(f"  {linea}")
        archivo_abierto.close
    except Exception as error:
        print(f"ERROR AL CARGAR LOS DISCO: {error}")
        
        
def modificar_cantante():
    leer_cantante()
    codigo = input("\n  INGRESE EL CODIGO DEL CANTANTE A MODIFICAR: ")
    try:
        path="./cantante.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                nombre = input("  INGRESE EL NOMBRE DEL CANTANTE: ")
                origen = input("  INGRESE EL PAÍS ORIGEN: ")
		        genero = input("  INGRESE EL GENERO MUSICAL: ")
		        discos_vendidos = input("  INGRESE PROMEDIO DISCOS VENDIDOS: ")
                modelo_modificado = f"{codigo},{nombre},{origen},{genero},{discos_vendidos}\n"
                archivo_abierto.write(modelo_modificado)
                archivo_abierto.truncate()
                print(f"\n  CANTANTE {codigo} HA SIDO MODIFICADO \n")
            else:
                archivo_abierto.write(linea)
                archivo_abierto.truncate()
    except Exception as error:
        print(f"ERROR AL APLICAR LA MODIFICACION: {error}")


def modificar_disco():
    leer_Disco()
    codigo = input("\n  INGRESE EL CODIGO DEL DISCO A MODIFICAR: ")
    try:
        path="./disco.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                nombre_disco = input("  INGRESE NOMBRE DEL DISCO: ")
                pais = input("  INGRESE EL PAIS: ")
                estilo = input("  INGRESE EL ESTILO: ")
		precio = input("  INGRESE EL PRECIO: ")
                modelo_modificado = f"{codigo},{nombre_disco},{pais},{estilo},{precio}\n"
                archivo_abierto.write(modelo_modificado)
                archivo_abierto.truncate()
                print(f"\n  DISCO {codigo} HA SIDO MODIFICADO \n")
            else:
                archivo_abierto.write(linea)
                archivo_abierto.truncate()
    except Exception as error:
        print(f"ERROR AL APLICAR LA MODIFICACION: {error}")


def eliminar_cantante():
    leer_cantante()
    codigo = input("\n  INGRESE EL CODIGO DEL CANTANTE A ELIMINAR: ")
    try:
        path="./cantante.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                modelo_vacio = "\n"
                archivo_abierto.write(modelo_vacio)
                archivo_abierto.truncate()
        print(f"\n HA SIDO ELIMINADO: {codigo} \n")
    except Exception as error:
        print(f"ERROR AL INTENTAR BORRAR AL CANTANTE: {error}")
        
        
def eliminar_disco():
    leer_Disco()
    codigo = input("\n  INGRESE EL CODIGO DEL DISCO A ELIMINAR: ")
    try:
        path="./disco.txt"
        archivo_abierto = open(path, mode="r+")
        lineas = archivo_abierto.readlines()
        archivo_abierto.seek(0)
        for linea in lineas:
            if codigo in linea:
                modelo_vacio = "\n"
                archivo_abierto.write(modelo_vacio)
                archivo_abierto.truncate()
        print(f"\n HA SIDO ELIMINADO: {codigo} \n")
    except Exception as error:
        print(f"ERROR AL INTENTAR BORRAR AL DISCO: {error}")


def Star_Aplication():

        print("*********************************************")
        print("ESCUELA POLITECNICA NACIONAL")
        print("SISTEMA DE ASIGNACION CANTANTE-DISCO")
        print("SELECCIONE EL NUMERO DE LA OPCION A REALIZAR")
        print("1. INGRESE UN CANTANTE")
        print("2. INGRESE UN DISCO")
        print("3. CONSULTAR LISTA DE CANTANTE")
        print("4. CONSULTAR LISTA DE DISCO")
        print("5. MODIFICAR CANTANTE")
        print("6. MODIFICAR DISCO")
        print("7. ELIMINAR CANTANTE")
        print("8. ELIMINAR DISCO")
        print("9. TERMINAR PROGRAMA")
        print("*********************************************")

while True:
    Star_Aplication()
      
    opcionMenu = input("SELECCIONE UNA OPCION-> ")
            
    if opcionMenu=="1":
        print("1. \n  RESGISTRO DE CANTANTE")
        crear_cantante()
     
    elif opcionMenu=="2": 
        print("2. \n REGISTRO DE DISCO")
        crear_disco()
        
    elif opcionMenu=="3":
        print("3. \n LISTA DE CANTANTE")
        leer_cantante()
          
    elif opcionMenu=="4":
        print("3. \n LISTA DE DISCO")
        leer_Disco()  
        
    elif opcionMenu=="5":
        print("3. \n MODIFICAR CANTANTE")
        modificar_cantante()
        
    elif opcionMenu=="6":
        print("3. \n MODIFICAR DISCO")
        modificar_disco()
       
    elif opcionMenu=="7":
        print("3. \n ELIMINAR CANTANTE")
        eliminar_cantante()
        
    elif opcionMenu=="8":
        print("3. \n ELIMINAR DISCO")
        eliminar_disco()
        
    elif opcionMenu=="9":
        break
        
    else:
        input("OPCION INCORRECTA...\nSELECCIONE NUEVAMENTE UNA OPCION")        
