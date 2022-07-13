from django.db import models
from coursesapp.models import Course
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import os
from PIL import Image
from django.conf import settings

class Students(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    BOARD = (
        ('Barisal','Barisal'),
        ('Chittagong','Chittagong'),
        ('Comilla','Comilla'),
        ('Dhaka','Dhaka'),
        ('Dinajpur','Dinajpur'),
        ('Jessore','Jessore'),
        ('Madrasah','Madrasah'),
        ('Rajshahi','Rajshahi'),
        ('Sylhet','Sylhet'),
        ('Mymensingh','Mymensingh'),
        ('Technical','Technical'),
    )

    def user_profile_pic(instance,filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.aaproll, ext)
        
        full_path = os.path.join(settings.MEDIA_ROOT,filename)
        if os.path.exists(full_path):
            os.remove(full_path)
            
        return os.path.join('users/profile_pic',filename)

    user = models.ForeignKey(User, null=False, on_delete = models.CASCADE)
    aaproll = models.CharField(max_length=100,unique=True)
    fullname = models.CharField(max_length=100,null=True,blank=True)
    contact_no = models.CharField(max_length=15, null=False, blank=False,unique=True)
    institue = models.CharField(max_length=100, blank=True,null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    datejoined = models.DateField(auto_now_add=True)
    sscroll = models.CharField(max_length=20, blank=True, null=True)
    sscboard = models.CharField(max_length=20, blank=True, choices=BOARD)
    sscyear = models.CharField(max_length=5, blank=True,null=True)
    hscroll = models.CharField(max_length=20, blank=True, null=True)
    hscboard = models.CharField(max_length=20, blank=True, choices=BOARD)
    hscyear = models.CharField(max_length=5, blank=True, null=True)
    regno = models.CharField(max_length=20, blank=True, null=True)
    otp = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True,upload_to=user_profile_pic)
    has_pro_pic = models.BooleanField(default=False)

    def __str__(self):
        return self.aaproll
    
    def image_tag(self):
        if self.profile_pic:
            return mark_safe(f'<img src="{self.profile_pic.url}" style="width: 45px; height:45px; border-radius:50%;" />')
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        SIZE = 600, 600

        if self.profile_pic:
            pic = Image.open(self.profile_pic.path)
            pic.thumbnail(SIZE,Image.LANCZOS)
            pic.save(self.profile_pic.path)


class College(models.Model):
    name = models.CharField(max_length=250)
    eiin = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} [{self.eiin}]"