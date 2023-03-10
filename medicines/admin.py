from django.contrib import admin
from .models import Medicines

class MedicinesAdmin(admin.ModelAdmin):
    list_display = ['title', 'english_title', 'created_at', 'updated_at']


admin.site.register(Medicines, MedicinesAdmin)
