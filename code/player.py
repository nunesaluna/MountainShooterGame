#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super(). __init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: #subir a nave somente até o topo
            self.rect.centery -= ENTITY_SPEED[self.name] #mexendo no eixo y o "retangulo" player
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: #descer a nave
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # andar com a nave somente até a borda esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH: #com elIF, duas teclas ñ poderiam ser pressionadas ao mesmo tempo.
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass
