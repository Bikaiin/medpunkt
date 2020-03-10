from django import  forms
from  django.utils import  timezone
from  first_aid_post.models import Patient

class QueueForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'special', 'placeholder': 'Ваше ФИО'}))

    def __init__(self, *args, **kwargs):
        super(QueueForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'ФИО'

    def clean(self):
        username = self.cleaned_data['username']
        if not Patient.objects.filter(fullname=username).exists():
            raise forms.ValidationError('Возможно вы ошиблись при вводе или данного юзера не существует')
