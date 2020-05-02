from django.urls import path
from . import views

app_name = 'learn'

urlpatterns = [
    path('', views.index, name=app_name),
    path('<course_id>/', views.course_page, name='course_page'),
    path('<course_id>/<skill_id>/', views.skill_page, name='skill_page'),
]