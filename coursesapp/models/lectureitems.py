from django.db import models

from coursesapp.models import Course, Section, Lecture

class LiveExam(models.Model):
    title = models.CharField(max_length=100,null=False)
    lecture = models.ForeignKey(Lecture, null=True, on_delete = models.SET_NULL)
    examurl = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_time = models.DateTimeField(null=True, blank=True)
    serial_number = models.IntegerField(null=True, blank=True)
    single_row = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PracticeExam(models.Model):
    title = models.CharField(max_length=100,null=False)
    lecture = models.ForeignKey(Lecture, null=True, on_delete = models.SET_NULL)
    examurl = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CourseMaterials(models.Model):
    title = models.CharField(max_length=100,null=False)
    lecture = models.ForeignKey(Lecture, null=True, on_delete = models.SET_NULL)
    url = models.CharField(max_length=250,null=True, blank=True)
    serial_number = models.IntegerField(null=True, blank=True)
    single_row = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CourseVideos(models.Model):
    title = models.CharField(max_length=100,null=False)
    lecture = models.ForeignKey(Lecture, null=True, on_delete = models.SET_NULL)
    url = models.CharField(max_length=250,null=True, blank=True)
    serial_number = models.IntegerField(null=True, blank=True)
    single_row = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        
class ExamResults(models.Model):
    
    def upload_as_lecture_name(instance,filename):
        return 'files/resource/%s/%s/%s' % (instance.lecture.section.course.name,instance.lecture.section.title, filename)
        
    title = models.CharField(max_length=100,null=False)
    lecture = models.ForeignKey(Lecture, null=True, on_delete = models.SET_NULL)

    pdf = models.FileField(upload_to=upload_as_lecture_name, null=True,blank=True,max_length=255)

    def __str__(self):
        return self.title
