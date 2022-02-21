from django.contrib import admin
from .models import *

# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name','email','school',"slug")
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name','email',"school")}
admin.site.register(People,PeopleAdmin)
admin.site.register(Teacher)
admin.site.register(Food)