def crear_cantante():
    
    print("\n  INGRESE LA INFORMACION DEL CANTANTE\n")
    codigo = input("  Codigo: ")
    nombre = input("  Nombre Cantante: ")
    edad = input("Edad Cantante: ")
    genero = input("  Genero musical: ")
    pais = input("  Pais nacimiento: ")

        
    try:
        path = "./cantante.txt"
        archivo_escritura_abierto = open(path,mode="a") 
        archivo_escritura_abierto.writelines([f"{codigo},{nombre},{edad},{genero},{pais}\n"])
        archivo_escritura_abierto.close()
        print("\n INFORMACION INGRESADA CORRECTAMENTE \n")
    except Exception as error:
        print(f"Error en el ingreso: {error}")

def crear_disco():
    
    print("\n  INGRESE LA INFORMACION DEL DISCO\n")
    codigo = input("  Codigo: ")
    nombre = input("  Nombre Disco: ")
    formato = input("  Tipo Formato: ")
    anio = input("  Anio: ")
    precio = input("  Precio: ")
        
    try:
        path = "./disco.txt"
        archivo_escritura_abierto = open(path,mode="a") 
        archivo_escritura_abierto.writelines([f"{codigo},{nombre},{formato},{anio},{precio}\n"])
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
                nombre = input("  Ingrese nombre del cantante: ")
                edad = input("  Ingrese Edad Cantante: ")
                genero = input("  Ingrese Genero musical: ")
                pais = input("  Ingrese Pais nacimiento: ")
                modelo_modificado = f"{codigo},{nombre},{edad},{genero},{pais}\n"
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
                nombre = input("  Nombre del disco: ")
                formato = input("  Ingrese formato: ")
                anio = input("  Ingrese Anio: ")
                precio = input("  Ingrese precio: ")
                modelo_modificado = f"{codigo},{nombre},{formato},{anio},{precio}\n"
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
        print("DEBER CANTANTE-DISCO")
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
