from django.shortcuts import HttpResponse, redirect,render,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import logout,login

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from coursesapp.models import Students, Settings,College
from django.contrib.auth import authenticate
from django.conf import settings

import random
import requests

# models and forms

from coursesapp.forms import RegistrationForm, LoginForm

from django.views import View

'''
class RegistrationView(FormView):
    template_name = "coursesapp/registration.html"
    form_class = RegistrationForm
    success_url = '/login'


    def form_valid(self,form):
        form.save()
        # print(user.first_name)
        # print(user.last_name)
        # print(user.email)
        
        return super().form_valid(form)
        
        '''


def CollegeList(request):
    if 'term' in request.GET:
        college = College.objects.filter(name__icontains=request.GET.get('term'))
        colleges = list()
        for clg in college:
            colleges.append(f"{clg.name}-{clg.eiin}")
        return JsonResponse(colleges, safe=False)
    else:
        return redirect('/')
        
def RegistrationView(request):
    if request.user.is_authenticated:
        return HttpResponse("Already Logged in")
    
    if request.is_ajax():
        contact_no = request.POST.get('contact_no')
        otp = random.randint(1111,9999)
            
        message = f"Your Academic Admission Pathshala OTP is {otp}"
        url = f"http://66.45.237.70/api.php?username={settings.SMS_API_USERNAME}&password={settings.SMS_API_PASSWORD}&number={contact_no}&message={message}"

        payload  = {}
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data = payload)

        return HttpResponse(otp)

    if request.method == 'POST':
        action = request.GET.get('action')
        if action == "sendotp":
            contact_no = request.POST.get('contact_no')
            fname = request.POST.get('fname')

            try:
                user = Students.objects.get(contact_no=contact_no)
                if user:
                    error = "Another student with this number already exists"
                    context = {"error": error}
                    return render(request,'coursesapp/registration.html',context)

            except:
                pass

            # number validation
            # generate otp
            otp = random.randint(1111,9999)
            
            message = f"Your Academic Admission Pathshala OTP is {otp}"
            url = f"http://66.45.237.70/api.php?username={settings.SMS_API_USERNAME}&password={settings.SMS_API_PASSWORD}&number={contact_no}&message={message}"

            payload  = {}
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request("POST", url, headers=headers, data = payload)

           

            otpsent = True
            context = {
                "contact_no":contact_no,
                'fname': fname,
                "otp" : otp,
                "otpsent" : otpsent
            }
            return render(request,'coursesapp/registration.html', context)
        
        if action == "verify":
            otp = request.POST.get('otp')
            userotp = request.POST.get('userotp')
            contact_no = request.POST.get('contact_no')
            fname = request.POST.get('fname')

            if userotp == otp:
                verify = True
                
                context = {
                    'contact_no' : contact_no,
                    'fname':fname,

                }
                return render(request,'coursesapp/registration_step2.html',context)
                
            else:
                invalidotp = True
                otpsent = True

                context = {
                "contact_no":contact_no,
                "otp" : otp,
                "otpsent" : otpsent,
                "invalidotp" : invalidotp,
                'fname': fname,
                }
                return render(request,'coursesapp/registration.html', context)

        

    if request.method == "GET":
        setting = Settings.objects.get(pk=1)
        context={
            'settings' :setting,
        }
        return render(request,'coursesapp/registration.html',context)



def CreateAccount(request):
    if request.is_ajax():
        email = request.POST.get('email')
        if email == "":
            email = None
        sscroll = request.POST.get('sscroll')
        hscroll = request.POST.get('hscroll')
        regno = request.POST.get('regno')
        try:
            userroll = Students.objects.get(sscroll=sscroll)
            userboard = userroll.sscboard
            checksscyear = userroll.sscyear
            if userboard == request.POST.get('sscboard') and checksscyear == request.POST.get('sscyear'):
                return HttpResponse("Another account exist with this sscroll,board and year")
                
        except:
            pass
        try:
            userroll = Students.objects.get(hscroll=hscroll)
            userboard = userroll.hscboard
            checkhscyear = userroll.hscyear
            if userboard == request.POST.get('hscboard') and checkhscyear == request.POST.get('hscyear'):
                return HttpResponse("Another account exist with this hscroll,board and year")
        except:
            pass
        try:
            user = Students.objects.get(regno=regno)
            if user:
                return HttpResponse("Another account exist with this regno")
        except:
            pass
                
        try:
            user = User.objects.get(email=email)
            if user:
                return HttpResponse("Another account exist with this email")
        except:
            fullname = request.POST.get('fname')

            contact_no = request.POST.get('contact_no')
            password = request.POST.get('password1')

            try:
                lastuser = Students.objects.last()
                lastroll = lastuser.aaproll
            except:
                lastroll = "AAP10000"

            idno = ""

            for c in lastroll:
                if c.isdigit():
                    idno = idno + c
            idno = int(idno) + 1

            username = "AAP" + str(idno)

            user = User.objects.create_user(username, email, password)
            user.first_name = fullname.split()[0]
            user.save()

            gender = request.POST.get('gender')
            institue = request.POST.get('institue')
            
            sscboard = request.POST.get('sscboard')
            sscyear = request.POST.get('sscyear')
            
            
            hscboard = request.POST.get('hscboard')
            hscyear = request.POST.get('hscyear')
            

            student = Students(user=user,aaproll=username,fullname=fullname,contact_no=contact_no,institue=institue,gender=gender,sscroll=sscroll,sscboard=sscboard,sscyear=sscyear,hscroll=hscroll,hscboard=hscboard,hscyear=hscyear,regno=regno)
           
            student.save()
            login(request, user)


            # Register user here
            return HttpResponse('success')
    else:
        return redirect('registration')    
            
            

    # if request.method == 'POST':
    #     contact_no = request.POST.get('contact_no')
    #     fullname = request.POST.get('fullname') 
    #     email = request.POST.get('email')
    #     pass1 = request.POST.get('password1')
    #     pass2 = request.POST.get('password2')
        
    #     try:
    #         user = User.objects.get(email=email)
    #         if user:
    #             messages.warning(request, 'Another user already exists with this email')
    #             print("user another with this mail")
    #             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #     except:
    #         return HttpResponse("done")
        


    #     # generate otp and send to number
        

    #     context = {
    #         'contact_no': contact_no,
    #     }



    #     return HttpResponse(contact_no)
    # else:
    #     return redirect('registration')


