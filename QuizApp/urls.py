from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from QuizApp import views
from .views import *
import QuizApp
app_name ="QuizApp"

urlpatterns = [
    path('', views.home, name="home"),
    path('api/get-quiz/', views.get_quiz, name="get_quiz"),
    path('quiz/',views.quiz,name="quiz")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
















