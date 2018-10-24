# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils import SHIP_TYPES_CHOICHES


class Game(models.Model):

    name = models.CharField('Game', max_length=100, blank=True, null=True)
    player1 = models.ForeignKey(
        User, related_name='games1', on_delete=models.CASCADE
    )
    player2 = models.ForeignKey(
        User, related_name='games2', on_delete=models.CASCADE
    )
    player_turn = models.BooleanField(default=True)

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


class ShipPosition(models.Model):
    ship = models.ForeignKey(
        Ship, related_name='shippositions', on_delete=models.CASCADE
    )
    horizontal = models.BooleanField(default=True)
    x = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    y = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name = 'shippostion'
        verbose_name_plural = 'shippostions'


class Attack(models.Model):
    game = models.ForeignKey(
        Game, related_name='attacks', on_delete=models.CASCADE
        )
    player = models.ForeignKey(
        User, related_name='attacks', on_delete=models.CASCADE
    )
    x = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    y = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    hit = models.BooleanField(default=False)

    class Meta:
        unique_together = ('game', 'player', 'x', 'y')
        verbose_name = 'attack'
        verbose_name_plural = 'attacks'