@login_required(login_url="login")
def Registerconfirm(request):
    return render(request, 'coursesapp/registerconfirm.html')


'''
class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()

        context ={
        'form': form,
        }
        return render(request,'coursesapp/registration.html', context)


    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # print(user.first_name)
            # print(user.last_name)
            # print(user.email)
            if user is not None:
                return redirect('login')
        context ={
            'form': form,
            }
        
        return render(request,'coursesapp/registration.html', context)

'''


def LoginView(request):

    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            error = "Credetial Wrong. Remember to input your roll Capital Letter"
            context = {'error': error}
            return render(request,'coursesapp/login.html', context)

        
    if request.method == 'GET':
        return render(request,'coursesapp/login.html')
    


# class LoginView(View):
#     def get(self, request):

#         form = LoginForm()
#         context = {'form': form,}
#         return render(request,'coursesapp/login.html', context)
    

#     def post(self,request):
#         form = LoginForm(request=request,data=request.POST)
#         if form.is_valid():
#             login(request, request.user)
#             return redirect("home")
        
#         context = {'form': form,}

#         return render(request,'coursesapp/login.html', context)


def logoutview(request):
    logout(request)
    return redirect("home")


def ForgotpasswordView(request):
    error = None
    otpsent = False
    if request.method == 'GET':
      
        return render(request,'coursesapp/forget_password.html')
    if request.method == 'POST':
        contact_no = request.POST.get('contact_no')
        try:
            user = Students.objects.get(contact_no=contact_no)
            if user:
                otp = random.randint(1111,9999)
                user.otp = otp
                user.save()
                
                message = f"Your Academic Admission Pathshala Forgot password OTP is {otp}"
                url = f"http://66.45.237.70/api.php?username={settings.SMS_API_USERNAME}&password={settings.SMS_API_PASSWORD}&number={contact_no}&message={message}"

                payload  = {}
                headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
                }

                response = requests.request("POST", url, headers=headers, data = payload)
                otpsent = True
                context = {
                    
                    'otpsent': otpsent,
                    'contact_no': contact_no,
                }
                return render(request,'coursesapp/forget_password.html',context)
                    
        except:
            error = "No Student Found with this number"
            context = {
                'error':error
            }
            return render(request,'coursesapp/forget_password.html',context)


def VerifyotpView(request):
    if request.method == 'POST':
        contact_no = request.POST.get('contact_no')
        otp = request.POST.get('otp')
        
        try:
            student = Students.objects.get(contact_no=contact_no)
            if student.otp == otp:
                context = {
                    'contact_no': contact_no,
                }   
                return render(request,'coursesapp/reset_password.html',context)
            else:
                otpsent = True
                context = {
                    'invalidotp':True,
                    'testotp' : otp,
                    'otpsent': otpsent,
                    'contact_no': contact_no,
                }
                return render(request,'coursesapp/forget_password.html',context)

        except:
            return redirect('login')
    else:
        return redirect('forgotpassword')

def ResetpasswordView(request):
    if request.method == 'POST':
        contact_no = request.POST.get('contact_no')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            student = Students.objects.get(contact_no=contact_no)
            user = User.objects.get(username=student.aaproll)
            user.set_password(password1)
            user.save()
            context ={
                'changedpass' : True,
            }
            return render(request,'coursesapp/login.html',context)
        else:
            return redirect('forgotpassword')
    else:
        return redirect('login')


# Forgot Roll
def ForgotrollView(request):
    if request.method == 'POST':
        contact_no = request.POST.get('contact_no')
        regno = request.POST.get('regno')
        rollsent = False
        nostudent = False
        try:
            student = Students.objects.get(contact_no=contact_no,regno=regno)
            message = f"Your Academic Admission Pathshala roll is {student.aaproll}"
            url = f"http://66.45.237.70/api.php?username={settings.SMS_API_USERNAME}&password={settings.SMS_API_PASSWORD}&number={contact_no}&message={message}"
            
            payload  = {}
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request("POST", url, headers=headers, data = payload)
            rollsent = True

        except:
            nostudent = True
        
        context = {
            'nostudent': nostudent,
            'rollsent' : rollsent,
        }
        return render(request,'coursesapp/forgot_roll.html',context)

    if request.method == 'GET':
        return render(request,'coursesapp/forgot_roll.html')
