from django import template
import datetime
register = template.Library()


@register.simple_tag
def getYears():
    year = datetime.datetime.today().year

    YEARS = range(year, year - 6, -1)

    return YEARS

# @register.simple_tag
# def cal_sellprice(price,discount):
#     if discount is None or discount == 0:
#         return price
#     sellprice = price
#     sellprice = price - (price*discount*0.01)
#     return  math.floor(sellprice)


# @register.simple_tag
# def is_enrolled(request,course):

#     if request.user.is_authenticated is False:
#         return False
#     try:
#         usercourse = UserCourse.objects.get(user= request.user, course= course)
#         if usercourse:
#             return True
#     except:
#         return False
