from django import forms

class AddPlaceForm(forms.Form):
    location = forms.CharField()
    time = forms.DateTimeField(widget=forms.DateTimeInput)


