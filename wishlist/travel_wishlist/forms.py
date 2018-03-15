from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place   # uses the Place class object model from the models.py
        fields = ('name', 'visited')    #fields name will be name and visited, to match the variables in the Place class object
