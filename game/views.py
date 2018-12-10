# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, status
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Game, Ship, ShipPosition, Attack
from .serializers import GameSerializer,  ShipPositonSerializer, AttackSerializer
from .services import ship_positioning


class GameView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_fields = ('id', 'name', )


class ShipPostionView(generics.CreateAPIView):
    queryset = ShipPosition.objects.all()
    serializer_class = ShipPositonSerializer

    def create(self, request, game_id):
        self.user = request.user
        ship_positions = request.data
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        ships = Ship.objects.filter(game=game_id, player=self.user)

        # check for validated postions and create shippositions
        ship_positioning(ships, ship_positions)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )


class AttackView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer
    filter_fields = ('game', 'player', 'hit')
