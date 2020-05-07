from django.shortcuts import render
from django.http import HttpResponse
from . models import Course, Skillcategory, Skill, Videocategory, Video, Challenge


def learn_index(request):
	courses = Course.objects.all()
	return render(request,'learn/learn.html', {'courses': courses})


def course_page(request, course_id):
	skills = Skill.objects.filter(course=course_id)
	return render(request, 'learn/course_page.html', {'skills': skills})


def skill_page(request, course_id, skill_id):
	videos = Video.objects.filter(skill=skill_id)
	return render(request, 'learn/skill_page.html', {'videos': videos})
# Create your views here.
