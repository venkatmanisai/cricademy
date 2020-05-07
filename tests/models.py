from django.db import models
from learn.models import Course, Skillcategory, Skill, Challenge
#from users.models import Profile
from django.conf import settings


class Testcreation(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	skill_category = models.ForeignKey(Skillcategory, on_delete=models.CASCADE, null=True, blank=True)
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)
	challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=True, blank=True)
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
	speed = models.CharField(max_length=7, choices=speed_choices, null=True, blank=True)
	L1 = "Level-1"
	L2 = "Level-2"
	L3 = "Level-3"
	level_choices = (
		(L1, "Level-1"),
		(L2, "Level-2"),
		(L3, "Level-3"),
	)
	level = models.CharField(max_length=7, choices=level_choices, null=True, blank=True)

	def __str__(self):
		return '{self.course} - {self.skill_category} - {self.skill} - {self.challenge} - {self.speed} - {self.level}'.format(self=self)


class Test(models.Model):
	test = models.ForeignKey(Testcreation, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	time = models.DateTimeField()
	active = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return '{self.user} - {self.time} - {self.test}'.format(self=self)

	def test_skill(self):
		test = self.test
		skill = test.skill.id
		return skill


class Testinputs(models.Model):
	test = models.ForeignKey(Test, on_delete=models.CASCADE)
	ball_count = models.PositiveSmallIntegerField()
	footwork = models.BooleanField(null=True, blank=True)
	middle = models.BooleanField(null=True, blank=True)
	bat_position = models.BooleanField(null=True, blank=True)
	head_position = models.BooleanField(null=True, blank=True)
	elbow_position = models.BooleanField(null=True, blank=True)
	shoulder_line = models.BooleanField(null=True, blank=True)
	ball_direction = models.BooleanField(null=True, blank=True)

	def __str__(self):
		return '{self.test} - {self.ball_count}'.format(self=self)







	










