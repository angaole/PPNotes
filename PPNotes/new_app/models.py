  # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class messa(models.Model):
    number = models.IntegerField(primary_key=True)
    ids = models.CharField(max_length=34)
    loca = models.CharField(max_length=34)
    alias = models.CharField(max_length=100, default="")
    dise = models.CharField(max_length=80)
    dis_sco = models.CharField(max_length=20)
    snp = models.CharField(max_length=120)

class seqe(models.Model):
    ids = models.CharField(max_length=34, primary_key=True)
    locas = models.CharField(max_length=34, default="chr")
    expre = models.CharField(max_length=34)
    seq = models.TextField()

class genes(models.Model):
    number = models.IntegerField(primary_key=True)
    ids = models.CharField(max_length=34)
    gene = models.CharField(max_length=34)
    gen_sco = models.CharField(max_length=34)
