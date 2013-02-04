from django import forms
#from django.forms import ModelForm
from openlabs.models import Details


class DetailsForm(forms.ModelForm):
    
    class Meta:
        model = Details