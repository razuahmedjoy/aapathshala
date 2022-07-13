from django.db import models
from coursesapp.models import Course, Section
from ckeditor.fields import RichTextField

class Lecture(models.Model):
    title = models.CharField(max_length=100,null=False)
    section = models.ForeignKey(Section, null=True, on_delete = models.SET_NULL)
    serial_number = models.IntegerField(null=True, blank=True)
    qns = models.CharField(max_length=100,null=True,blank=True)
    result = models.FileField(upload_to="files/resource/course_result", null=True,blank=True)
    lecture_notice = RichTextField(null=True,blank=True)

    def __str__(self):
        return self.title
