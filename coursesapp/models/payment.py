from django.db import models
from coursesapp.models import UserCourse, Course
from django.contrib.auth.models import User

class Payment(models.Model):
    order_id = models.CharField(max_length=100,null=False)
    payment_id = models.CharField(max_length=100, null=True)
    usercourse = models.ForeignKey(UserCourse,null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.user.username}- {self.course.name}"
