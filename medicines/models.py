from django.db import models
from django.urls import reverse


class Medicines(models.Model):
    title = models.CharField(max_length=100)
    english_title = models.CharField(max_length=100)
    generic_name = models.TextField(null=True, blank=True)  # نام ژنریک
    english_name = models.TextField(null=True, blank=True)  # نام انگلیسی
    pronunciation = models.TextField(null=True, blank=True)  # تلفظ
    synonyms = models.TextField(null=True, blank=True)  # مترادف‌ها
    other_names = models.TextField(null=True, blank=True)  # سایر اسامی
    brands = models.TextField(null=True, blank=True)  # نام‌های تجاری
    main_drug_category = models.TextField(null=True, blank=True)  # دسته بندی اصلی دارویی
    summary = models.TextField(null=True, blank=True)  # خلاصه
    mechanism_of_action = models.TextField(null=True, blank=True)  # ماکانیسم اثر
    indications = models.TextField(null=True, blank=True)  # اندیکاسیون‌ها
    contraindications = models.TextField(null=True, blank=True)  # کنترا اندیکاسیون‌ها
    related_treatments = models.TextField(null=True, blank=True)  # درمان‌های مرتبط
    related_conditions = models.TextField(null=True, blank=True)  # شرایط مرتبط
    drug_dose = models.TextField(null=True, blank=True)  # دوز دارو
    different_dosage_forms = models.TextField(null=True, blank=True)  # دوز اشکال مختلف
    drug_interactions = models.TextField(null=True, blank=True)  # تداخلات دارویی
    food_interactions = models.TextField(null=True, blank=True)  # تداخلات غذایی
    drug_absorption = models.TextField(null=True, blank=True)  # جذب دارو
    half_life = models.TextField(null=True, blank=True)  # نیمه عمر
    toxicity = models.TextField(null=True, blank=True)  # سمیت
    method_of_consumption = models.TextField(null=True, blank=True)  # شیوه مصرف
    adverse_effects = models.TextField(null=True, blank=True)  # اثرات نامطلوب
    side_effects = models.TextField(null=True, blank=True)  # عوارض جانبی
    symptoms_of_excessive_consumption = models.TextField(null=True, blank=True)  # علایم مصرف زیاد
    warnings = models.TextField(null=True, blank=True)  # هشدار‌ها
    gallery = models.ImageField(null=True, blank=True, upload_to='MedicinesGallery/')
    references = models.TextField(null=True, blank=True)  # منابع
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('medicines_detail', args=[self.id])


