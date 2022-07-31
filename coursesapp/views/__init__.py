from coursesapp.views.homepage import HomepageView
from coursesapp.views.courses import coursePage, myCourses,remove_course
from coursesapp.views.library import LibraryView,AdmissionInfoView
from coursesapp.views.auth import RegistrationView, LoginView, logoutview, CreateAccount, Registerconfirm,ForgotpasswordView,VerifyotpView,ResetpasswordView,ForgotrollView,CollegeList
from coursesapp.views.checkout import checkout

from coursesapp.views.profile import Profile,ProfileUpdate,ProfilePicUpdate
from coursesapp.views.care import PersonalCare
from coursesapp.views.test import testview
from coursesapp.views.export import exportstudents,export_as_course
from coursesapp.views.join_us_view import join_us