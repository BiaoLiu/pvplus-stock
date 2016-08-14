#coding:utf-8
from functools import wraps

from rest_framework.response import Response

from pvplus_common.models import response_message, response_retcode


def  requestparams_validate(serializer):
    '''请求参数校验'''

    def decorator(func):
        @wraps(func)
        def in_decorator(self, request, *args, **kwargs):
            # 通用处理
            command = serializer(data=request.GET)
            if not command.is_valid():
                response_message['recode'] = response_retcode['error']
                response_message['errmsg'] = command.errors
                return Response(response_message)
            kwargs['command'] = command.validated_data
            return func(self, request, *args, **kwargs)
        return in_decorator
    return decorator