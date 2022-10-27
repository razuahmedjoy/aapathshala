from django.contrib import admin

# Register your models here.
from coursesapp.models import Course, Tag, Prerequisite, Learning, Video, Section,Lecture,LiveExam,PracticeExam,CourseMaterials,CourseVideos,ExamResults, UserCourse, Payment, Library, LibraryFolders, Settings,Announcement, Routine
from coursesapp.models.student import Students,College
from import_export.admin import ImportExportModelAdmin

from coursesapp.models import JoinUs

from django.utils.html import format_html




class VideoAdmin(admin.TabularInline):
    model = Video

class SectionAdmin(admin.TabularInline):
    model = Section
    fields = ("title", "serial_number",)

class LectureAdmin(admin.TabularInline):
    model = Lecture
    
class RoutineAdmin(admin.TabularInline):
    model = Routine

# Library

class LibraryFolderAdmin(admin.TabularInline):
    model = LibraryFolders
class LibraryAdmin(admin.ModelAdmin):
    inlines = [LibraryFolderAdmin]
    list_display = ['title','collapsable','serial_number']
    list_editable = ('collapsable','serial_number',)

# Lectureitems
class LiveExamAdmin(admin.TabularInline):
    model = LiveExam
    extra = 1

class PracticeExamAdmin(admin.TabularInline):
    model = PracticeExam
    extra = 1
class CourseMaterialsAdmin(admin.TabularInline):
    model = CourseMaterials
    extra = 1
class CourseVideosAdmin(admin.TabularInline):
    model = CourseVideos
    extra = 1
class ExamResultsAdmin(admin.TabularInline):
    model = ExamResults
    extra = 1




class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionAdmin, VideoAdmin, TagAdmin,RoutineAdmin]
    list_display = ['name','running_week', 'get_price', 'get_discount','sell_price', 'active']
    list_editable = ('running_week',)

    list_filter = ("discount","active")
    save_as = True

    def get_discount(self, course):
        return f"{course.discount}%"
    def get_price(self, course):
        return f"৳ {course.price}"
    def sell_price(self, course):
        sellprice = course.price - (course.price*course.discount*.01)
        return f"৳ {int(sellprice)}"

    get_discount.short_description = "Discount"
    get_price.short_description = "Price"
    sell_price.short_description = "Sell Price"

class SectionAdmin(admin.ModelAdmin):
    inlines = [LectureAdmin ]
    list_display = ['__str__', 'course', 'serial_number']
    list_filter = ['course']
    save_as = True
    ordering = ('serial_number',)

class LectureModelAdmin(admin.ModelAdmin):
    inlines = [LiveExamAdmin,PracticeExamAdmin,CourseMaterialsAdmin,CourseVideosAdmin,ExamResultsAdmin ]
    list_display = ['title','section','get_course','serial_number']
    list_filter = ['section','section__course']
    save_as = True
    ordering = ('serial_number',)

    

    def get_course(self,lecture):
        return lecture.section.course
    get_course.short_description = "Course"


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['__str__','get_user','order_id','date','status']
    search_fields = ['user__username']
    readonly_fields=('usercourse','user','order_id','payment_id')

    def get_user(self, payment):
        return format_html(f"<a href='/secret/aapadminaap/auth/user/{payment.user.id}' target='_blank'>{payment.user}</a>")


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['__str__','user','course']
    list_filter = ['course']
    search_fields = ['user__username']
    readonly_fields=('user','student',)
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ['__str__','fullname','contact_no','sscroll','hscroll','regno','image_tag','datejoined']
    search_fields = ['aaproll', 'fullname', 'contact_no','sscroll','hscroll','regno','institue']
    readonly_fields=('user',)
    list_filter = ['has_pro_pic']

class CollegeAdmin(ImportExportModelAdmin):
    list_display = ['id','__str__','eiin']
    ordering = ('id',)
    search_fields = ['name','eiin']

class JoinUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'hsc_batch', 'department', 'your_aap_roll', 'currently_studying', 'your_free_time', 'contact', 'why_choose_us', 'status']
    search_fields = ['your_aap_roll', 'contact', 'full_name', 'hsc_batch', 'department']
    list_editable = ('status',)

admin.site.register(College,CollegeAdmin)

admin.site.register(Course, CourseAdmin)
# admin.site.register(Tag)
# admin.site.register(Prerequisite)
# admin.site.register(Learning)
# admin.site.register(Video)


admin.site.register(Section,SectionAdmin)
admin.site.register(Lecture,LectureModelAdmin)

admin.site.register(Students,StudentAdmin)
admin.site.register(UserCourse,UserCourseAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(Library,LibraryAdmin)
admin.site.register(Settings)
admin.site.register(Announcement)
admin.site.register(JoinUs, JoinUsAdmin)