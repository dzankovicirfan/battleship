# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Ship
from .utils import SHIP_TYPES_CHOICHES


class CreateShips(object):

    def __init__(self, game, player1, player2):
        self.game = game
        self.player1 = player1
        self.player2 = player2

    def create(self):
        for ship_type in SHIP_TYPES_CHOICHES:
            self.create_ship(ship_type[0])

    def create_ship(self, ship_type):

        ship1 = Ship.objects.create(
            game=self.game,
            player=self.player1,
            ship=ship_type
        )
        ship2 = Ship.objects.create(
            game=self.game,
            player=self.player2,
            ship=ship_type
        )
        return ship1, ship2
