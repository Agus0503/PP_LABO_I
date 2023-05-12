from os import system
import random
import datetime
import json
import re
import Parsers
import Validaciones
import Utilidades

def guardar_txt_resultado_batalla(ganador, perdedor):
    """_summary_
        Recibo por parametro los datos resultantes de la simulacion de batalla para escribir en el archivo
    Args:
        ganador : _description_
        perdedor : _description_
    Returns:
        Bool: True si pudo escribir en el archivo
              False si no pudo escribir en el archivo  
    """    
    with open("resultados-batallas.txt", "a",encoding='utf-8') as archivo:
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
        archivo.write(f"\nFecha de la batalla: {fecha_actual}\n")
        archivo.write(f"Ganador: {ganador['nombre']} \nPerdedor: {perdedor['nombre']}\n")
        
        retorno = Validaciones.validar_escritura(archivo)
        if retorno:
            print("Los datos de la batalla se guardaron correctamente")
        else:
            print("Hubo un error en la carga de datos de la batalla")
        
    return retorno

def guardar_csv_personajes_modificados(ruta:str,lista:list):
    """_summary_
        Creo un nuevo archivo CSV con los datos recibidos
    Args:
        ruta (str): direccion del archivo
        lista (list): lista de datos a guardar
    """    
    with open(ruta,'a',encoding='utf-8') as nuevo_csv:
        
        for personaje in lista:
            id_personaje = personaje['id']
            nombre = personaje['nombre']
            raza = personaje['raza']
            poder_pelea = personaje['poder_pelea']
            poder_ataque = personaje['poder_ataque']
            habilidades = personaje['habilidades']

            nuevo_csv.write(f"{id_personaje},{nombre},{raza},{poder_pelea},{poder_ataque},{habilidades}\n")

def dbz_jugar_batalla(lista:list):
    """_summary_
        Recibo la lista de datos leidos del archivo CSV para 
        simular una batalla entre los personajes pertenecientes a la lista
    Args:
        lista (list): lista contenedora de los datos leidos del archivo CSV
    """
    personaje_elegido = None
    personajes_actualizados = []
    
    system('cls')
    print("Elija su personaje:")
    for personaje in lista:
        print(f"{personaje['id']}. {personaje['nombre']} ")
    
    eleccion = input("Ingrese el id del personaje: ")
    while not eleccion.strip():  
        eleccion = input("Debe ingresar un valor. Ingrese el id del personaje: ")
        
    if Validaciones.validar_entero(eleccion):
         for personaje in lista:
            if personaje['id'] == int(eleccion): 
                if 'Saiyan' in personaje['raza']:  #Verifico que pertenece a la raza 'Saiyan
                    personaje['poder_pelea'] *= 1.50 #Aumento su poder de pelea un 50%
                    personaje['poder_ataque'] *= 1.70 #Aumento su poder de ataque un 70%
                    personaje['habilidades'].append('Transformacion Nivel Dios') #Agrego una nueva habilidad
                    print("Tu personaje es un Saiyan, Obtuviste un Power up!")
                    personajes_actualizados.append(personaje)
                personaje_elegido = personaje
                break
            
    if personaje_elegido is None:
        print("Debe seleccionar el numero de personaje mostrado en pantalla")
    
    oponentes_disponibles = []
    for personaje in lista:
        if personaje != personaje_elegido:
            oponentes_disponibles.append(personaje)
    oponente = random.choice(oponentes_disponibles)
    
    resultado = Utilidades.determinar_mayor_valor(personaje_elegido,oponente,'poder_ataque')
    ganador = resultado[0]
    perdedor = resultado[1]
    
    guardar_txt_resultado_batalla(ganador,perdedor)
    guardar_csv_personajes_modificados('personajes_modificados.csv',personajes_actualizados)
    

def guardar_personajes_json(lista:list,raza:str,habilidad:str):
    """_summary_
        Recibo la lista y los datos necesarios para guardar los mismos en el archivo json
    Args:
        lista (list): lista contenedora de los datos leidos del archivo CSV
        raza (str): dato ingresado por el usuario
        habilidad (str): dato ingresado por el usuario
    """    

    habilidad = re.sub(r'\s', '_', habilidad).title()
    raza = re.sub(r'\s]', '_', raza).title()
    
    ruta = f"{raza}_{habilidad}.Json"
    
    with open(ruta, 'w') as archivo:
        json.dump(lista, archivo, indent=4)


def leer_json_elegido(archivos_json:list):
    """_summary_
        Muestra una lista de archivos JSON disponibles y permite al usuario elegir cuál  desea leer,
        luego, invoco las funciones "leer_json" y "mostrar_datos_json" del módulo "Parsers" 
        para mostrar los datos del archivo seleccionado.
    Args:
        archivos_json (list): lista que contiene las rutas de los archivos Json existentes
    """    
    system('cls')
    if not archivos_json:
        print("No hay archivos Json para leer")
        return
    
    print("¿Qué archivo desea leer?")
    for i in range(1, len(archivos_json) + 1):
        print(f"{i}. {archivos_json[i-1]}")
    
    opcion = input("Ingrese el número del archivo que desea leer : ")
    
    if not Validaciones.validar_entero(opcion):
        print("ERROR: debe ingresar un número entero.")
        return
    
    opcion_int = int(opcion)
    
    if opcion_int < 1 or opcion_int > len(archivos_json):
        print("La opción no es válida.")
        return
    
    archivo_elegido = archivos_json[opcion_int - 1]
    
    system('cls')
    print(f"Leyendo el archivo {archivo_elegido}...")
    
    Parsers.leer_json(archivo_elegido)
    Parsers.mostrar_datos_json(archivo_elegido)
