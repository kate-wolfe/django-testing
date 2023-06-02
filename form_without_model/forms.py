from django import forms


class SetupForm(forms.Form):
    primitive = forms.CharField(max_length=30)
    map_path = forms.CharField(max_length=200)
