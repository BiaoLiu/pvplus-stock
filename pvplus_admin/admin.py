from django.contrib import admin

# Register your models here.

from pvplus_model.models.stock import AppStock
from pvplus_model.models.question import AppQuestions,AppAnswers,AppListens

admin.site.register(AppStock)
admin.site.register(AppQuestions)
admin.site.register(AppAnswers)
admin.site.register(AppListens)