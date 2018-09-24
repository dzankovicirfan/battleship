# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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
