from django import forms
from django.forms import TextInput, RadioSelect, Select, EmailInput, ModelForm
from .models import Account
class RepasswordForm(ModelForm):
    class Meta:
        model=Account
        fields=['password']
        widgets={
            'password':TextInput(attrs={"Type":"text","class":"form-control","Placeholder":"Enter your Password Again"})
        }

class RegistrationForm(ModelForm):

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
        fields=['username','lastname','gender',
                'city','country','password','email']
        widgets={
            'username':TextInput(attrs={"Type":"text",'Placeholder':"Write Your Name","class":"form-control"}),
            'lastname':TextInput(attrs={"Type":"text","Placeholder":"Write Your LastName","class":"form-control"}),
            'gender':RadioSelect(choices=Gender),
            'city':TextInput(attrs={"Type":"text","Placeholder":"Enter the City","class":"form-control"}),
            'country':Select(attrs={"Type":"text","id":"inputState","class":"form-control"},choices=Country),
            'password':TextInput(attrs={"Type":"text","class":"form-control"}),
            'email':EmailInput(attrs={"Type":"text","class":"form-control","placeholder":"Enter a Valid Emial"})

        }