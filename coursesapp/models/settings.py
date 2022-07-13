from django.db import models
from ckeditor.fields import RichTextField

class Settings(models.Model):
    registration = models.BooleanField(default=True)
    exam_details = RichTextField(null=True,blank=True)
    hero_cover = models.ImageField(upload_to="hero_cover/",null=True,blank=True)
    
    
    def __str__(self):
        return "Website settings"