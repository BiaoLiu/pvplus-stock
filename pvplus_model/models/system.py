#coding:utf-8
from django.db import models


class AppMsg(models.Model):
    pk_msg = models.CharField(primary_key=True, max_length=40)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    pk_receive = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    msgtype = models.CharField(max_length=20, blank=True, null=True)
    isaudit = models.TextField(blank=True, null=True)  # This field type is a guess.
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_msg'


class AppMsgRecord(models.Model):
    pk_record = models.CharField(primary_key=True, max_length=40)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    pk_relate = models.CharField(max_length=40, blank=True, null=True)
    msgtype = models.CharField(max_length=20, blank=True, null=True)
    isread = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_msg_record'