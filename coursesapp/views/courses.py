from django.shortcuts import HttpResponse,render, redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
# models
from coursesapp.models import Course, Video, UserCourse, Section, Lecture, LiveExam, PracticeExam, CourseMaterials, CourseVideos

@method_decorator(login_required(login_url="login"),name="dispatch")
class myCourses(ListView):
    template_name = "coursesapp/my-courses.html"
    context_object_name = 'usercourses'

    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)


'''
@login_required(login_url="login")
def myCourses(request):
    user = request.user
    usercourses = UserCourse.objects.filter(user=user)
    print(usercourses)
    context={
        'usercourses' : usercourses,
    }
    return render(request, 'coursesapp/my-courses.html', context)

'''


@login_required(login_url="login")
def remove_course(request):
    if request.method == "POST":
        usercourseid = request.POST.getlist('usercourse')
        if usercourseid:
            # print(usercourseid)
            for id in usercourseid:
                UserCourse.objects.filter(id=id).delete()
            return redirect('mycourses')
        prev = request.META.get('HTTP_REFERER')
        # print(prev)
        return HttpResponseRedirect(prev)
    if request.method == "GET":
        courses = UserCourse.objects.filter(user=request.user)
        context = {
            'courses':courses,
        }
        return render(request,'coursesapp/removecourse.html',context)


def coursePage(request,slug):

    # print(request.user.is_authenticated)
    course = Course.objects.get(slug=slug)
    exam = None
    week = None
    cmaterials = None
    vmaterials = None
    try:
        video = course.video_set.first()
        # print(video)
    except:
        video = None

    sections = course.section_set.all().order_by("serial_number")

    if request.method == 'GET' and 'week' in request.GET:
        try:
            
            week = request.GET.get('week')
            week = Section.objects.get(pk=week)
            
        except:
            return redirect("checkout", slug=course.slug)

        

    if "exam" and "id" in request.GET:
        try:
            usercourse = UserCourse.objects.get(user=request.user,course=course)
            examtype = request.GET.get('exam')
            if examtype == "live":
                exam = LiveExam.objects.get(pk=request.GET.get('id'))
            if examtype == "practice":
                exam = PracticeExam.objects.get(pk=request.GET.get('id'))
        except:
            return redirect('checkout', slug=course.slug)

    if 'embaded' and 'id' in request.GET:
        try:
            usercourse = UserCourse.objects.get(user=request.user, course=course)
            embaded = request.GET.get('embaded')
            if embaded == "cmaterials":
                cmaterials = CourseMaterials.objects.get(pk=request.GET.get('id'))
            if embaded == "coursevideos":
                vmaterials = CourseVideos.objects.get(pk=request.GET.get('id'))
        except:
            return redirect('checkout', slug=course.slug)
        
    
    
    
    quiz_id = request.GET.get('quiz')
    section_id = request.GET.get('section')    
    # print("HI")  
    try:
        # quiz = Quiz.objects.get(id=quiz_id,section=section_id)
        current_section = Section.objects.get(id=section_id)
        # print(current_section)
        try:
            usercourse = UserCourse.objects.get(user=request.user, course=course)
            
        except:
            return redirect("checkout", slug=course.slug)
    except:
        quiz = None
        current_section = None
        
    

    

    context = {
        'course': course,
        'quiz': quiz,
        'video':video,
        'sections': sections,
        'current_section' : current_section,
        'week': week,
        'exam':exam,
        'cmaterials': cmaterials,
        'vmaterials': vmaterials,
        
        
    }   

    
    return render(request,"coursesapp/course_page.html", context )