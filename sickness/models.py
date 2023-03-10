from django.db import models
from django.urls import reverse


class Sickness(models.Model):

    title = models.CharField(max_length=100)
    english_title = models.CharField(max_length=100)
    summary = models.TextField()
    definition = models.TextField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    pathophysiology = models.TextField(blank=True, null=True)
    differential_diagnoses = models.TextField(blank=True, null=True)
    clinical_features = models.TextField(blank=True, null=True)
    epidemiology = models.TextField(blank=True, null=True)
    etiology = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    management = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    risk_factors = models.TextField(blank=True, null=True)
    complications = models.TextField(blank=True, null=True)
    prognosis = models.TextField(blank=True, null=True)
    prevention = models.TextField(blank=True, null=True)
    other_names = models.TextField(blank=True, null=True)
    gallery = models.ImageField(blank=True, null=True, upload_to='SicknessGallery/')
    references = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sickness_detail', args=[self.id])
