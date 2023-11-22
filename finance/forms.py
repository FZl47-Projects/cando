from django import forms

class TestForm(forms.Form):
    amount = forms.IntegerField()