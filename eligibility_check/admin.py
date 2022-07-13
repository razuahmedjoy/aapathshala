from django.contrib import admin

# Register your models here.
from .models import medical,engineering,versity,unitChange,admissionSystemOverview,admissionDetailsInfo,eligibilityCheckerControl,AdmissionApplication

class medicalAdmin(admin.ModelAdmin):
    list_display = ['name','ssc_gpa','hsc_gpa','hsc_bio_gpa','total_gpa']
    list_editable = ('ssc_gpa','hsc_gpa','hsc_bio_gpa','total_gpa',)



class engineeringAdmin(admin.ModelAdmin):
    list_display = ['name','ssc_gpa','hsc_gpa','physics_gpa','chemistry_gpa','hmath_gpa','english_gpa','subject_total_gpa']
    list_editable = ('ssc_gpa','hsc_gpa','physics_gpa','chemistry_gpa','hmath_gpa','english_gpa','subject_total_gpa',)

class versityAdmin(admin.ModelAdmin):
    list_display = ['name','ssc_gpa','hsc_gpa','total_gpa']
class unitChangeAdmin(admin.ModelAdmin):
    list_display = ['name','ssc_gpa','hsc_gpa','total_gpa']

class eligibilityCheckerControlAdmin(admin.ModelAdmin):
    list_display = ['__str__','on']
    
admin.site.register(medical,medicalAdmin)
admin.site.register(engineering,engineeringAdmin)
admin.site.register(versity,versityAdmin)
admin.site.register(unitChange,unitChangeAdmin)
admin.site.register(admissionSystemOverview)
admin.site.register(admissionDetailsInfo)
admin.site.register(eligibilityCheckerControl,eligibilityCheckerControlAdmin)
admin.site.register(AdmissionApplication)