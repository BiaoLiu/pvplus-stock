#coding:utf-8
from django import forms

from pvplus_model.models.question import AppQuestions


class QuestionForm(forms.ModelForm):

    class Meta:
        model=AppQuestions
        exclude=('pk_question','isaudited','status','createtime','updatetime')


