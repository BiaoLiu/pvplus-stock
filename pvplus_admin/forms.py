# coding: utf-8
from django import forms
from django.db.models import Q

from pvplus_model.models.question import AppQuestions, AppAnswers
from pvplus_model.models.user import AppUserProfile

YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)


def get_users(is_respondent=False):
    """获取用户列表"""
    users = AppUserProfile.objects
    if is_respondent:  # 认证用户
        users = users.filter(isverified=True)

    return tuple(users.values_list('pk_user', 'realname'))


class QuestionForm(forms.ModelForm):
    user = forms.ChoiceField(choices=get_users(), label='提问用户')
    respondent = forms.ChoiceField(choices=get_users(True), label='回答用户')

    class Meta:
        model = AppQuestions
        exclude = ('',)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        instance = kwargs.get('instance')
        if instance:
            # initial['user'] = AppUserProfile.objects.filter(pk_user=instance.pk_user).values_list('pk_user','realname')[0]
            # userids=[instance.pk_user,instance.pk_respondent]
            # AppUserProfile.objects.filter(pk_user__in=userids).values_list('pk_user')[0][0]

            initial['user'] = instance.pk_user
            initial['respondent'] = instance.pk_respondent
            super(QuestionForm, self).__init__(initial=initial, *args, **kwargs)
        else:
            super(QuestionForm, self).__init__(*args, **kwargs)


def get_question():
    return AppQuestions.objects.filter(Q(isaudit=True) & Q(isopen=True)).values_list('pk_question', 'content')


class AnswerForm(forms.ModelForm):
    user = forms.ChoiceField(choices=get_users(True), label='用户', required=False)
    question = forms.ChoiceField(choices=get_question(), label='提问', required=False)

    class Meta:
        model = AppAnswers
        exclude = ('',)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        instance = kwargs.get('instance')

        if instance:
            initial['user'] = instance.pk_user
            initial['question'] = instance.pk_question

        super(AnswerForm, self).__init__(initial, *args, **kwargs)
