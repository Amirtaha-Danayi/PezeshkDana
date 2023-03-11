from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField



class Sickness(models.Model):

    title = models.CharField(max_length=100)
    english_title = models.CharField(max_length=100)
    summary = RichTextField()
    definition = RichTextField(blank=True, null=True)
    classification = RichTextField(blank=True, null=True)
    pathophysiology = RichTextField(blank=True, null=True)
    differential_diagnoses = RichTextField(blank=True, null=True)
    clinical_features = RichTextField(blank=True, null=True)
    epidemiology = RichTextField(blank=True, null=True)
    etiology = RichTextField(blank=True, null=True)
    diagnosis = RichTextField(blank=True, null=True)
    management = RichTextField(blank=True, null=True)
    treatment = RichTextField(blank=True, null=True)
    risk_factors = RichTextField(blank=True, null=True)
    complications = RichTextField(blank=True, null=True)
    prognosis = RichTextField(blank=True, null=True)
    prevention = RichTextField(blank=True, null=True)
    other_names = RichTextField(blank=True, null=True)
    gallery = models.ImageField(blank=True, null=True, upload_to='SicknessGallery/')
    references = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sickness_detail', args=[self.id])
