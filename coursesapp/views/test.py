from django.shortcuts import HttpResponse, redirect,render,HttpResponseRedirect
from django.contrib.auth import logout,login
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from coursesapp.models import Students, Course, Video, UserCourse

from django.contrib import messages
import random
import datetime
import uuid
# models and forms

from coursesapp.forms import RegistrationForm, LoginForm

from django.views import View



def testview(request):

    return HttpResponse("test")