import sys
from funciones import *

pygame.init()

font = pygame.font.Font(None, 50)
acierto = pygame.mixer.Sound(r"Musica\acierto.mp3")
error = pygame.mixer.Sound(r"Musica\incorrecto.mp3")
pygame.mixer.music.load(r"Musica\musica.mp3")
pygame.mixer.music.play(-1)

running = True
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
                        acierto.play()
                else:
                    error.play()                                               
                texto = ""
            else:
                if len(texto) < maximo:
                    if event.unicode in letras_str:
                        texto += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if shuffle_button.collidepoint(x, y):
                key = elegir_key(lista_clave)
                letras = mezclar_palabra(key)
                letras_a_usar = letras_disponibles(letras)
                letras_str = str(letras_a_usar)
            elif clear_button.collidepoint(x, y):
                texto = ""
            elif submit_button.collidepoint(x, y):
                    if texto in lista_palabras[key]:
                        if texto not in palabras_escritas:
                            palabras_escritas.append(texto)
                            acumulador+=5
                            acierto.play()
                    else:
                        error.play()                                       
                    texto = ""
                    
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    tiempo_restante = max(0,duracion-tiempo_transcurrido)
    if tiempo_restante <= 0:
        running = False

    segundos = tiempo_restante//1000
    screen.blit(fondo,(0,0))
    letras_surface = font.render("Letras a usar:" + (letras_str),True,texto_color) 
    screen.blit(letras_surface,(500, 400))
    texto_surface = font.render(F"Ingrese una palabra:{texto}", True, texto_color)
    screen.blit(texto_surface, (500, 500))
    tiempo_surface = font.render(f"Tiempo restante: {segundos}", True, texto_color)
    screen.blit(tiempo_surface, (1250, 10))
    puntaje = font.render(f"Puntuación:{acumulador}",True,texto_color)
    screen.blit(puntaje,(10,10))
    palabras_surface = font.render("Palabras en la lista: " + ', '.join(palabras_escritas), True, texto_color)
    screen.blit(palabras_surface, (10, 700))
    shuffle_button, clear_button, submit_button = mostrar_botones(screen)
    
    pygame.display.flip()
    
    tiempo.tick(FPS)
print(f"El puntaje obtenido es: {acumulador}")
pygame.quit()
sys.exit() 
