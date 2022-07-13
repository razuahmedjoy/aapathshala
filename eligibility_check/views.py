from django.shortcuts import render,HttpResponse
from .forms import medical_info_form,engineering_info_form
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.views.decorators.csrf import csrf_exempt
from itertools import chain
from .models import medical,engineering,versity,unitChange,admissionSystemOverview,admissionDetailsInfo,eligibilityCheckerControl,AdmissionApplication
from coursesapp.models import Students
# Create your views here.

def choice_track(request):
    return render(request, 'eligibility/choice_track.html')

def sort_student_profile_pic(request):
    
    # Students.objects.filter(profile_pic__isnull=False).exclude(profile_pic='').update(has_pro_pic=True)
    students = Students.objects.filter(profile_pic__isnull=False).exclude(profile_pic='')
    # students = Students.objects.filter(profile_pic__isnull=False)
    pro_pic_students = Students.objects.filter(has_pro_pic=True)
    count1 = students.count()
    count2 = pro_pic_students.count()
    context = {'students':students,
    'pro_pic_students':pro_pic_students,
    'count1':count1,
    'count2':count2,
        
    }
    return render(request,"eligibility/choice_track.html",context)
    

def check_eligibility(request):
    form1 = medical_info_form(request.POST or None)
    form2 = engineering_info_form(request.POST or None)
    if request.method == 'GET':
        admsysover = admissionSystemOverview.objects.all()
        # print(admsysover)
        admissiondetailsinfo = admissionDetailsInfo.objects.all()
        # print(admissiondetailsinfo)
        eligibity_checker = eligibilityCheckerControl.objects.last()
        admission_exams = AdmissionApplication.objects.all()
        

        context ={
            'form1': form1,
            'form2': form2,
            'admsysover': admsysover,
            'admissiondetailsinfo':admissiondetailsinfo,
            'eligibity_checker':eligibity_checker,
            'admission_exams':admission_exams,
        }
        return render(request, 'eligibility/get_info.html',context)
    
    if request.is_ajax():
        if form1.is_valid() and form2.is_valid():
            ssc_gpa = form1.cleaned_data.get('ssc_gpa')
            hsc_gpa = form1.cleaned_data.get('hsc_gpa')
            
            hsc_bio_gpa = form1.cleaned_data.get('hsc_bio_gpa')
            total_gpa = ssc_gpa+hsc_gpa
            physics_gpa = form2.cleaned_data.get('physics_gpa')
            chemistry_gpa = form2.cleaned_data.get('chemistry_gpa')
            hmath_gpa = form2.cleaned_data.get('hmath_gpa')
            english_gpa = form2.cleaned_data.get('english_gpa')
            allow_second_time = form2.cleaned_data.get('allow_second_time')
            subject_total_gpa = physics_gpa+chemistry_gpa+hmath_gpa+english_gpa

            # print(total_gpa)

            medical_clg = medical.objects.filter(ssc_gpa__lte = ssc_gpa).filter(hsc_gpa__lte = hsc_gpa).filter(hsc_bio_gpa__lte = hsc_bio_gpa).filter(total_gpa__lte = total_gpa)

            engineering_clg = engineering.objects.filter(ssc_gpa__lte = ssc_gpa).filter(hsc_gpa__lte = hsc_gpa).filter(physics_gpa__lte = physics_gpa).filter(chemistry_gpa__lte = chemistry_gpa).filter(hmath_gpa__lte = hmath_gpa).filter(english_gpa__lte = english_gpa).filter(subject_total_gpa__lte = subject_total_gpa)


            versity_clg = versity.objects.filter(ssc_gpa__lte = ssc_gpa).filter(hsc_gpa__lte = hsc_gpa).filter(total_gpa__lte=total_gpa)
            
            unitChange_clg = unitChange.objects.filter(ssc_gpa__lte = ssc_gpa).filter(hsc_gpa__lte = hsc_gpa).filter(total_gpa__lte=total_gpa)

            
            if allow_second_time:
                medical_clg = medical_clg.filter(allow_second_time = allow_second_time)
                engineering_clg = engineering_clg.filter(allow_second_time = allow_second_time)
                versity_clg = versity_clg.filter(allow_second_time = allow_second_time)
                unitChange_clg = unitChange_clg.filter(allow_second_time = allow_second_time)

            def get_total_sit(clgs):
                sit = 0
                for clg in clgs:
                    if clg.total_sit:
                        sit = sit+clg.total_sit
                return sit
            
            
            def get_total_exam(clgs):
                exam = 0
                for clg in clgs:
                    if clg.exam_value:
                        exam = exam + clg.exam_value
                return exam
            total_sit_for_you = get_total_sit(medical_clg) + get_total_sit(engineering_clg) + get_total_sit(versity_clg) + get_total_sit(unitChange_clg)
            total_exam_for_you = get_total_exam(medical_clg) + get_total_exam(engineering_clg) + get_total_exam(versity_clg)
            
            unit_change_total_xm = get_total_exam(unitChange_clg)
            unit_change_total_sit = get_total_sit(unitChange_clg)
            


            # print(medical_clg)
            # print(engineering_clg)
            # print(versity_clg)
            ssc_gpa = float(ssc_gpa)
            hsc_gpa = float(hsc_gpa)

            all_clgs = list(chain(medical_clg, versity_clg,unitChange_clg))
            # print(type(all_clgs))
            # print(all_clgs)

            all_clgs_with_gpa = [i for i in all_clgs if i.ssc_gpa_multiply and i.hsc_gpa_multiply]
            # print(all_clgs_with_gpa)
            gst = False 
            for clg in all_clgs_with_gpa:
                if clg.name == "GST A":
                    gst = True
                    all_clgs_with_gpa.remove(clg)
            # print(all_clgs_with_gpa)

            result_box = render_to_string('eligibility/result-table.html',context={'medical':medical_clg,'engineering':engineering_clg,'versity':versity_clg,'unitChange':unitChange_clg,'total_sit_for_you':total_sit_for_you,'total_exam_for_you':total_exam_for_you,'unit_change_total_xm':unit_change_total_xm,'unit_change_total_sit':unit_change_total_sit,'ssc_gpa':ssc_gpa,'hsc_gpa':hsc_gpa,'all_clgs_with_gpa':all_clgs_with_gpa,'gst':gst})

            # print(result_box)

            return JsonResponse({'data':'ok','result_box':result_box})
        else:
            # print(form.errors.as_ul())
            return JsonResponse({"errormsg": form1.errors.as_ul(),"error":True})




@csrf_exempt
def show_details(request):
    
    if request.is_ajax():
        id = request.POST.get('id')
        model = request.POST.get('model')

        if model == 'medical':
            clg = medical.objects.get(id=id)
        elif model == 'engineering':
            clg = engineering.objects.get(id=id)
        elif model == 'versity':
            clg = versity.objects.get(id=id)
        elif model == 'unitChange':
            clg = unitChange.objects.get(id=id)
        else:
            clg = None

        details = render_to_string('eligibility/details.html',context={'clg':clg})

        
       
       
        

        return JsonResponse({'data':'ok','details':details})


    return redirect('/')