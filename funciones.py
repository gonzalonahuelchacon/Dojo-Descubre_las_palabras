from data import lista_palabras
import random

def mezclar_palabra(letras:str):
    '''
    Mezcla las letras

    '''
    retorno = False
    if len(letras) > 0:
        lista_letras = list(letras)

        random.shuffle(lista_letras)
        retorno = "".join(lista_letras)

    return retorno


def elegir_key(claves:list):
    """recibe una lista de claves y devuelve una al azar

    Args:
        palabras (list): lista de palabras

    Returns:
        _type_: False en caso de que la lista este vacia, sino retorna una key al azar
    """
    return random.choice(claves)

def crear_lista_claves(lista:list):
    """recibe la lista de las palabras y retorna una lista con las key 

    Args:
        lista (list): lista de las palabras

    Returns:
        _type_: False en caso de que la lista este vacia, sino retorna una lista con todas las key
    """
    retorno = False
    if len(lista) > 0:
        lista_claves = []
        for claves in lista:
            lista_claves.append(claves)
        retorno = lista_claves
    return retorno

def letras_disponibles(palabra):
    """recibe una serie de letras la mete en una lista y crea un set de la misma

    Args:
        palabra (_type_): letras a settear

    Returns:
        _type_: False en caso de que la palabra este vacia, sino devuelve una lista seteada de las letras de ese palabra
    """
    retorno = False
    if len(palabra) > 0:
        lista_letras = []
        for letra in palabra:
            lista_letras.append(letra)
        letras_disponibles = set(lista_letras)
        retorno = letras_disponibles
    return retorno

def pedir_letras(letras_disponible:set):
    letra = input("Ingrese letra: ")