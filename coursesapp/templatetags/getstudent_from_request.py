from django import template
from coursesapp.models import Students
register = template.Library()


@register.simple_tag
def getStudentFromRequest(request):
    try:
        student = Students.objects.get(user=request.user)
        return student
    except:
        return None
