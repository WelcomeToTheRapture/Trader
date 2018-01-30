# -*- coding: utf-8 -*-
"""
Information for coin traders API's.
"""
from django.db import models


class ApiInfo(models.Model):
    name = models.CharField(max_length=30, blank=True)
    pagina = models.CharField(max_length=30, blank=True)
    api = models.CharField(max_length=30, blank=True)
