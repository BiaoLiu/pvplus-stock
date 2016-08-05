# coding: utf-8
from django import forms
from pvplus_model.models.question import AppQuestions
from pvplus_model.models.user import AppUserProfile

YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)

def get_users(is_respondent=False):
    """获取用户列表"""
    users= AppUserProfile.objects
    if is_respondent: #认证用户
        users=users.filter(isverified=True)

    return tuple(users.values_list('pk_user','realname'))

class QuestionForm(forms.ModelForm):
    user=forms.ChoiceField(choices=get_users(),label='提问用户',initial='pk_user')
    respondent=forms.ChoiceField(choices=get_users(True),label='回答用户')

    class Meta:
        model=AppQuestions
        exclude=('',)




