# -*- coding: utf-8 -*-
"""
Information for coin traders API's.
"""
from django.db import models


class Period(models.Model):
    tiempo = models.CharField(max_length=30, blank=False)
