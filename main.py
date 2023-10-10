import pygame, sys
from funciones import *

key = elegir_key(crear_lista_claves(lista_palabras))
letras = mezclar_palabra(key)
letras_a_usar = letras_disponibles(letras)
letras_str = str(letras_a_usar)


pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Descubre las palabras")

font = pygame.font.Font(None, 36)
texto = ""
texto_color = NEGRO
maximo = 10
letras_validadas = letras_disponibles(letras)
palabras_escritas = []
running = True
tiempo = pygame.time.Clock()
tiempo_restante = 9000
acumulador=0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
            elif event.key == pygame.K_RETURN:
                if texto in lista_palabras[key]:
                    if texto not in palabras_escritas:
                        palabras_escritas.append(texto)
                        acumulador+=5
                    
                    
                texto = ""
            else:
                if len(texto) < maximo:
                    if event.unicode in letras_validadas:
                        texto += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                x, y = event.pos
                if shuffle_button.collidepoint(x, y):
                    letras = mezclar_palabra(key)
                    letras_validadas = letras_disponibles(letras)
                elif clear_button.collidepoint(x, y):
                    texto = ""
                elif submit_button.collidepoint(x, y):
                    if  texto in lista_palabras[key]:
                        if texto not in palabras_escritas:  # Verifica si la palabra no está en palabras_escritas
                            palabras_escritas.add(texto)  # Agrega la palabra al conjunto
                            acumulador += 5  # Aumenta el acumulador en 5
                    texto = ""


    screen.fill(BLANCO)
    #Muestra las letras a usar
    letras_surface = font.render("Letras a usar:" + (letras_str),True,texto_color) 
    screen.blit(letras_surface,(10,10))
    #Muestra la palabra ingresada
    texto_surface = font.render(F"Ingrese una palabra:{texto}", True, texto_color)
    screen.blit(texto_surface, (10, 50))
    # Muestra el tiempo restante
    tiempo_surface = font.render(f"Tiempo restante: {tiempo_restante}", True, texto_color)
    screen.blit(tiempo_surface, (10, 100))
    puntaje = font.render(f"Puntuación:{acumulador}",True,texto_color)
    screen.blit(puntaje,(10,150))
    # Muestra las palabras escritas
    palabras_surface = font.render("Palabras en la lista: " + ', '.join(palabras_escritas), True, texto_color)
    screen.blit(palabras_surface, (10, 200))
    shuffle_button, clear_button, submit_button = mostrar_botones(screen)
    pygame.draw.rect(screen, (0, 0, 0), shuffle_button, 2)  # Dibuja el borde de los botones
    pygame.draw.rect(screen, (0, 0, 0), clear_button, 2)
    pygame.draw.rect(screen, (0, 0, 0), submit_button, 2)
    pygame.display.flip()
    tiempo_restante -= 1
    if tiempo_restante <= 0:
        running = False

    tiempo.tick(60)
print(f"El puntaje obtenido es: {acumulador}")

pygame.quit()
sys.exit() 

