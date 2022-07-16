from django.contrib import admin
from home.models import *
# Register your models here.

@admin.register(Note)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['user','date','heading','get_tags']

    def get_tags(self,obj):
        return ", ".join(o for o in obj.tags.names())        
#admin.site.register(Tag)
