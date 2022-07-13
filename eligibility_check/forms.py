from dataclasses import fields
from django import forms
from django.forms import DateField
from django.contrib.auth.models import User

from .models import medical,engineering

class medical_info_form(forms.ModelForm):
    
    class Meta:
        model = medical
        exclude = ('name','total_gpa','ssc_bio_gpa','exam_value','details_info','total_sit','application_link')
        labels = {
            'ssc_gpa': ('SSC GPA'),
            'hsc_gpa' : ('HSC GPA'),
         
            'hsc_bio_gpa' : ('HSC Biology'),
            
        }

class engineering_info_form(forms.ModelForm):
    
    class Meta:
        model = engineering
        exclude = ('name','ssc_gpa','hsc_gpa','total_gpa','subject_total_gpa','extra_condition','exam_value','details_info','total_sit','application_link')
        labels = {
            'physics_gpa': ('HSC Physics'),
            'chemistry_gpa' : ('HSC Chemistry'),
            'hmath_gpa' : ('HSC H.Math'),
         
            'english_gpa' : ('HSC English'),
            
        }