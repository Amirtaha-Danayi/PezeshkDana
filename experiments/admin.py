from django.contrib import admin
from .models import Experiments



class ExperimentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'english_name','created_at']


admin.site.register(Experiments, ExperimentsAdmin)