from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_home, name='chatbot_home'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
]
