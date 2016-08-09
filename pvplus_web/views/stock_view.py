from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView,CreateView

from pvplus_web.forms import question_form


class QuestionView(ListView,CreateView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
        # form= question_form(request.POST)
        # if form.is_valid():
        #     return render()
