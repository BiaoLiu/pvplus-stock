#coding:utf-8
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from pvplus_common.request_validate import requestparams_validate
from pvplus_model.models.question import AppQuestions
from pvplus_webapi.serializers.question import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = AppQuestions.objects.all()

    @list_route(url_path='getquestionlist')
    @requestparams_validate(QuestionSerializer)
    def get_questions(self,request,*args,**kwargs):

        return Response(data='test')
