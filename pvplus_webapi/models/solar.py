#coding:utf-8
from django.db import models


class AppInfoGlobalinstalled(models.Model):
    pk_year = models.CharField(primary_key=True, max_length=40)
    china = models.DecimalField(db_column='China', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    america = models.DecimalField(db_column='America', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    england = models.DecimalField(db_column='England', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    australia = models.DecimalField(db_column='Australia', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    germany = models.DecimalField(db_column='Germany', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    italy = models.DecimalField(db_column='Italy', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    japan = models.DecimalField(db_column='Japan', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    other = models.DecimalField(db_column='Other', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'app_info_globalinstalled'


class AppInfoSolar(models.Model):
    pk_year = models.CharField(primary_key=True, max_length=40)
    solarcells = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    solarmodule = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    centralizedinverter = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pvstytem = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'app_info_solar'

