from django.db import models
from coursesapp.models import Course
from ckeditor.fields import RichTextField


class Section(models.Model):
    title = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Course, null=False, on_delete = models.CASCADE)
    serial_number = models.IntegerField(null=False)
    direction = RichTextField(null=True,blank=True)

    def __str__(self):
        return (str(self.id)+"--"+self.title + " - " +str(self.course))
