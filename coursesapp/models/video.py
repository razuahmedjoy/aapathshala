from django.db import models
from coursesapp.models import Course

class Video(models.Model):
    title = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Course, null=False, on_delete = models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_url = models.CharField(max_length=50, null=False)
    isPreview = models.BooleanField(default=False)

    def __str__(self):
        return self.title
