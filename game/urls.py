# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path, include

from rest_framework import routers

from .views import GameView, ShipPostionView

router = routers.SimpleRouter()
router.register(r'game', GameView)

app_name = 'game'

urlpatterns = [
    path('', include(router.urls)),
    path('shippositon/<int:game_id>/', ShipPostionView.as_view(), name='shippositon')
]
