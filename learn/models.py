from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.course_name


class Skillcategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    skillcategory_name = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.skillcategory_name


class Skill(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Skillcategory, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    skill_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.skill_name


class Videocategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    videocategory_name = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.videocategory_name


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    skill_category = models.ForeignKey(Skillcategory, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    category = models.ForeignKey(Videocategory, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=100)
    video = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.video_name


class Challenge(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    challenge_name = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.challenge_name



