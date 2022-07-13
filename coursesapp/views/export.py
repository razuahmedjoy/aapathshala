from django.shortcuts import HttpResponse, redirect,render,HttpResponseRedirect
from coursesapp.models import Students,UserCourse
from django.contrib.auth.decorators import user_passes_test
import csv

def exportstudents(request):
    if request.user.is_staff:
        response = HttpResponse(content_type='text/csv')
        
        writer = csv.writer(response)
        writer.writerow(['aaproll','contact no','hsc year'])
        
        for student in Students.objects.all().values_list('aaproll','contact_no','hscyear'):
            writer.writerow(student)
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        return response
    else:
        return redirect('home')

def export_as_course(request,id):
    if request.user.is_staff:
        response = HttpResponse(content_type='text/csv')
        
        writer = csv.writer(response)
        writer.writerow(['aaproll','contact no','date','course'])
        
        for student in UserCourse.objects.filter(course__id=id).values_list('user__username','student__contact_no','date','course'):
            writer.writerow(student)
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        return response
    else:
        return redirect('home')