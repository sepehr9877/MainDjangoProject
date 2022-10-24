from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account,UserProfile
def Registration(request):
    userid=request.user.id
    if User.is_authenticated:
        return redirect("/")
    if request.method=="POST":
        Register_form=RegistrationForm(data=request.POST or request.GET)
        print(Register_form.errors)
        if Register_form.is_valid():
            firstname=Register_form.cleaned_data['username']
            lastname=Register_form.cleaned_data['lastname']
            gender=Register_form.cleaned_data['gender']
            country=Register_form.cleaned_data['country']
            city=Register_form.cleaned_data['city']
            password=Register_form.cleaned_data['password']
            email=Register_form.cleaned_data['email']
            repassword=Register_form.cleaned_data['Repassword']
            Account.Object.create_user(username=firstname,firstname=firstname,lastname=lastname,email=email,password=password)
            UserProfile.objects.CreateUserProfile(firstname=firstname,
                                                  lastname=lastname,
                                                  password=password,
                                                  email=email,
                                                  gender=gender,
                                                  city=city,
                                                  country=country,
                                                  username=firstname)
    else:
        Register_form=RegistrationForm()
    context={"Registration":Register_form,}
    return render(request,"Login_Reg/Registration.html",context)

# Create your views here.
