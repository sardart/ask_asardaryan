from django.urls import path

from questions.views import QuestionList
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("settings/", views.settings, name="settings"),
    path("login/", views.login, name="settings"),
    path("register/", views.register, name="settings"),
    path("ask/", views.ask, name="ask"),

]


