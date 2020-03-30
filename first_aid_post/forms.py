from django import  forms
from  django.utils import  timezone
from  first_aid_post.models import Patient, Vacinations, Disease, DYNAMICS
import datetime

class QueueForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'special', 'placeholder': 'ФИО'}))

    def __init__(self, *args, **kwargs):
        super(QueueForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'ФИО'

    def clean(self):
        username = self.cleaned_data['username']
        if not Patient.objects.filter(fullname=username).exists():
            raise forms.ValidationError('Возможно вы ошиблись при вводе или данного юзера не существует')

class PatientForm(forms.Form):
    pheight = forms.IntegerField(widget=forms.NumberInput())
    pweights = forms.IntegerField(widget=forms.NumberInput())

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['pheight'].label = 'Рост'
        self.fields['pweights'].label = 'Вес'

class AddVacForm(forms.Form):
    vac = forms.ModelChoiceField(queryset=Vacinations.objects.all(), empty_label=None) 
    
    def __init__(self, *args, **kwargs):
        super(AddVacForm, self).__init__(*args, **kwargs)
        self.fields['vac'].label = 'прививка'



class AddDiagnosisForm(forms.Form):
    date = forms.DateTimeField(widget=forms.SelectDateWidget())
    status= forms.ChoiceField(choices = DYNAMICS) 
    disease = forms.ModelChoiceField(queryset=Disease.objects.all(), empty_label=None) 
    description = forms.CharField(widget=forms.Textarea)

class DatePickForm(forms.Form):
    sdate = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'form-my'}))
    edate = forms.DateTimeField(widget=forms.SelectDateWidget(attrs={'class': 'form-my'}), initial=timezone.now())
    def __init__(self, *args, **kwargs):
        super(DatePickForm, self).__init__(*args, **kwargs)
        self.fields['sdate'].label = 'Дата начала'
        self.fields['edate'].label = 'Дата конца'
    