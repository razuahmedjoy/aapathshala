from django.shortcuts import HttpResponse,render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
# models
from coursesapp.models import Course, Video, UserCourse, Students,Announcement

# Forms
from .forms import ProfileUpdateForm,ProfilePicUpdateForm


@login_required(login_url="login")
def Profile(request):
    
    try:
        student = Students.objects.get(user=request.user)
    except:
        student = None
    
    if student is None:
        return redirect('login')
    
    usercourses = UserCourse.objects.filter(student=student)
    announcement = Announcement.objects.last()
    context ={
        'student' : student,
        'usercourses' : usercourses,
        'announcement':announcement,
    }
    return render(request,"coursesapp/profile.html",context)

@login_required(login_url="login")
def ProfileUpdate(request):
    current_user = Students.objects.get(user=request.user)
    form = ProfileUpdateForm(instance = current_user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=current_user)
        if form.is_valid():
            contact_no = form.cleaned_data.get("contact_no")

            
            # validations


            form.save()
            form = ProfileUpdateForm(instance=current_user)
            return redirect('profile')
           


    context = {
        'form' : form,
    }

    return render(request,'coursesapp/profileupdate.html',context)
    

# profile picture update form

@login_required(login_url="login")
def ProfilePicUpdate(request):
    current_user = Students.objects.get(user=request.user)
    form = ProfilePicUpdateForm(instance = current_user)

    if request.method == "POST":
        form = ProfilePicUpdateForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():    
            # validations


            form.save()
            form = ProfilePicUpdateForm(instance=current_user)
            return redirect('profile')
           


    context = {
        'form' : form,
    }

    return render(request,'coursesapp/profilepicupdate.html',context)