import pygame
from pygame import display, event

pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(600, 480)) #criando a janela de visualização do game
print('Setup End')

print('Loop Start')
while True:
    #check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #constante do pygame
            pygame.quit() # Close Window
            quit() # End Pygame
