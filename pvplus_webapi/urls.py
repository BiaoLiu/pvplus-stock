# coding:utf-8
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from pvplus_webapi.views.question_view import QuestionViewSet
from pvplus_webapi.views.stock_view import StockViewSet

router = DefaultRouter()
router.register('stock', StockViewSet)
router.register('question',QuestionViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
