from django import forms
from django.forms import TextInput, RadioSelect, Select, EmailInput, ModelForm,CharField
from .models import Account


class RegistrationForm(ModelForm):
    Repassword=CharField(widget=TextInput(attrs={"Type": "text", 'Placeholder': "Write Your Name", "class": "form-control"}))
    class Meta:

        model=Account
        fields=['username','lastname','password','email','Repassword','city','country','gender']
        exclude=['is_superadmin','is_active','is_staff']
        Country = (
            ('1', 'india'),
            ('2', 'United States'),
            ('3', 'France'),
            ('4', 'Italy'),
            ('5', 'others')
        )
        Gender = (
            ('Male', 'Male'),
            ('Female', 'Female')
        )
        widgets={
            'username':TextInput(attrs={"Type":"text",'Placeholder':"Write Your Name","class":"form-control"}),
            'lastname':TextInput(attrs={"Type":"text","Placeholder":"Write Your LastName","class":"form-control"}),
            'password':TextInput(attrs={"Type":"text","class":"form-control"}),
            'email':EmailInput(attrs={"Type":"text","class":"form-control","placeholder":"Enter a Valid Emial"}),
            'city':TextInput(attrs={"Type": "text", "Placeholder": "Enter the City", "class": "form-control"}),
            'country':Select(attrs={"Type": "text", "id": "inputState", "class": "form-control"}, choices=Country),
            "gender":RadioSelect(choices=Gender)

        }

class LoginForm(forms.Form):
    UserName=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Username"})
    )
    Password=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Password"})
    )

