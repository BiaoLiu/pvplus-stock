#coding:utf-8
from rest_framework import serializers

class ListBaseSerializer(serializers.Serializer):
    pindex=serializers.IntegerField()
    psize=serializers.IntegerField()