from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# views
from .views import choice_track,check_eligibility,show_details,sort_student_profile_pic

urlpatterns = [

        path('',check_eligibility,name="check_eligibility"),
        path('show_details/',show_details,name="show_details"),
        path('sort/',sort_student_profile_pic,name="sort_student_profile_pic"),

   
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)