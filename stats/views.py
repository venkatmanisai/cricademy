from django.shortcuts import render
from learn.models import Course, Skill
from users.models import Profile
from tests.models import Test, Testinputs
#from django.http import HttpResponse

def stats_index(request):
	courses = Course.objects.all()
	return render(request, 'stats/stats_index.html', {'courses': courses})

def stats_course(request, course_id):
	skills = Skill.objects.filter(course=course_id)
	return render(request, 'stats/stats_course.html', {'skills': skills})


def stats_skill(request, course_id, skill_id):
	user = request.user
	tests = Test.objects.filter(user=user)
	footwork = 0
	middle = 0
	bat_position = 0
	head_position = 0
	elbow_position = 0
	shoulder_line = 0
	ball_direction = 0
	count = 0
	for test in tests:
		test_skill = test.test_skill()
		if test_skill == int(skill_id):
			testinputs = Testinputs.objects.filter(test=test)
			for testinput in testinputs:
				count += 1
				if testinput.footwork == True:
					footwork += 1
				if testinput.middle == True:
					middle += 1
				if testinput.bat_position == True:
					bat_position += 1
				if testinput.head_position == True:
					head_position += 1
				if testinput.elbow_position == True:
					elbow_position += 1
				if testinput.shoulder_line == True:
					shoulder_line += 1
				if testinput.ball_direction == True:
					ball_direction += 1
	if count != 0:
		footwork_stat = (footwork/count)*100
		middle_stat = (middle/count)*100
		bat_position_stat = (bat_position/count)*100
		head_position_stat = (head_position/count)*100
		elbow_position_stat = (elbow_position/count)*100
		shoulder_line_stat = (shoulder_line/count)*100
		ball_direction_stat = (ball_direction/count)*100
		return render(request, 'stats/stats_skill.html', {'footwork_stat': footwork_stat, 'middle_stat': middle_stat,
			'bat_position_stat': bat_position_stat, 'head_position_stat': head_position_stat, 'elbow_position_stat': elbow_position_stat,
			'shoulder_line_stat': shoulder_line_stat, 'ball_direction_stat': ball_direction_stat})
	else:
		return render(request, 'stats/stats_skill.html', {'no_data': 'No sufficient Data'})


def stats_skill_overall(request):
	return render(request, 'stats/stats_skill_overall.html')


def stats_skill_challenge(request):
	return render(request, 'stats/stats_skill_challenge.html')


