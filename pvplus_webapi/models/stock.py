#coding:utf-8
from django.db import models


class AppStock(models.Model):
    pk_stock = models.CharField(primary_key=True, max_length=40)
    stockname = models.CharField(max_length=100, blank=True, null=True)
    tradetype = models.CharField(max_length=100, blank=True, null=True)
    isdisabled = models.IntegerField(blank=True, null=True)
    istop = models.IntegerField(blank=True, null=True)
    sortno = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_stock'