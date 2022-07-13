from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from django.utils.text import slugify
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe


from colorfield.fields import ColorField

# Create your models here.


class Categorys(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = self.name
            self.slug = slugify(slug_str, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Bartas(models.Model):
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    cover_picture = models.ImageField(upload_to="files/barta/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    seo_description = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title

    def cover_image(self):
         return mark_safe(f'<img src="{self.cover_picture.url}" width="90" height="60" />')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            id = str(self.id)
            slug_str = f"{self.title}-{id}"
            self.slug = slugify(slug_str, allow_unicode=True)
        if not self.seo_description:
            desc = strip_tags(self.description)
            truncated_text = desc[:80]
            self.seo_description = truncated_text
        return super().save(*args, **kwargs)
        
        
class Singlenotice(models.Model):
    title = RichTextField()
    text_color = ColorField(default='#fff')
    background_color = ColorField(default="#870af5")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return mark_safe(self.title)