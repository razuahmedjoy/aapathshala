from django import forms
import datetime
from coursesapp.models import Students


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Students
        exclude = ('user','contact_no','regno','aaproll','birth_date','otp','sscroll','hscroll','regno','profile_pic','has_pro_pic')
        labels = {
            'fullname': ('Enter Full Name'),
            'sscboard' : ('SSC BOARD'),
            'sscyear' : ('SSC YEAR'),
            'hscboard' : ('HSC BOARD'),
            'hscyear' : ('HSC YEAR'),
        }

class ProfilePicUpdateForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('profile_pic',)
        labels = {
            'profile_pic': ('Change Profile Picture')
        }