from django import template
register = template.Library()
import decimal
@register.simple_tag
def your_gpa_marks(ssc_gpa,hsc_gpa,ssc_multipy,hsc_multipy):
    total = round((5*ssc_multipy)+(5*hsc_multipy))
    user = round((decimal.Decimal(ssc_gpa)*decimal.Decimal(ssc_multipy))+(decimal.Decimal(hsc_gpa)*decimal.Decimal(hsc_multipy)),1)
    return  f"{user}/{total}"
