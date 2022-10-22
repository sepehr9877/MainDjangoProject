from django import forms
from django.forms import TextInput,RadioSelect,Select,EmailInput
from .models import Account
class RepasswordForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['password']
        widgets={
            'password':TextInput(attrs={"class":"form-control","Placeholder":"Enter your Password Again"})
        }

class RegistrationForm(forms.ModelForm):

    class Meta:
        Gender=(
            ('Male','Male'),
            ('Female','Female')
        )
        Country=(
            ('india', 'india'),
            ('United States', 'United States'),
            ('France', 'France'),
            ('Italy', 'Italy'),
            ('others', 'others')
        )
        model=Account
        fields=['firstname','lastname','gender',
                'city','country','password','email']
        widgets={
            'firstname':TextInput(attrs={'Placeholder':"Write Your Name","class":"form-control"}),
            'lastname':TextInput(attrs={"Placeholder":"Write Your LastName","class":"form-control"}),
            'gender':RadioSelect(choices=Gender),
            'city':TextInput(attrs={"Placeholder":"Enter the City"}),
            'country':Select(attrs={"id":"inputState","class":"form-control"},choices=Country),
            'password':TextInput(attrs={"class":"form-control"}),
            'email':EmailInput(attrs={"class":"form-control","placeholder":"Enter a Valid Emial"})

        }