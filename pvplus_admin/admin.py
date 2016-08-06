from django.contrib import admin

# Register your models here.
from pvplus_admin.forms.question_form import QuestionForm, AnswerForm, ListenForm
from pvplus_admin.forms.perspect_form import PerspectForm, PerspectCommentForm
from pvplus_model.models.perspect import AppPerspects, AppPerspectComments
from pvplus_model.models.stock import AppStock
from pvplus_model.models.question import AppQuestions, AppAnswers, AppListens


@admin.register(AppQuestions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk_question', 'content')
    fields = ('pk_user', 'questionmode', 'questionrelate', 'content', 'pk_respondent', 'question_price', 'listen_price',
              'listennum', 'goodnum', 'isopen', 'isaudited')
    # exclude = ('pk_user','pk_question','pk_respondent','status','updatetime')
    form = QuestionForm

    # def save_model(self, request, obj, form, change):
    #     # if not change:
    #     #     obj.pk_question = str(uuid.uuid1()).replace('-','')
    #
    #     obj.pk_user = form.cleaned_data['user']
    #     obj.pk_respondent = form.cleaned_data['respondent']
    #
    #     obj.save()


@admin.register(AppAnswers)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk_answer', 'voice', 'duration', 'content')
    fields = ('pk_user', 'pk_question', 'voice', 'duration', 'content', 'isbest')
    form = AnswerForm


@admin.register(AppListens)
class ListenAdmin(admin.ModelAdmin):
    exclude = ('pk_listen', 'createtime')
    form = ListenForm


@admin.register(AppStock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('pk_stock', 'stockname', 'tradetype', 'isdisabled', 'istop', 'sortno')
    exclude = ('createtime',)


@admin.register(AppPerspects)
class PerspectAdmin(admin.ModelAdmin):
    list_display = ('pk_perspect', 'pk_stock', 'title', 'stockprice', 'isbullish', 'isaudited')
    fields = ('pk_stock', 'pk_user', 'title', 'reason', 'stockprice', 'isbullish', 'expertprice', 'expertrate',
              'commentnum', 'goodnum', 'downnum', 'isaudited')
    form = PerspectForm


@admin.register(AppPerspectComments)
class PerspectCommentAdmin(admin.ModelAdmin):
    exclude = ('pk_comment',)
    form = PerspectCommentForm





    # admin.site.register(AppQuestions)
    # admin.site.register(AppAnswers)
    # admin.site.register(AppListens)
