# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['name', 'player1', 'player2']


admin.site.register(Game, GameAdmin)
