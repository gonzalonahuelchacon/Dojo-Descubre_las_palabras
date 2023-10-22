from data import lista_palabras
import random, pygame

#Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

#Pantalla
width, height = 1600, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Descubre las palabras")

#Fps
tiempo = pygame.time.Clock()
FPS = 30

#Tiempo
tiempo_inicial = pygame.time.get_ticks()
duracion = 90000

#Fondo e icono
fondo = pygame.image.load(r"Imagenes\fondo.jpg")
fondo = pygame.transform.scale(fondo,(width ,height))
icono = pygame.image.load(r"Imagenes\icono.png")
pygame.display.set_icon(icono)

#Texto
texto = ""
texto_color = BLANCO

#largo de palabras
maximo = 10 

#Palbaras escritas por el usuario
palabras_escritas = []

#Claves
lista_clave = ["mares","relojeria","milanesa","floresta"]

#Puntuacion
acumulador = 0
def elegir_key(claves:list):  
    return random.choice(claves)

def mezclar_palabra(letras:str):
    
    retorno = False
    if len(letras) > 0:
        lista_letras = list(letras)

        random.shuffle(lista_letras)
        retorno = "".join(lista_letras)

    return retorno

def letras_disponibles(palabra):
    
    retorno = False
    if len(palabra) > 0:
        lista_letras = []
        for letra in palabra:
            lista_letras.append(letra)
        letras_disponibles = set(lista_letras)
        retorno = letras_disponibles
    return retorno

def mostrar_botones(screen):
    shuffle_button = pygame.draw.rect(screen, BLANCO, (1300, 395, 100, 35))
    clear_button = pygame.draw.rect(screen, BLANCO, (1300, 495, 100, 35))
    submit_button = pygame.draw.rect(screen, BLANCO, (1300, 545, 100, 35))

    font = pygame.font.Font(None, 34)
    shuffle_text = font.render("Shuffle", True, NEGRO)
    clear_text = font.render("Clear", True, NEGRO)
    submit_text = font.render("Submit", True, NEGRO)

    screen.blit(shuffle_text, (1315, 400))
    screen.blit(clear_text, (1315, 500))
    screen.blit(submit_text, (1315, 550))

    return shuffle_button, clear_button, submit_button

key = elegir_key(lista_clave)
letras = mezclar_palabra(key)
letras_a_usar = letras_disponibles(letras)
letras_str = str(letras_a_usar)

