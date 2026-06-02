#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import display, event

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # criando a janela de visualização do game

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            #check for all events
            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT: #constante do pygame
            #        pygame.quit() # Close Window
            #        quit() # End Pygame
