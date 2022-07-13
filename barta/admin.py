from django.contrib import admin
from barta.models import Bartas,Categorys,Singlenotice
# Register your models here.


class BartaAdmin(admin.ModelAdmin):
    list_display = ['__str__','category','cover_image','created_at','slug']
    read_only_fields = ('slug',)
    list_editable = ('category',)
    
class CategorysAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    read_only_fields = ('slug',)

admin.site.register(Categorys,CategorysAdmin)
admin.site.register(Bartas,BartaAdmin)
admin.site.register(Singlenotice)