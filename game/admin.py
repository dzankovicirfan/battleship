# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Game, Ship, ShipPosition


class GameAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['name', 'player1', 'player2']


class ShipAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['game', 'player', 'ship']


class ShipPositionAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['ship', 'x', 'y']


admin.site.register(Game, GameAdmin)
admin.site.register(Ship, ShipAdmin)
admin.site.register(ShipPosition, ShipPositionAdmin)
