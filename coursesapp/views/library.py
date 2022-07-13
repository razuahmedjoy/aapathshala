from django.shortcuts import HttpResponse,render, redirect
from coursesapp.models import Library, Settings


def LibraryView(request):
    library = Library.objects.order_by('serial_number')
    context = {
        'library': library,
    }
    return render(request,'coursesapp/library.html',context)


def AdmissionInfoView(request):
    setting = Settings.objects.get(pk=1)
    
    context={
        'setting':setting,
    }
    return render(request,'coursesapp/admissioninfo.html',context)