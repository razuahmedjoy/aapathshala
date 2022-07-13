from django.shortcuts import HttpResponse,render, redirect

def PersonalCare(request):
    return render(request,'coursesapp/care.html')