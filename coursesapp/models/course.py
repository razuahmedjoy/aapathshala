from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import uuid
class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    description = RichTextField(blank=True, null=True)
    price = models.IntegerField(null=False,default=0)
    discount = models.IntegerField(null=False,default=0)
    active = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="files/resource", null=True,blank=True)
    running_week = models.IntegerField(null=True,blank=True)
    examcourse = models.BooleanField(default=False)


    def __str__(self):
        return self.name


   
    def save(self, *args, **kwargs):
        # name = self.name + uuid.uuid4().hex[:10]
        if not self.slug:
            name = self.name + "-" + str(self.id)
            self.slug = slugify(name)
        super(Course, self).save(*args, **kwargs)


    class Meta:
        ordering = ('-date', )


class Routine(models.Model):
    course = models.ForeignKey(Course, null=False, on_delete = models.CASCADE)
    title = models.CharField(max_length=100,null=False)
    routinefile = models.FileField(upload_to="files/resource/routine", null=True,blank=True)
    
    def __str__(self):
        return self.title
        
        
class CourseProperty(models.Model):
    description = models.CharField(max_length=50,null=True)
    course = models.ForeignKey(Course, null=False, on_delete = models.CASCADE)

    class Meta:
        abstract = True
    

    def __str__(self):
        return self.description


class Tag(CourseProperty):
    pass


class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass
