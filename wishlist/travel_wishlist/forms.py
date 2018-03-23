from django import forms
from .models import Place


# datepicker widget reference: https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
class DateInput(forms.DateInput):
    input_type = 'date'


# Initial addition/creation of Places
class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place   # uses the Place class object model from the models.py
        fields = ('name',)    #fields name will be name and visited, to match the variables in the Place class object


# For modifying/adding more values
# datepicker widget reference: https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
class VisitPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('date_visited', 'notes',)
        widgets = {
            'date_visited': DateInput()
        }
