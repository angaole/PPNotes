# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class message(models.Model):
    ids = models.CharField(max_length=9)
    loca = models.CharField(max_length=34)
    seq = models.CharField(max_length=34)
    snp = models.CharField(max_length=32)
    dise = models.CharField(max_length=20)
    dis_sco = models.IntegerField(max_length=1)
    gene = models.CharField(max_length=34)
    gen_sco = models.IntegerField(max_length=1)
    expre = models.IntegerField(max_length=1)
