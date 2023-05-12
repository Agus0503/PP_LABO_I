import json
import Utilidades

def leer_csv(ruta:str):
    """_summary_
        Leo el archivo segun la ruta recibida por parametro
    Args:
        ruta (str): direccion donde se encuentra el archivo a leer
    Returns:
        list: devuelve una lista de los datos leidos del archivo
    """    
    lista_retorno = []
    
    with open(ruta, 'r',encoding='utf-8') as archivo:
       for linea in archivo:
            linea = linea.strip().split(',')
            personaje = {
                'id': int(linea[0]),
                'nombre': linea[1],
                'raza': Utilidades.separar_cadena(linea[2],'-'),
                'poder_pelea': int(linea[3]),
                'poder_ataque': int(linea[4]),
                'habilidades' : Utilidades.separar_cadena(linea[5],'|$%')
            }
            lista_retorno.append(personaje)
    
    return lista_retorno

def leer_json(ruta:str):
    """_summary_
        Recibo la direccion(ruta) la cual se desea leer
    Args:
        ruta (str): direccion del archivo a leer
    Returns:
        lista de diccionarios obtenida de la lectura del archivo JSON
    """    
    with open(ruta,"r") as mi_archivo:
        data = json.load(mi_archivo)
    
    return data

def mostrar_datos_json(archivo:str):
    
    data = leer_json(archivo)
    
    for personaje in data:
        nombre = personaje['nombre']
        poder = personaje['poder_ataque']
        habilidades = ' + '.join(personaje['habilidades_restantes'])
        print(f'{nombre} - {poder} - {habilidades.title()}')