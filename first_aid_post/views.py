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
        queue.append(patient)
        return HttpResponseRedirect(reverse('queue_view'))
    ctx = {
        'form': form
    }
    return render(request, 'index.html', ctx)

def queue_view(request):
    ctx = {
        'queue':queue
    }
    return render(request, 'queue.html', ctx)


