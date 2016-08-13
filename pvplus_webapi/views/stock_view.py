# coding:utf-8
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.views import Response

from pvplus_common.models import response_message
from pvplus_common.request_validate import requestparams_validate
from pvplus_model.models.stock import AppStock
from pvplus_webapi.serializers.stock import StockCommandSerializer, StockSerializer
from pvplus_webapi.services.stock_service import StockService


class StockViewSet(viewsets.ModelViewSet):
    queryset = AppStock.objects.all()

    @list_route(url_path='getstocklist')
    @requestparams_validate(StockCommandSerializer)
    def get_stocks(self, request, *args, **kwargs):
        '''获取股票列表'''
        # command = StockCommandSerializer(data=request.GET)
        # if not command.is_valid():
        #     response_message['recode'] = response_retcode['error']
        #     response_message['errmsg'] = command.errors
        #     return Response(response_message)

        stocks = StockService().get_stocks(**kwargs['command'].validated_data)
        response_message['data'] = StockSerializer(stocks, many=True).data

        return Response(response_message)