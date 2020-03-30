from django.shortcuts import render
from django.http import HttpResponse
from first_aid_post.forms import QueueForm, PatientForm, AddVacForm, AddDiagnosisForm, DatePickForm
from first_aid_post.models import Patient, Vacinations, PatientCard, Diagnosis, Disease
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import logging

queue = []
logger = logging.getLogger(__name__)
# def test1():
# #     queue.append(1)  # will use the outer one
# #
# # def test2():
# #     queue.append(1)

# Create your views here.
def index(request):
    form = QueueForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        patient = Patient.objects.get(fullname=username)
        if queue.count(patient.id) < 1 :
            queue.append(patient.id)

        return HttpResponseRedirect(reverse('queue_view', kwargs={'user_id':patient.id}))
    ctx = {
        'form': form
    }
    return render(request, 'index.html', ctx)

def queue_view(request, user_id):
    if queue.count(user_id) < 1 :
        return HttpResponseRedirect(reverse('index'))

    place = queue.index(user_id) +1
    time = (place - 1) * 5
    ctx = {
        'place':place,
        'queue':queue,
        'time': time
    }
    return render(request, 'queue.html', ctx)

def patient_view(request):
    
    if len(queue) == 0 :
        return render(request, 'nopac.html', {'data': 'новых пациентов пока нет'})


    patient = Patient.objects.get(id=queue[0])
    # form = PatientForm(request.POST or None)
    
    card = PatientCard.objects.get(title=patient)
    vacinations = Vacinations.objects.all().filter(patientcard=card)
    diagnosis = Diagnosis.objects.all().filter(patient=card)

    addvac = AddVacForm(request.POST or None)
    if addvac.is_valid():
        vac = addvac.cleaned_data['vac']
        card.vaccinations.add(Vacinations.objects.get(title=vac))
        
        return HttpResponseRedirect(reverse('patient_view'))

    adddes = AddDiagnosisForm(request.POST or None)
    if adddes.is_valid():
        description = adddes.cleaned_data['description']
        disease = adddes.cleaned_data['disease']
        date = adddes.cleaned_data['date']
        status = adddes.cleaned_data['status']

        diagnos = Diagnosis()
        diagnos.patient = card
        diagnos.disease = disease
        diagnos.date = date
        diagnos.status = status
        diagnos.description = description
        diagnos.save()

        return HttpResponseRedirect(reverse('patient_view'))

    ctx = {
        'patient': patient,
        # 'form': form,
        'card': card,
        'vacinations' : vacinations,
        'diagnosis': diagnosis,
        'form_add_vac': addvac,
        'form_add_des': adddes
    }
    return render(request, 'patient.html', ctx)

def main_view(request):
    return render(request, 'base.html', {})

def patientnext_view(request):
    if len(queue) != 0 :
        del queue[0]
    return HttpResponseRedirect(reverse('patient_view'))


def search_view(request):
    searchform = QueueForm(request.POST or None)
    if searchform.is_valid():
        username = searchform.cleaned_data['username']
        patient = Patient.objects.get(fullname=username)
        
        return HttpResponseRedirect(reverse('s_patient_view', kwargs={'user_id':patient.id}))
    
    ctx = {
        'form': searchform
    }    
    
    return render(request, 'sform.html', ctx)
    

def s_patient_view(request, user_id):
    patient = Patient.objects.get(id=user_id)
    
    
    card = PatientCard.objects.get(title=patient)
    vacinations = Vacinations.objects.all().filter(patientcard=card)
    diagnosis = Diagnosis.objects.all().filter(patient=card)

    addvac = AddVacForm(request.POST or None)
    if addvac.is_valid():
        vac = addvac.cleaned_data['vac']
        card.vaccinations.add(Vacinations.objects.get(title=vac))
        
        return HttpResponseRedirect(reverse('s_patient_view', kwargs={'user_id':patient.id}))

    adddes = AddDiagnosisForm(request.POST or None)
    if adddes.is_valid():
        description = adddes.cleaned_data['description']
        disease = adddes.cleaned_data['disease']
        date = adddes.cleaned_data['date']
        status = adddes.cleaned_data['status']

        diagnos = Diagnosis()
        diagnos.patient = card
        diagnos.disease = disease
        diagnos.date = date
        diagnos.status = status
        diagnos.description = description
        diagnos.save()


    ctx = {
        'patient': patient,
        'card': card,
        'vacinations' : vacinations,
        'diagnosis': diagnosis,
        'form_add_vac': addvac,
        'form_add_des': adddes
    }

    return render(request, 'search.html', ctx)


def params_view(request):


    return render(request, 'search.html', {})

def report_view(request):
    pickup_records = []
    form = DatePickForm(request.POST or None)
    if form.is_valid():
        sdate = form.cleaned_data['sdate']
        edate = form.cleaned_data['edate']
        desiase = Disease.objects.all()
        
        for d in desiase :
            ill = Diagnosis.objects.filter(disease=d, status='Заболел', date__range=[sdate, edate])
            healthy = Diagnosis.objects.filter(disease=d, status='Выздоровел', date__range=[sdate, edate])
            record = {
                'title': d,
               'count': len(ill)-len(healthy)
            }
            pickup_records.append(record)
    

    ctx = {
        'form': form,
        'data': pickup_records
    }


    return render(request, 'report.html', ctx)