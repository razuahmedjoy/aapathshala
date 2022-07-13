from django.db import models
from ckeditor.fields import RichTextField


class Announcement(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = RichTextField()
    created_At = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title