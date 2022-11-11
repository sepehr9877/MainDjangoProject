from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, RadioSelect, Select, EmailInput, ModelForm,CharField
from .models import Account
class Registerform(forms.Form):
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
    username=forms.CharField(widget=TextInput(attrs={"Type":"text",'Placeholder':"Write Your Name","class":"form-control"}))
    lastname=forms.CharField(widget=TextInput(attrs={"Type":"text","Placeholder":"Write Your LastName","class":"form-control"}))
    password=forms.CharField(widget=TextInput(attrs={"Type":"text","class":"form-control"}))
    repassword=CharField(widget=TextInput(attrs={"Type": "text", 'Placeholder': "Write Your Name", "class": "form-control"}))
    email=forms.CharField(widget=EmailInput(attrs={"Type":"text","class":"form-control","placeholder":"Enter a Valid Emial"}))
    city=forms.CharField(widget=TextInput(attrs={"Type": "text", "Placeholder": "Enter the City", "class": "form-control"}))
    country=forms.CharField(widget=Select(attrs={"Type": "text", "id": "inputState", "class": "form-control"}, choices=Country))
    gender=forms.CharField(widget=RadioSelect(choices=Gender))
    def clean_repassword(self):
        repassword=self.cleaned_data['repassword']
        print("repassword")
        password=self.cleaned_data['password']
        if password!=repassword:
            print("enter the password error")
            raise forms.ValidationError("Passwords arent match")
        return password
    def clean_username(self):
        username=self.cleaned_data['username']
        print("username")
        selected_user=Account.objects.filter(user__username=username)
        if selected_user:
            print("enter error")
            raise forms.ValidationError("Username Already Existed")
        return username
    def clean_email(self):
        email=self.cleaned_data['email']
        selected_email=Account.objects.filter(user__email=email)
        if selected_email:
            raise forms.ValidationError("Email Already Existed")
        return email
class LoginForm(forms.Form):
    UserName=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Username"})
    )
    Password=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Your Password"})
    )

