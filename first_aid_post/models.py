from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from transliterate import translit


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    # slug = models.SlugField(blank=True)
    position = models.CharField(max_length=100)
    subdivision = models.CharField(max_length=100)
    working_conditions = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname





class PatientCard(models.Model):
    title = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # slug = models.SlugField(blank=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    vaccinations = models.ManyToManyField('Vacinations')

    def __str__(self):
        return  self.title.fullname

class Vacinations(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    # slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

DYNAMICS = (
    ('Заболел', 'Заболел'),
    ('Выздоровел', 'Выздоровел'),
    ('Болеет', 'Болеет'),
)

class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    patient = models.ForeignKey(PatientCard, on_delete=models.CASCADE)
    disease = models.ForeignKey('Disease', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=DYNAMICS, default=DYNAMICS[0][0])
    # slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return '%s %s %s %s' % (self.date, self.patient,self.disease, self.status)


class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    # slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

class Referral(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    patient = models.ForeignKey(PatientCard, on_delete=models.CASCADE)


#
# def pre_save_slug(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         slug = slugify(translit(instance.title, reversed=True))
#         instance.slug = slug
#
# def pre_save_slug_card(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         slug = slugify(translit(instance.title.title, reversed=True))+"'s card"
#         instance.slug = slug
#
#
#
#
#
# pre_save.connect(pre_save_slug_card, sender=PatientCard)
# pre_save.connect(pre_save_slug, sender=Patient)
# pre_save.connect(pre_save_slug, sender=Vacinations)
# pre_save.connect(pre_save_slug, sender=Diagnosis)
