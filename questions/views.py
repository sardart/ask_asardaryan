# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from questions.models import Question


class QuestionList(ListView):
    model = Question
    paginate_by = 1



def paginate(request, objects):
    pag = Paginator(objects, 20)
    try:
        page = pag.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        page = pag.get_page(1)
    except EmptyPage:
        page = pag.get_page(pag.num_pages)
    return page



def index(request):
    # fakeDataManager = FakeDataManager()
    # questions = fakeDataManager.generate_questions()
    questions = Question.objects.all().prefetch_related()
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