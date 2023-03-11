from django.db import models
from ckeditor.fields import RichTextField


class Explanation(models.Model):
    title = models.CharField(max_length=200)
    english_title = models.CharField(max_length=200)
    scenario = RichTextField()

    #Chief_Complaintblank=True, null=True
    mainـcomplaintـPersian = RichTextField(blank=True, null=True)
    mainـcomplaintـenglish =RichTextField(blank=True, null=True)

    #History_of_Present_Illness
    onset = RichTextField(blank=True, null=True)
    location = RichTextField(blank=True, null=True)
    radiation = RichTextField(blank=True, null=True)
    duration = RichTextField(blank=True, null=True)
    character = RichTextField(blank=True, null=True)
    associated = RichTextField(blank=True, null=True)
    symptom = RichTextField(blank=True, null=True)
    exacerbating_and_alleviating = RichTextField(blank=True, null=True)
    factors = RichTextField(blank=True, null=True)
    temporal = RichTextField(blank=True, null=True)
    patterns =RichTextField(blank=True, null=True)
    severity = RichTextField(blank=True, null=True)
    other_details = RichTextField(blank=True, null=True)

    #Past_Medical_History
    past_medical_history = RichTextField(blank=True, null=True)

    #Medication_History
    medication_history = RichTextField(blank=True, null=True)

    #Family_History
    family_history = RichTextField(blank=True, null=True)

    #Social_History
    social_history = RichTextField(blank=True, null=True)

    #Review_of_Systems
    constitutional = RichTextField(blank=True, null=True)
    HENT = RichTextField(blank=True, null=True)
    integumentary = RichTextField(blank=True, null=True)
    cardiovascular =RichTextField(blank=True, null=True)
    gastrointestinal = RichTextField(blank=True, null=True)
    genitourinary = RichTextField(blank=True, null=True)
    endocrine = RichTextField(blank=True, null=True)
    hematology_Oncology = RichTextField(blank=True, null=True)
    neurologic = RichTextField(blank=True, null=True)
    respiratory = RichTextField(blank=True, null=True)

    #Related_Conditions
    related_disease =RichTextField(blank=True, null=True)
    related_symptoms = RichTextField(blank=True, null=True)
