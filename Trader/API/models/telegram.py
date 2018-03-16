# -*- coding: utf-8 -*-
"""
Information for Telegram Notifier Bot.
"""
from django.db import models
from django.contrib.auth.models import User


class TelegramData(models.Model):
    usuario = models.ForeignKey(User)
    chat_id = models.CharField(max_length=10)
