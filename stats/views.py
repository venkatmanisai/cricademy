from django.shortcuts import render
from learn.models import Course
#from django.http import HttpResponse

def stats_index(request):
	courses = Course.objects.all()
	return render(request, 'stats/stats_index.html', {'courses': courses})

def stats_course(request):
	return render(request, 'stats/stats_course.html')


def stats_skill(request):
	return render(request, 'stats/stats_skill.html')


def stats_skill_overall(request):
	return render(request, 'stats/stats_skill_overall.html')


def stats_skill_challenge(request):
	return render(request, 'stats/stats_skill_challenge.html')


