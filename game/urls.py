# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include

from rest_framework import routers

from .views import GameView, ShipPostionView, AttackView

router = routers.SimpleRouter()
router.register(r'game', GameView)
router.register(r'attack', AttackView)

app_name = 'game'

urlpatterns = [
    path('', include(router.urls)),
    path('shipposition/<int:game_id>/', ShipPostionView.as_view(), name='shipposition')
]
