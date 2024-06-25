from django import forms
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator, DecimalValidator
class ValidateForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class':'form-control'
        }),
        validators=[
            RegexValidator(regex=r"^[A-Za-z\s]+$",
                message="Name should contain only alphabets",
                code="invalid name"
            )
        ]
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your age',
            'class':'form-control'
        }),
        validators=[
            MaxValueValidator(
                120,
                message="Age cannot be greater than 120"
            ),
            MinValueValidator(
                18,
                message="Age cannot be less than 18"
            )
        ]
    )
    salary = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your salary',
            'class':'form-control'
        }),
        validators=[
            DecimalValidator(10,2),
            MinValueValidator(1000)
        ]
    )


class JokesCountForm(forms.Form):
    count = forms.IntegerField(
        min_value=1,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter limit of jokes',
            'class':'form-control'
        }),
    )

class GreetingsForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder':'Enter your Name',
            'class':'form-control'
        }),
        validators=[
            RegexValidator(regex=r"^[A-Za-z\s]+$",
                message="Name should contain only alphabets",
                code="invalid name"
            )
        ]
    )