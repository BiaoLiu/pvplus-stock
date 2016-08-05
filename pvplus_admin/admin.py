from django.contrib import admin

# Register your models here.
from pvplus_admin.forms import QuestionForm, AnswerForm
from pvplus_model.models.stock import AppStock
from pvplus_model.models.question import AppQuestions,AppAnswers,AppListens
import uuid


@admin.register(AppQuestions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk_question','content')
    fields = ('user','questionmode','questionrelate','content','respondent','question_price','listen_price',
              'listennum','goodnum','isopen','isaudit')
    # exclude = ('pk_user','pk_question','pk_respondent','status','updatetime')
    form = QuestionForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.pk_question = str(uuid.uuid1()).replace('-','')

        obj.pk_user= form.cleaned_data['user']
        obj.pk_respondent = form.cleaned_data['respondent']

        obj.save()


@admin.register(AppAnswers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk_answer','voice','duration','content')
    fields = ('user','question','voice','duration','content','isbest')
    form = AnswerForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.pk_answer = str(uuid.uuid1()).replace('-', '')

        obj.pk_user = form.cleaned_data['user']
        obj.pk_question = form.cleaned_data['question']

        obj.save()



@admin.register(AppListens)
class ListenAdmin(admin.ModelAdmin):
    pass





# admin.site.register(AppQuestions)
# admin.site.register(AppAnswers)
# admin.site.register(AppListens)