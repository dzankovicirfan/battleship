# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from .models import Game, Ship, ShipPosition, Attack
from .services import CreateShips


def turn(game, player):
    if player == game.player1 and game.player_turn:
        print(player == game.player1 and game.player_turn)
        game.player_turn = False
        game.save()
        return
    if player == game.player2 and not game.player_turn:
        game.player_turn = True
        game.save()
        return
    raise serializers.ValidationError('It is not your turn')


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


class AttackSerializer(serializers.ModelSerializer):
    '''
    Player 1 always plays first
    '''
    player = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Attack
        fields = ('game', 'player', 'x', 'y', 'hit')
        validators = [
            UniqueTogetherValidator(
                queryset=Attack.objects.all(),
                fields=('game', 'player', 'x', 'y')
            )
        ]

    def create(self, validated_data):
        player = self.context['request'].user
        game = validated_data['game']
        validated_data['player'] = player

        turn(game, player)

        ships = Ship.objects.filter(game=game, player=player)
        ship_hit = ShipPosition.objects.filter(
            ship__in=ships, x=validated_data['x'], y=validated_data['y']
        )
        if ship_hit:
            validated_data['hit'] = True

        attack = super(AttackSerializer, self).create(validated_data)
        return attack
