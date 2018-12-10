# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Ship, ShipPosition
from .utils import SHIP_TYPES_CHOICHES, SHIP_TYPES, ShipType


class CreateShips(object):

    def __init__(self, game, player1, player2):
        self.game = game
        self.player1 = player1
        self.player2 = player2

    def create(self):
        for ship_type in SHIP_TYPES_CHOICHES:
            self.create_ship(ship_type[0])

    def create_ship(self, ship_type):

        # create ships for player 1
        ship1 = Ship.objects.create(
            game=self.game,
            player=self.player1,
            ship=ship_type
        )

        # create ships for player 2
        ship2 = Ship.objects.create(
            game=self.game,
            player=self.player2,
            ship=ship_type
        )
        return ship1, ship2


# ships(ships from player in the game), ship_positions(ship positions that is send)
def ship_positioning(ships, ship_positions):
    ship_id = [ship.id for ship in ships]
    ships_position_id = [ship_position['ship'] for ship_position in ship_positions]
    if ships_position_id != ship_id:
        raise serializers.ValidationError('Wrong Ships')

    positions = []
    for ship_position in ship_positions:
        ship = Ship.objects.get(pk=ship_position['ship'])
        ship_type = SHIP_TYPES_CHOICHES[ship.ship-1][0]
        ship_size = SHIP_TYPES[ship_type-1].size
        horizontal = ship_position['horizontal']

        x = ship_position['x']
        y = ship_position['y']
        i = 1

        positions.append(ShipPosition(
            ship=ship,
            horizontal=horizontal,
            x=x,
            y=y,
        ))
        for i in range(i, ship_size):
            if horizontal:
                positions.append(ShipPosition(
                    ship=ship,
                    horizontal=horizontal,
                    x=x+i,
                    y=y,
                ))
            else:
                positions.append(ShipPosition(
                    ship=ship,
                    horizontal=horizontal,
                    x=x,
                    y=y+i,
                ))
    list_position = [(item.x, item.y) for item in positions]
    # unique ship positions
    set_positions = set(list_position)
    # check if there are ship position that go over 10(size of the table)
    overflow = [item for item in positions if item.x > 10 or item.y > 10]

    if len(positions) != len(set_positions) or overflow:
        raise serializers.ValidationError('Ship overlap, please select valid postitons')

    ShipPosition.objects.bulk_create(positions)
    return positions
