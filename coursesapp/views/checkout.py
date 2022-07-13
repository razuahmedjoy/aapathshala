from django.shortcuts import HttpResponse,render, redirect

# models
from coursesapp.models import Course, Video, Payment, UserCourse
from time import time
from datetime import datetime, date
from django.contrib.auth.decorators import login_required

from coursesapp.models.student import Students


@login_required(login_url="login")
def checkout(request,slug):

    # print(request.user.is_authenticated)

    course = Course.objects.get(slug=slug)

    

    action = request.GET.get('action')
    
    if action == "enroll-now" and (course.price == 0 or course.discount == 100):
        
        try:
            usercourse = UserCourse.objects.get(user=request.user, course=course)
            if usercourse:
                return redirect("mycourses")
        except:
            pass
        # sellprice = int(course.price - (course.price*course.discount*0.01))
        # if sellprice == 0:
        
        orderid = f"aap-{date.today()}-{int(time())}"
        payment = Payment()
        payment.user = request.user
        payment.course = course
        payment.order_id = orderid
        payment.payment_id = f"Free Course-{course.name}"
        payment.status = True

        student = Students.objects.get(user=request.user)

        userCourse = UserCourse(user = payment.user, course = payment.course, student = student)
        userCourse.save()

        payment.usercourse = userCourse
        payment.save()

        return redirect("mycourses")
         
        
        
    try:
        usercourse = UserCourse.objects.get(user= request.user, course= course)
        if usercourse:
            return redirect('mycourses')
    except:
        pass

    context = {
    'course': course,
        
    } 

    
    return render(request,"coursesapp/checkout.html", context )