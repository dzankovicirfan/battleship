# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, mixins

from .models import Game, Ship
from .serializers import GameSerializer, ShipSerializer


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
