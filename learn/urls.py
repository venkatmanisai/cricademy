from django.urls import path
from . import views

app_name = 'learn'

urlpatterns = [
    path('', views.home, name=app_name),
]