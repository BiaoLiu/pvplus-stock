# coding:utf-8
from rest_framework import serializers

from pvplus_webapi.serializers.base import ListBaseSerializer


class QuestionSerializer(ListBaseSerializer):
    keyword = serializers.CharField(required=False, default='')
    sorttype = serializers.CharField(required=False, default='')
    sortno = serializers.CharField(required=False, default='')
