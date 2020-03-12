from django.shortcuts import render
from django.http import HttpResponse
from first_aid_post.forms import QueueForm
from first_aid_post.models import Patient
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

queue = []

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
        queue.append(patient.id)
        return HttpResponseRedirect(reverse('queue_view', kwargs={'user_id':patient.id}))
    ctx = {
        'form': form
    }
    return render(request, 'index.html', ctx)

def queue_view(request, user_id):
    place = queue.index(user_id) +1
    time = (place - 1) * 5
    ctx = {
        'place':place,
        'queue':queue,
        'time': time
    }
    return render(request, 'queue.html', ctx)

def patient_view(request):
    return render(request, 'queue.html', ctx)

