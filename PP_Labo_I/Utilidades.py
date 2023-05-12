import Controlador
import Validaciones
import unidecode

def separar_cadena(cadena, delimitador):
    """_summary_
        Recibe una cadena de texto y un delimitador y devuelve una lista de elementos separados por el delimitador,
        eliminando los elementos vacíos
    Args:
        cadena (str): cadena de texto 
        limitador (str): representacion del limitador por el cual se trabajara la cadena de texto
    Returns:
        list: lista de elementos separados por el delimitador solicitado
    """    
    elementos = cadena.split(delimitador)
    
    elementos_sin_vacios = []
    for elemento in elementos:
        if elemento.strip() != "":
            elementos_sin_vacios.append(elemento.strip())
    
    return elementos_sin_vacios

def calcular_promedio(valor1, valor2):
    """_summary_
        Obtengo los valores y calculo el promedio de los mismos
    Args:
        valor1 
        valor2 
    Returns:
        float: promedio entre los valores recibidos por parametro
    """    
    promedio = float((valor1 + valor2) / 2)
    return promedio


def determinar_mayor_valor(personaje1, personaje2, clave):
    """_summary_
        Recibe y compara los valores de los personajes segun el valor de la clave solicitada
    Args:
        personaje1 (dict): Diccionario que representa un personaje
        personaje2 (dict): Diccionario que representa un personaje.
        clave (str): El nombre del clave que se utilizará para determinar el mayor valor
    Returns:
        tupla: Una tupla que contiene dos diccionarios: el primero representa al ganador y el segundo al perdedor.
    """
    if personaje1[clave] is None or personaje2[clave] is None:
        print("Los personajes deben tener un valor válido para la clave especificada.")
        return False
        
    if personaje1[clave] > personaje2[clave]:
        ganador = personaje1
        perdedor = personaje2
    else:
        ganador = personaje2
        perdedor = personaje1

    return ganador, perdedor


def obtener_datos(lista:list, raza:str, habilidad_buscada:str):
    """_summary_
        Busca y obtiene las coincidencias solicitadas por el usuario 
        en la lista general de personajes devolviendo un filtro de la misma
    Args:
        lista (list): lista de diccionarios que contiene los personajes leidos del archivo
        raza (str): dato que desea obtener el usuario
        habilidad_buscada (str): _description_
    Returns:
        list: lista filtrada de los personajes que cumplen la condicion
    """    
    personajes_filtrados = []
    
    habilidad_buscada = unidecode.unidecode(habilidad_buscada.lower())
    raza = unidecode.unidecode(raza.lower())
    
    for personaje in lista:
        habilidades_no_buscadas = []
        habilidades_decodificadas = []
        
        for habilidad in personaje["habilidades"]:
            habilidad = unidecode.unidecode(habilidad.lower())
            habilidades_decodificadas.append(habilidad)
            if habilidad != habilidad_buscada:
                habilidades_no_buscadas.append(habilidad)
        
        raza_personaje = tuple(personaje["raza"])
        raza_personaje = unidecode.unidecode(raza_personaje[0].lower())
        
        if raza == raza_personaje and habilidad_buscada in habilidades_decodificadas:
            personajes_filtrados.append({
                "nombre": personaje["nombre"],
                "poder_ataque": personaje["poder_ataque"],
                "habilidades_restantes": habilidades_no_buscadas
            })
    
    if Validaciones.dbz_validar_lista(personajes_filtrados):
        Controlador.guardar_personajes_json(personajes_filtrados,raza,habilidad_buscada)
    else:
        print("No se encontraron coincidencias")