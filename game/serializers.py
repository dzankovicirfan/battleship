# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'player1', 'player2')

    def create(self, validated_data):
        if validated_data['player1'] != validated_data['player2']:
            return super(GameSerializer, self).create(validated_data)
        raise serializers.ValidationError('Player have to be different.')
