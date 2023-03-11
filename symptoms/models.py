from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField




class Symptoms(models.Model):

    title = models.CharField(max_length=100 , verbose_name='عنوان')
    english_title = models.CharField(max_length=100) #
    definition = RichTextField(blank=True , null=True) # تعریف
    classification = RichTextField(blank=True , null=True) # طبقه‌بندی
    mechanism = RichTextField(blank=True , null=True) # سازوکار
    pathophysiology = RichTextField(blank=True , null=True)# پاتوفیزیولوژی
    related = RichTextField(blank=True , null=True) # شرایط مرتبط
    diagnostic_value = RichTextField(blank=True , null=True) #ارزش‌های تشخیص
    clinical_features = RichTextField(blank=True , null=True) #ویژیگی‌های بالینی
    diagnosis = RichTextField(blank=True , null=True) #تشخیص
    epidemiology = RichTextField(blank=True , null=True) #اپیدمیولوژی
    management = RichTextField(blank=True , null=True) #مدیریت
    etiology = RichTextField(blank=True , null=True) #اتیولوژی
    cause = RichTextField(blank=True , null=True)#اتیولوژی
    gallery = models.ImageField(blank=True , null=True ,upload_to='SymptomsGallery/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('symptoms_detail', args=[self.id])



