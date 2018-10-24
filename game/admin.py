# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Game, Ship, ShipPosition, Attack


class GameAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['name', 'player1', 'player2']


class ShipAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['game', 'player', 'ship']


class ShipPositionAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['ship', 'x', 'y']


class AttackAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['game', 'player', 'x', 'y', 'hit']


admin.site.register(Game, GameAdmin)
admin.site.register(Ship, ShipAdmin)
admin.site.register(ShipPosition, ShipPositionAdmin)
admin.site.register(Attack, AttackAdmin)
