from django import forms
from django.forms import TextInput, RadioSelect, Select, EmailInput, ModelForm,CharField
from .models import UserProfile


class RegistrationForm(ModelForm):
    Repassword=CharField(widget=TextInput(attrs=
        {"Type": "text", 'Placeholder': "Write Your Name", "class": "form-control"}
        ))

    class Meta:
        Gender=(
            ('Male','Male'),
            ('Female','Female')
        )
        Country=(
            ('1', 'india'),
            ('2', 'United States'),
            ('3', 'France'),
            ('4', 'Italy'),
            ('5', 'others')
        )
        model=UserProfile
        fields=['username','lastname','gender',
                'city','country','password','email','Repassword']
        widgets={
            'username':TextInput(attrs={"Type":"text",'Placeholder':"Write Your Name","class":"form-control"}),
            'lastname':TextInput(attrs={"Type":"text","Placeholder":"Write Your LastName","class":"form-control"}),
            'gender':RadioSelect(choices=Gender),
            'city':TextInput(attrs={"Type":"text","Placeholder":"Enter the City","class":"form-control"}),
            'country':Select(attrs={"Type":"text","id":"inputState","class":"form-control"},choices=Country),
            'password':TextInput(attrs={"Type":"text","class":"form-control"}),
            'email':EmailInput(attrs={"Type":"text","class":"form-control","placeholder":"Enter a Valid Emial"})

        }
