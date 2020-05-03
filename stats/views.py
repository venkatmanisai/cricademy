from django.shortcuts import render
from learn.models import Course, Skill
#from django.http import HttpResponse

def stats_index(request):
	courses = Course.objects.all()
	return render(request, 'stats/stats_index.html', {'courses': courses})

def stats_course(request, course_id):
	skills = Skill.objects.filter(course=course_id)
	return render(request, 'stats/stats_course.html', {'skills': skills})


def stats_skill(request, course_id, skill_id):
	return render(request, 'stats/stats_skill.html')


def stats_skill_overall(request):
	return render(request, 'stats/stats_skill_overall.html')


def stats_skill_challenge(request):
	return render(request, 'stats/stats_skill_challenge.html')


