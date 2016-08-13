#coding:utf-8
from django.db import models


class AppTrandeorder(models.Model):
    pk_order = models.CharField(primary_key=True, max_length=40)
    pk_relate = models.CharField(max_length=40, blank=True, null=True)
    relateobj = models.CharField(max_length=20, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    totalamount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    paytype = models.CharField(max_length=20, blank=True, null=True)
    orderstatus = models.IntegerField(blank=True, null=True)
    paysource = models.CharField(max_length=20, blank=True, null=True)
    transactionid = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    paytime = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'app_trandeorder'