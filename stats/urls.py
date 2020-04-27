from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.stats_index, name='stats_index'),
    path('course_stats', views.stats_course, name='stats_course'),
    path('skill_stats', views.stats_skill, name='stats_skill'),
    path('skill_overall_stats', views.stats_skill_overall, name='stats_skill_overall'),
    path('skill_challenge_stats', views.stats_skill_challenge, name='stats_skill_challenge'),
]