# coding:utf-8
from django.db import models
from pvplus_common.string_extension import get_uuid
from pvplus_model.models.user import AppUserProfile


class AppPerspectCommentGoods(models.Model):
    pk_key = models.CharField(primary_key=True, max_length=40)
    pk_comment = models.CharField(max_length=40, blank=True, null=True)
    pk_user = models.CharField(max_length=40, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'app_perspect_comment_goods'


class AppPerspectComments(models.Model):
    pk_comment = models.CharField('id', primary_key=True, max_length=40)
    pk_perspect = models.CharField('决议id', max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    content = models.TextField('内容', null=True)
    atuserid = models.CharField('@用户', max_length=40, blank=True, null=True)
    atcommentid = models.CharField('@评论', max_length=40, blank=True, null=True)
    floor = models.IntegerField('楼层', default=0, blank=True, null=True)
    goodnum = models.IntegerField('点赞数', default=0, blank=True, null=True)
    isaudited = models.NullBooleanField('是否审核', blank=True, null=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'app_perspect_comments'
        verbose_name = '决议评论'
        verbose_name_plural = '决议评论列表'

    def __str__(self):
        return self.content[:20]


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
    pk_perspect = models.CharField('决议id', primary_key=True, default=get_uuid(), max_length=40)
    pk_stock = models.CharField('股票', max_length=40, blank=True, null=True)
    pk_user = models.CharField('用户id', max_length=40, blank=True, null=True)
    stockprice = models.DecimalField('股票价格', max_digits=18, decimal_places=2, null=True)
    isbullish = models.NullBooleanField('是否看多', null=True)
    expertprice = models.DecimalField('预期价格', max_digits=18, decimal_places=2, null=True)
    expertrate = models.DecimalField('预期收益率', max_digits=18, decimal_places=2, null=True)
    expertyearprofit = models.DecimalField('企业年利润', max_digits=18, decimal_places=2, null=True)
    title = models.CharField('标题', max_length=200, null=True)
    reason = models.TextField('原因', null=True)
    commentnum = models.IntegerField('评论数', default=0, blank=True, null=True)
    goodnum = models.IntegerField('点赞数', default=0, blank=True, null=True)
    downnum = models.IntegerField('踩数', default=0, blank=True, null=True)
    isaudited = models.NullBooleanField('是否审核', null=True)
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'app_perspects'
        verbose_name = '决议'
        verbose_name_plural = '决议列表'


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
