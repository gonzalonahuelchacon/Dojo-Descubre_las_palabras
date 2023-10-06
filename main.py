import pygame, sys
from funciones import *

key = elegir_key(crear_lista_claves(lista_palabras))
letras = mezclar_palabra(key)
letras_a_usar = letras_disponibles(letras)
print(letras_a_usar)

pygame.init()

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Descubre las palabras")

font = pygame.font.Font(None, 36)
texto = ""
texto_color = (255, 255, 255)
maximo = 10
letras_validadas = letras_disponibles(letras)
palabras_escritas = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
            elif event.key == pygame.K_RETURN:
                print("Texto escrito: ", texto)
                if texto in lista_palabras[key]:
                    palabras_escritas.append(texto)
                
                texto = ""
            else:
                if len(texto) < maximo:
                    if event.unicode in letras_validadas:
                        texto += event.unicode


    screen.fill((0, 0, 0))
    texto_surface = font.render(texto, True, texto_color)
    screen.blit(texto_surface, (10, 10))
    pygame.display.flip()

print(palabras_escritas)
pygame.quit()
sys.exit() 

