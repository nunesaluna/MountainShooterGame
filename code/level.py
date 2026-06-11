#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.entity_factory import EntityFactory
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #chamando o metodo get.entity da classe EntityFactory
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000 #20 segundos
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)


    def run(self):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock() #FPS baseado num tempo específico independente da máquina
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #fechar a janela no nível 1 = quit
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2')) #aleatoriamente escolhe entre spawns de inimigos 1 e 2
                    self.entity_list.append(EntityFactory.get_entity(choice))

            #printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10,5)) #tempo duração da fase
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35)) #mostra o fps na tela
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20)) #qts entidades tem na tela
            pygame.display.flip()
        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name= "Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color). convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
