from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField



class Medicines(models.Model):
    title = models.CharField(max_length=100)
    english_title = models.CharField(max_length=100)
    generic_name = RichTextField(null=True, blank=True)  # نام ژنریک
    english_name = RichTextField(null=True, blank=True)  # نام انگلیسی
    pronunciation = RichTextField(null=True, blank=True)  # تلفظ
    synonyms = RichTextField(null=True, blank=True)  # مترادف‌ها
    other_names = RichTextField(null=True, blank=True)  # سایر اسامی
    brands = RichTextField(null=True, blank=True)  # نام‌های تجاریRichTextField
    main_drug_category = RichTextField(null=True, blank=True)  # دسته بندی اصلی دارویی
    summary = RichTextField(null=True, blank=True)  # خلاصه
    mechanism_of_action = RichTextField(null=True, blank=True)  # ماکانیسم اثر
    indications = RichTextField(null=True, blank=True)  # اندیکاسیون‌ها
    contraindications = RichTextField(null=True, blank=True)  # کنترا اندیکاسیون‌ها
    related_treatments = RichTextField(null=True, blank=True)  # درمان‌های مرتبط
    related_conditions = RichTextField(null=True, blank=True)  # شرایط مرتبط
    drug_dose = RichTextField(null=True, blank=True)  # دوز دارو
    different_dosage_forms = RichTextField(null=True, blank=True)  # دوز اشکال مختلف
    drug_interactions = RichTextField(null=True, blank=True)  # تداخلات دارویی
    food_interactions = RichTextField(null=True, blank=True)  # تداخلات غذایی
    drug_absorption = RichTextField(null=True, blank=True)  # جذب دارو
    half_life = RichTextField(null=True, blank=True)  # نیمه عمر
    toxicity =RichTextField(null=True, blank=True)  # سمیت
    method_of_consumption = RichTextField(null=True, blank=True)  # شیوه مصرف
    adverse_effects = RichTextField(null=True, blank=True)  # اثرات نامطلوب
    side_effects = RichTextField(null=True, blank=True)  # عوارض جانبی
    symptoms_of_excessive_consumption = RichTextField(null=True, blank=True)  # علایم مصرف زیاد
    warnings = RichTextField(null=True, blank=True)  # هشدار‌ها
    gallery = models.ImageField(null=True, blank=True, upload_to='MedicinesGallery/')
    references = RichTextField(null=True, blank=True)  # منابع
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('medicines_detail', args=[self.id])


