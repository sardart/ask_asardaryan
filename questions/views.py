# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from questions.models import Question


class QuestionList(ListView):
    model = Question
    paginate_by = 1


def paginate(request, objects):
    paginator = Paginator(objects, 20)
    try:
        page = paginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        page = paginator.get_page(1)
    except EmptyPage:
        page = paginator.get_page(paginator.num_pages)
    return page


def index(request):
    questions = Question.objects.all().prefetch_related()
    paginated_questions = paginate(request, questions)
    return render(request, "questions/index.html", context={"questions": paginated_questions})


def hot(request):
    questions = Question.objects.hot()
    paginated_questions = paginate(request, questions)
    return render(request, "questions/index.html", context={"questions": paginated_questions})


def questions_for_tag(request, tag):
    questions = Question.objects.by_tag(tag)
    paginated_questions = paginate(request, questions)
    return render(request, "questions/index.html", context={"questions": paginated_questions})


def settings(request):
    return render(request, "questions/settings.html", context={"username": "Artur Sardaryan"})


def login(request):
    return render(request, "questions/login.html")


def register(request):
    return render(request, "questions/register.html")


def ask(request):
    return render(request, "questions/ask.html")


def question_by_pk(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "questions/question_page.html", context={"question": question})
