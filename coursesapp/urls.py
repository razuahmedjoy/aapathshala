from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# views
from coursesapp.views import HomepageView,coursePage, RegistrationView, LoginView, logoutview, checkout, myCourses,remove_course, CreateAccount, testview,Registerconfirm,Profile,ProfileUpdate,ForgotpasswordView,VerifyotpView,ResetpasswordView,ForgotrollView,LibraryView,AdmissionInfoView,PersonalCare,exportstudents,ProfilePicUpdate,export_as_course,CollegeList

from coursesapp.views import join_us

urlpatterns = [
    
    path('', HomepageView.as_view(), name="home" ),
    path('registration/', RegistrationView, name="registration" ),
    path('createaccount/', CreateAccount, name="createaccount" ),
    path('college/', CollegeList, name="collegelist" ),
    
    path('registerconfirm/', Registerconfirm, name="registerconfirm" ),
    path('login/', LoginView, name="login" ),
    path('logout/', logoutview, name="logout" ),
    path('library/', LibraryView, name="library" ),
    path('admission-info/', AdmissionInfoView, name="admissioninfo" ),
    path('personal-care/', PersonalCare, name="personalcare" ),

    #join us 
    path('join-us/', join_us, name="join_us")
,    
    # forgot password
    path('forgot-pass/', ForgotpasswordView, name="forgotpassword" ),
    path('verifyotp/', VerifyotpView, name="verifyotp" ),
    path('resetpassword/', ResetpasswordView, name="resetpassword" ),
    

    # forgot roll
    path('forgotroll/', ForgotrollView, name="forgotroll" ),

    # testview
    path('test/', testview, name="test" ),


    # user profile urls
    
    path('profile/', Profile, name="profile" ),
    path('profile/update', ProfileUpdate, name="profileupdate" ),
    path('profile/change_pro_pic', ProfilePicUpdate, name="profilepicupdate" ),
    path('course/<str:slug>', coursePage, name="coursepage" ),
    path('checkout/<str:slug>', checkout, name="checkout" ),

    path('my-courses/', myCourses.as_view(), name="mycourses" ),
    path('remove-course/', remove_course, name="removecourse" ),

    # Admin views
    path('export/students', exportstudents, name="exportstudents" ),
    path('export/ascourse/<int:id>', export_as_course, name="export_as_course" ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)