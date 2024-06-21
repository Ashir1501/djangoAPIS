from django import forms
from decimal import Decimal
class ValidateForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name'
        })
    )
    age = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your age'
        })
    )
    salary = forms.DecimalField(
        min_value=1,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your salary'
        })
    )


class JokesCountForm(forms.Form):
    count = forms.IntegerField(max_value=100, min_value=1)