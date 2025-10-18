#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                List_Bg = []
                for i in range(7):
                    List_Bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    List_Bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return List_Bg
