# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from .utils import SHIP_TYPES_CHOICHES


class Game(models.Model):

    name = models.CharField('Game', max_length=100, blank=True, null=True)
    player1 = models.ForeignKey(
        User, related_name='games1', on_delete=models.CASCADE
    )
    player2 = models.ForeignKey(
        User, related_name='games2', on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'game'
        verbose_name_plural = 'games'

    @property
    def players(self):
        return (self.player1, self.player2)


class Ship(models.Model):
    game = models.ForeignKey(
        Game, related_name='ships', on_delete=models.CASCADE
    )
    player = models.ForeignKey(
        User, related_name='ships', on_delete=models.CASCADE
    )
    ship = models.SmallIntegerField(choices=SHIP_TYPES_CHOICHES)

    class Meta:
        verbose_name = 'ship'
        verbose_name_plural = 'ships'


