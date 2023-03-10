from django.db import models
from django.urls import reverse


class Experiments(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)  # نام انگلیسی
    natural_range = models.TextField()  # محدوده طبیعی
    physiopathology = models.TextField()  # فیزیوپاتولوژی
    reasons_for = models.TextField()  # دلایل تغییر
    change = models.TextField()  # مظاهر تغییر
    interpretation = models.TextField()  # تفسیر
    quick_interpretation = models.TextField()  # تفسیر سریع
    differential_diagnoses = models.TextField()  # تشخیص های افتراقی
    false_results = models.TextField()  # تشخیص‌های کاذب
    gallery = models.ImageField(upload_to='experiments_cover/', null=True, blank=True)
    references = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('experiments_detail', args=[self.id])