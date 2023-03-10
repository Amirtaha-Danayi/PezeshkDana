from django.contrib import admin
from .models import Sickness

class AdminSickness(admin.ModelAdmin):
    list_display = ['title' , 'english_title' , 'created_at']




admin.site.register(Sickness ,AdminSickness)