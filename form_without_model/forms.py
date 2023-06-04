from django import forms


class SetupForm(forms.Form):
    # primitive = forms.CharField(max_length=30)
    index_choice = forms.IntegerField()
    # map_path = forms.CharField(max_length=200)
