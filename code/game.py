#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.menu import Menu
from const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self ):


        while True:
            menu = Menu (self.window)
            menu.run()
            pass
            # Check for all events
            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      print('Quitting')
               #     pygame.quit() # close pygame
                #    quit() # end pygame