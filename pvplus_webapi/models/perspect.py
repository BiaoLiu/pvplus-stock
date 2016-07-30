#coding:utf-8
from django.db import models


class AppPerspectCommentGoods(models.Model):
    pk_key = models.CharField(primary_key=True, max_length=40)
    pk_comment = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_perspect_comment_goods'


class AppPerspectComments(models.Model):
    pk_comment = models.CharField(primary_key=True, max_length=40)
    pk_perspect = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    atuserid = models.CharField(max_length=40, blank=True, null=True)
    atcommentid = models.CharField(max_length=40, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    goodnum = models.IntegerField(blank=True, null=True)
    isaudited = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_perspect_comments'


class AppPerspectDowns(models.Model):
    pk_key = models.CharField(primary_key=True, max_length=40)
    pk_perspect = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_perspect_downs'


class AppPerspectGoods(models.Model):
    pk_key = models.CharField(primary_key=True, max_length=40)
    pk_perspect = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_perspect_goods'


class AppPerspects(models.Model):
    pk_perspect = models.CharField(primary_key=True, max_length=40)
    pk_stock = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    stockprice = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    isbullish = models.IntegerField(blank=True, null=True)
    expertprice = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    expertrate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    expertyearprofit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    commentnum = models.IntegerField(blank=True, null=True)
    goodnum = models.IntegerField(blank=True, null=True)
    downnum = models.IntegerField(blank=True, null=True)
    isaudited = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_perspects'

class VPerspectStock(models.Model):
    pk_perspect = models.CharField(max_length=40)
    pk_stock = models.CharField(max_length=40, blank=True, null=True)
    stockname = models.CharField(max_length=100, blank=True, null=True)
    tradetype = models.CharField(max_length=100, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    stockprice = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    isbullish = models.IntegerField(blank=True, null=True)
    expertprice = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    expertrate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    expertyearprofit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    commentnum = models.IntegerField(blank=True, null=True)
    goodnum = models.IntegerField(blank=True, null=True)
    downnum = models.IntegerField(blank=True, null=True)
    isaudited = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'v_perspect_stock'