from django.contrib import admin
from .models import Symptoms



class SymptomsAdmin(admin.ModelAdmin):
    list_display = ['title', 'english_title', 'created_at']


admin.site.register(Symptoms, SymptomsAdmin)