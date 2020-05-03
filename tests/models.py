from django.db import models
from learn.models import Course, Skillcategory, Skill, Challenge


class Testcreation(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	skill_category = models.ForeignKey(Skillcategory, on_delete=models.CASCADE, null=True)
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
	challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=True)
	S1 = "71-80"
	S2 = "81-90"
	S3 = "91-100"
	SPIN = "71-100"
	MP1 = "101-110"
	MP2 = "111-120"
	MP3 = "121-130"
	MPACE = "101-130"
	P1 = "131-140"
	P2 = "141-150"
	P3 = "151-160"
	PACE = "131-160"
	speed_choices = (
		(S1, '71-80'),
		(S1, '81-90'),
		(S1, '91-100'),
		(SPIN, "71-100"),
		(P1, '101-110'),
		(P2, '111-120'),
		(P3, '121-130'),
		(MPACE, "101-130"),
		(P1, '131-140'),
		(P2, '141-150'),
		(P3, '151-160'),
		(PACE, "131-160"),
	)
	speed = models.CharField(max_length=7, choices=speed_choices, null=True)
	L1 = "Level-1"
	L2 = "Level-2"
	L3 = "Level-3"
	level_choices = (
		(L1, "Level-1"),
		(L2, "Level-2"),
		(L3, "Level-3"),
	)
	level = models.CharField(max_length=7, choices=level_choices, null=True)


class Test(models.Model):
	test = models.ForeignKey(Testcreation, on_delete=models.CASCADE)
	time = models.DateTimeField()


class Testinputs(models.Model):
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	footwork = models.BooleanField()
	middle = models.BooleanField()
	bat_position = models.BooleanField()
	head_position = models.BooleanField()
	elbow_position = models.BooleanField()
	shoulder_line = models.BooleanField()
	ball_direction = models.BooleanField()










