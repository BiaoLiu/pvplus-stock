#coding:utf-8
from django.db import models

class AppListens(models.Model):
    pk_listen = models.CharField(primary_key=True, max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    iscommented = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_listens'


class AppQuestionComments(models.Model):
    pk_comment = models.CharField(primary_key=True, max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_question_comments'


class AppQuestionGoods(models.Model):
    pk_key = models.CharField(primary_key=True, max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_question_goods'


class AppQuestions(models.Model):
    pk_question = models.CharField(primary_key=True, max_length=40)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    questionmode = models.CharField(max_length=20, blank=True, null=True)
    questionrelate = models.CharField(max_length=20, blank=True, null=True)
    pk_respondent = models.CharField(max_length=40, blank=True, null=True)
    listennum = models.IntegerField(blank=True, null=True)
    isopen = models.IntegerField(blank=True, null=True)
    iscommented = models.IntegerField(blank=True, null=True)
    question_price = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    listen_price = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    isaudit = models.IntegerField(blank=True, null=True)
    goodnum = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_questions'

class AppAnswers(models.Model):
    pk_answer = models.CharField(primary_key=True, max_length=40)
    pk_question = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    voice = models.CharField(max_length=200, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    isbest = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_answers'