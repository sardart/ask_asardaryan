from django.urls import path

from questions.views import QuestionList
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hot/", views.hot, name="hot"),
    path("tag/<str:tag>/", views.questions_for_tag, name="tag"),
    path("settings/", views.settings, name="settings"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("ask/", views.ask, name="ask"),
    path("question/<int:pk>/", views.question_by_pk, name="question"),

]


