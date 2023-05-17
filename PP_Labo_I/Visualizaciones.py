from os import system
import re
import unidecode
import Validaciones
import Utilidades

def dbz_imprimir_menu():
    """_summary_
        Funcion encargada de imprimir el menu principal de opciones
    """    
    menu = ["1.Traer datos desde archivo",
            "2.Listar cantidad por raza",
            "3.Listar personajes por raza",
            "4.Listar personajes por habilidad",
            "5.Jugar batalla",
            "6.Guardar Json",
            "7.Leer Json",
            "8.Salir del programa"]
    
    for i in range(len(menu)):
        print(menu[i])


def dbz_menu_principal():
    """_summary_
        Imprime menú de opciones y pide al usuario ingresar una opcion correspondiente 
    Returns:
        int: Devuelvo la opcion ingresada o -1 en caso de ser incorrecta
    """    
    dbz_imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    if Validaciones.validar_entero(opcion):
        opcion = int(opcion)
        while opcion < 1 or opcion > 8:
                system('cls')
                dbz_imprimir_menu()
                opcion = input("Error,ingrese una opcion valida: ")
                if Validaciones.validar_entero(opcion):
                    opcion = int(opcion)
                else:
                    opcion = -1
        return opcion
    else:
        return -1

# ----------------------------------- PUNTO 2 --------------------------------
def dbz_agrupar_por_tipo(lista:list,tipo:str):
    """_summary_
        Imprime los personajes agrupados por el tipo especificado
    Args:
        lista (list): lista de diccionarios 
        tipo (str): Indicador sobre que tipo trabajar
    """    
    personajes_por_tipo = {}
    
    for personaje in lista:
        valor = personaje[tipo][0]
        if valor in personajes_por_tipo:
            personajes_por_tipo[valor] += 1
        else:
            personajes_por_tipo[valor] = 1

    system('cls')
    print(f"Cantidad de personajes por {tipo}")
    for valor, cantidad in personajes_por_tipo.items():
        print(f"{valor}: {cantidad}")


# ----------------------------------- PUNTO 3 --------------------------------
def dbz_listar_por_tipo(lista:list,key:str):
    """_summary_
    Recibe e imprime los personajes agrupados por el tipo especificado y ademas su poder de ataque
    Args:
    lista (list): lista de personajes
    key (str): clave de la cual se requiere informacion
    """ 
    personajes_por_tipo = {}
    
    for personaje in lista:
        clave = personaje[key]
        
        for elemento in clave: 
            if elemento not in personajes_por_tipo:
                personajes_por_tipo[elemento] = []
            personajes_por_tipo[elemento].append({'nombre': personaje['nombre'], 'poder_ataque': personaje['poder_ataque']})
    
    system('cls')
    for clave, personajes in personajes_por_tipo.items():
        print(f"{clave}:")
        for personaje in personajes:
            print(f"- {personaje['nombre']} | Poder de ataque: {personaje['poder_ataque']}")
    
# ----------------------------------- PUNTO 4 --------------------------------
def submenu_habilidades(lista:list):
    """_summary_
    Imprime un submenu interactivo para mayor facilidad de gestión de habilidades al usuario.

    Args:
        lista (list): lista de diccionarios que contiene los personajes leídos del archivo
    """

    system('cls')
    print('''¿Qué desea realizar?
            1. Listar por habilidad
            2. Ver lista de habilidades disponibles''')

    opcion = input("Elija una opción: ").strip()

    while True:
        if not opcion:
            print("Debe ingresar una opción.")
            break
        elif not Validaciones.validar_entero(opcion):
            print("Debe ingresar un número entero.")
        elif int(opcion) not in [1, 2]:
            print("La opción elegida no es válida.")
        else:
            opcion = int(opcion)
            break

    if opcion == 1:
        habilidad = input("Ingrese la habilidad por la que desea listar: ")
        dbz_lista_por_habilidad(lista, habilidad)
    elif opcion == 2:
        imprimir_habilidades(lista)
        
        
def dbz_lista_por_habilidad(lista:list, habilidad:str):
    """_summary_
        Recibe la lista y una habilidad indicada por el usuario de la cual se informaran los datos segun corresponda
    Args:
        lista (list): lista de diccionarios que contiene los personajes leidos del archivo
        habilidad (str): elemento de la lista que tiene como valor la key 'habilidades'
    """    
    personajes = []
    habilidad = unidecode.unidecode(habilidad.lower())
    
    for personaje in lista:
        habilidades = []
        for elemento in personaje['habilidades']:
            elemento = unidecode.unidecode(elemento.lower())
            habilidades.append(elemento)
            
        if habilidad in habilidades:
            nombre = personaje['nombre']
            raza = personaje['raza']
            poder_pelea = personaje['poder_pelea']
            poder_ataque = personaje['poder_ataque']
            promedio_poder = Utilidades.calcular_promedio(poder_pelea, poder_ataque)
            
            personajes.append({
                'nombre': nombre,
                'raza': raza,
                'promedio_poder': promedio_poder
            })
        
    system('cls')
    for personaje in personajes:
        print(f"- Nombre: {personaje['nombre']} | Raza: {personaje['raza']} | Promedio Poder: {personaje['promedio_poder']}")

        
def imprimir_habilidades(diccionarios):

    habilidades_obtenidas = set()

    for diccionario in diccionarios:
        habilidades = diccionario.get('habilidades')
        if habilidades:
            habilidades_obtenidas.update(habilidades)

    system('cls')
    if habilidades_obtenidas:
        print("Habilidades obtenidas:")
        for habilidad in habilidades_obtenidas:
            print(f"- {habilidad}")
    else:
        print("No se encontraron habilidades")

