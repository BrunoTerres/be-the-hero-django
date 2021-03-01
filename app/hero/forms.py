from django import forms

from .models import Ngo, Incidents

class NgoRegister(forms.ModelForm):

    class Meta:
        model = Ngo
        fields = ('name', 'email', 'whatsapp', 'city', 'ur',)