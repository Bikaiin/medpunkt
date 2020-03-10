from django.contrib import admin
from first_aid_post.models import PatientCard, Patient, Vacinations, Disease, Diagnosis

admin.site.register(PatientCard)
admin.site.register(Patient)
admin.site.register(Vacinations)
admin.site.register(Disease)
admin.site.register(Diagnosis)
