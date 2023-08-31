from django.contrib import admin
from .models import dform

admin.site.register(dform)

class dformAdmin(admin.ModelAdmin):
    list_display=('id','name', 'email', 'subject', 'message')
# Register your models here.
