from django import forms

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class AddPlaceForm(forms.Form):
    WHERE = forms.CharField()
    WHEN = forms.DateTimeField(widget=DateInput)