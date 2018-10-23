# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Game, Ship, ShipPosition
from .services import CreateShips


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'player1', 'player2')

    def create(self, validated_data):
        if validated_data['player1'] != validated_data['player2']:
            game = super(GameSerializer, self).create(validated_data)
            CreateShips(game, game.player1, game.player2).create()
            return game
        raise serializers.ValidationError('Players have to be different.')


class ShipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ship
        fields = ('id', 'game', 'player', 'ship')


class ShipPositonSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShipPosition
        fields = ('ship', 'horizontal', 'x', 'y')
