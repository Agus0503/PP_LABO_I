def validar_entero(numero_str):
    """_summary_
        Valido que la cadena recibida contenga o no un numero entero
    Args:
        numero_str (str): cadena a evaluar
    Returns:
        bool: True si la cadena contiene un numero entero
              False si la cadena no contiene un numero entero  
    """    
    retorno = False

    if len(numero_str):
        if numero_str.isnumeric() or (numero_str[0] == "-" and numero_str[1:].isnumeric()):
            retorno = True
            
    return retorno

def validar_flotante(numero_str):
    """_summary_
        Valido que la cadena recibida contenga o no un numero flotante
    Args:
        numero_str (str): cadena a evaluar
    Returns:
        bool: True si la cadena contiene un numero flotante
              False si la cadena no contiene un numero flotante
    """    
    retorno = False
    cantidad_puntos = numero_str.count(".")

    if cantidad_puntos == 1:
        lista_flotante = numero_str.split(".")
        if validar_entero(lista_flotante[0]) and lista_flotante[1].isnumeric():
            retorno = True

    return retorno

def dbz_validar_lista(lista):
    """_summary_
        Recibo una lista y valido que no este vacia
    Args:
        lista (list): lista contenedora de los datos leidos del archivo CSV
    Returns:
        Bool: True si la lista no esta vacia
              False si la lista esta vacia
    """
    if not lista:
        return False
    
    return True

def validar_escritura(archivo):
    """_summary_
        Recibo y valido que el archivo se escribio correctamente
    Args:
        archivo : Archivo por el cual se desea validar una escritura
    Returns:
        Bool: True si pudo escribir
              False si no pudo  
    """    
    if archivo.tell() > 0:
        return True
    else:
        return False