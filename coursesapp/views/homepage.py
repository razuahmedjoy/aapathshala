from django.db.models import query
from django.shortcuts import HttpResponse,render
from django.views.generic import ListView
# models
from coursesapp.models import Course,Settings
from barta.models import Singlenotice
from eligibility_check.models import eligibilityCheckerControl



class HomepageView(ListView):
    template_name = 'coursesapp/home.html'
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['eligibity_checker'] = eligibilityCheckerControl.objects.last()
        context['single_notice'] = Singlenotice.objects.all().order_by('-id')[:10]
        context['web_settings'] = Settings.objects.last()
        return context
'''
def home(request):
    courses = Course.objects.all()
    context ={
        'courses' : courses,
    }
    return render(request,"coursesapp/home.html", context)

'''