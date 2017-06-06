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
    snpid = models.CharField(max_length=34, default="1")

class seqe(models.Model):
    ids = models.CharField(max_length=34, primary_key=True)
    locas = models.CharField(max_length=34, default="chr")
    strand = models.CharField(max_length=3, default="+")
    classs = models.CharField(max_length=20, default="none")
    length = models.CharField(max_length=5, default="1")
    exons = models.CharField(max_length=2, default="0")
    expre = models.CharField(max_length=500)
    seq = models.TextField()

class genes(models.Model):
    number = models.IntegerField(primary_key=True)
    ids = models.CharField(max_length=34)
    gene = models.CharField(max_length=34)
    gen_sco = models.CharField(max_length=34)
