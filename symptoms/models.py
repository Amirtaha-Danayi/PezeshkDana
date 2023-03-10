from django.db import models
from django.urls import reverse


class Symptoms(models.Model):

    title = models.CharField(max_length=100 , verbose_name='عنوان') #
    english_title = models.CharField(max_length=100) #
    definition = models.TextField(blank=True , null=True) # تعریف
    classification = models.TextField(blank=True , null=True) # طبقه‌بندی
    mechanism = models.TextField(blank=True , null=True) # سازوکار
    pathophysiology = models.TextField(blank=True , null=True)# پاتوفیزیولوژی
    related = models.TextField(blank=True , null=True) # شرایط مرتبط
    diagnostic_value = models.TextField(blank=True , null=True) #ارزش‌های تشخیص
    clinical_features = models.TextField(blank=True , null=True) #ویژیگی‌های بالینی
    diagnosis = models.TextField(blank=True , null=True) #تشخیص
    epidemiology = models.TextField(blank=True , null=True) #اپیدمیولوژی
    management = models.TextField(blank=True , null=True) #مدیریت
    etiology = models.TextField(blank=True , null=True) #اتیولوژی
    cause = models.TextField(blank=True , null=True)#اتیولوژی
    gallery = models.ImageField(blank=True , null=True ,upload_to='SymptomsGallery/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('symptoms_detail', args=[self.id])



