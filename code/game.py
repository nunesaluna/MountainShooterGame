#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        # Cria a janela do jogo
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        menu = Menu(self.window)  # Criado antes do loop o meu travou criando depois
        while True:
            menu.run()
            pass

