from django.contrib import admin

# Register your models here.

from pvplus_model.models.stock import AppStock
from pvplus_model.models.question import AppQuestions,AppAnswers,AppListens


@admin.register(AppQuestions)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('pk_question','get_users')
    exclude = ('pk_question',)

@admin.register(AppAnswers)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(AppListens)
class ListenAdmin(admin.ModelAdmin):
    pass





# admin.site.register(AppQuestions)
# admin.site.register(AppAnswers)
# admin.site.register(AppListens)