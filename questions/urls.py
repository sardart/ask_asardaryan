from django.urls import path

from questions.views import questions_detail, QuestionList
from . import views

urlpatterns = [
    path('hot/', views.questions_list, name='questions_list'),
    path('<int:question_id>/', questions_detail, name='questions_detail'),
]


