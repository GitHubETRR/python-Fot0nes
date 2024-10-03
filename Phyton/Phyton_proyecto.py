#profe, dejé funciones incompletes, lo sigo trabajando al código
import pygame
import random

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Chase the')
reloj = pygame.time.Clock()
puntuacion = 0

color_fondo = (255, 255, 255)
color_circulo = (255, 0, 0)
radio_circulo = 30
posicion_circulo = (random.randint(radio_circulo, 800-radio_circulo), random.randint(radio_circulo, 600-radio_circulo))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (mouse_x - posicion_circulo[0])**2 + (mouse_y - posicion_circulo[1])**2 <= radio_circulo**2:
        puntuacion += 1
        posicion_circulo = (random.randint(radio_circulo, 800-radio_circulo), random.randint(radio_circulo, 600-radio_circulo))

    ventana.fill(color_fondo)
    pygame.draw.circle(ventana, color_circulo, posicion_circulo, radio_circulo)
    pygame.display.flip()
    reloj.tick(30)
