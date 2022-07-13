from time import strftime
from django import template
from datetime import datetime, timedelta
from django.utils import formats
register = template.Library()

@register.simple_tag
def get_date_range(start_date,end_date):
    if start_date is None and end_date is None:
        return f"-"
    if end_date is None:
        return f"{start_date.strftime('%d %b')} -"
    else:
        start_date = start_date.strftime("%d %b")
        end_date = end_date.strftime("%d %b")
        return f"{start_date} - {end_date}"
@register.simple_tag
def get_time_left(end_date,start_date):
    if end_date is not None and start_date is not None:
        today = datetime.now()
        if today < start_date:
            return ""
        else:
            time_left = end_date - today
            if end_date > today:
                time_left = f"{time_left.days}Days {time_left.seconds//3600}H"
                return time_left
            else:
                return "End"
                
    if end_date is None:
        return f"-"
    if end_date is not None and start_date is None:
       today = datetime.now()
    #   print(end_date)
       time_left = end_date - today
       if end_date > today:
           time_left = f"{time_left.days}Days {time_left.seconds//3600}H"
           return time_left
       else:
            return "End"