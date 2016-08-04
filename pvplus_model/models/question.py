# coding:utf-8
from django.db import models

from pvplus_model.models.user import AppUserProfile


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
    pk_question = models.CharField('问答id', primary_key=True, max_length=40)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    content = models.TextField('提问内容', blank=True, null=True)
    questionmode = models.CharField('提问方式', max_length=20, blank=True, null=True)
    questionrelate = models.CharField('提问相关', max_length=20, blank=True, null=True)
    pk_respondent = models.CharField('回复者id', max_length=40, blank=True, null=True)
    listennum = models.IntegerField('偷听人数', blank=True, null=True)
    isopen = models.NullBooleanField('是否公开', blank=True, null=True)
    iscommented = models.NullBooleanField('是否已评论', blank=True, null=True)
    question_price = models.DecimalField('提问价格', max_digits=18, decimal_places=4, blank=True, null=True)
    listen_price = models.DecimalField('偷听价格', max_digits=18, decimal_places=4, blank=True, null=True)
    isaudit = models.NullBooleanField('是否审核', blank=True, null=True)
    goodnum = models.IntegerField('点赞数', blank=True, null=True)
    status = models.IntegerField('状态', blank=True, null=True)
    createtime = models.DateTimeField('创建时间', blank=True, null=True)
    updatetime = models.DateTimeField('更新时间', blank=True, null=True)

    class Meta:
        db_table = 'app_questions'
        verbose_name_plural = verbose_name = '问答'

    def get_author(self):
        pass
        # return AppUserProfile.objects.filter(pk_user=self.pk_user)

    def get_users(self):
        return AppUserProfile.objects.filter(isverified=True)

    def __str__(self):
        return self.content


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
