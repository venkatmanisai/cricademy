from django.contrib import admin
from . models import Course, Skillcategory, Skill, Videocategory, Video, Challenge


admin.site.register(Course)
admin.site.register(Skillcategory)
admin.site.register(Skill)
admin.site.register(Videocategory)
admin.site.register(Video)
admin.site.register(Challenge)

