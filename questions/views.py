# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from questions.models import Question


class QuestionList(ListView):
    model = Question
    paginate_by = 1



def index(request):
    return render(request, "questions/index.html")


def settings(request):
    return render(request, "questions/settings.html")

def login(request):
    return render(request, "questions/login.html")

def register(request):
    return render(request, "questions/register.html")