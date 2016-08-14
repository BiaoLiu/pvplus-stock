# coding:utf-8
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from pvplus_common.models import response_retcode, response_message
from pvplus_common.request_validate import requestparams_validate
from pvplus_common.serviceresult import is_empty
from pvplus_model.models.question import AppQuestions
from pvplus_webapi.serializers.question import QuestionListCommandSerializer, QuestionCommandSerializer
from pvplus_webapi.services.questhon_service import QuestionService


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = AppQuestions.objects.all()

    @list_route(url_path='getquestionlist')
    @requestparams_validate(QuestionListCommandSerializer)
    def get_questions(self, request, *args, **kwargs):
        '''获取提问列表'''
        return Response(data='test')

    @list_route(url_path='createquestion')
    @requestparams_validate(QuestionCommandSerializer)
    def create_question(self, request, *args, **kwargs):
        '''创建提问'''
        result = QuestionService().create_question(**kwargs['command'])
        if not is_empty(result.ruleviolations):
            response_message['recode'] = response_retcode['error']
            response_message['errmsg'] = result.ruleviolations
        else:
            response_message['data'] = result.data

        return Response(response_message)
