from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Experiments(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)  # نام انگلیسی
    natural_range = RichTextField(blank=True, null=True)  # محدوده طبیعی
    physiopathology = RichTextField(blank=True, null=True)  # فیزیوپاتولوژی
    reasons_for = RichTextField(blank=True, null=True)  # دلایل تغییر
    change = RichTextField(blank=True, null=True)  # مظاهر تغییر
    interpretation = RichTextField(blank=True, null=True)  # تفسیر
    quick_interpretation = RichTextField(blank=True, null=True)  # تفسیر سریع
    differential_diagnoses = models.TextField(blank=True, null=True)  # تشخیص های افتراقی
    false_results = RichTextField(blank=True, null=True)  # تشخیص‌های کاذب
    gallery = models.ImageField(upload_to='experiments_cover/', null=True, blank=True)
    references = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('experiments_detail', args=[self.id])