# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from questions.models import Question


class QuestionList(ListView):
    model = Question
    paginate_by = 1


def questions_detail(request, question_id):
    return render(request, 'questions_detail.html', {'question': get_object_or_404(Question, pk=question_id)})

def questions_list(request):
    return render(request, 'questions_list.html', {'question': get_object_or_404(Question)})
