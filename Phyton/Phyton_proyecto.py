import pygame
import random

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Chase the dot')
clock = pygame.time.Clock()

color_background = (255, 255, 255)
color_circle = (255, 0, 0)
radio_circle = 30
position_circle = (random.randint(radio_circle, 800-radio_circle), random.randint(ratio_circle, 600-ratio_circle))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (mouse_x - position_circle[0])**2 + (mouse_y - position_circle[1])**2 <= ratio_circle**2:
        puntuacion += 1
        posicion_circulo = (random.randint(ratio_circle, 800-ratio_circle), random.randint(ratio_circle, 600-ratio_circle))

    window.fill(color_background)
    pygame.draw.circle(window, color_circle, position_circle, ratio_circle)
    pygame.display.flip()
   
