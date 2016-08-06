# coding: utf-8
from django import forms
from django.db.models import Q

from pvplus_model.models.perspect import AppPerspects, AppPerspectComments
from pvplus_model.models.question import AppQuestions
from pvplus_model.models.stock import AppStock
from pvplus_model.models.user import AppUserProfile


def get_users(is_verified=False):
    """获取用户列表"""
    users = AppUserProfile.objects
    if is_verified:  # 认证用户
        users = users.filter(isverified=True)

    return tuple(users.values_list('pk_user', 'realname'))

def get_stocks():
    """获取股票列表"""
    stocks = AppStock.objects.filter(isdisabled=True).values_list('pk_stock', 'stockname')
    return tuple(stocks)

def get_question():
    """获取提问列表"""
    questions = AppQuestions.objects.filter(Q(isaudited=True) & Q(isopen=True)).values_list('pk_question', 'content')
    return tuple(questions)

def get_perspects():
    """获取决议列表"""
    perspects = AppPerspects.objects.filter(isaudited=True).values_list('pk_perspect', 'title')
    return tuple(perspects)

def get_perspect_comments():
    """获取决议评论列表"""
    comments = AppPerspectComments.objects.filter(isaudited=True).values_list('pk_comment', 'content')
    return tuple(comments)


class AuthorForm(forms.Form):
    pk_user = forms.ChoiceField(choices=get_users(), label='用户')
