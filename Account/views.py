from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView

from .forms import Registerform,LoginForm
from .models import Account
class RegisterPage(FormView):
    template_name = 'Login_Reg/Registration.html'
    registerform = Registerform
    def get(self, request, *args, **kwargs):
        if(self.request.user.is_authenticated):
            return redirect("/")
        else:
            return render(request=self.request,template_name=self.template_name,context={"Registration":Registerform()})

    def post(self, request, *args, **kwargs):
        register_form=Registerform(data=self.request.POST)
        if(self.form_valid(form=register_form)):
            username=register_form.cleaned_data['username']
            lastname=register_form.cleaned_data['lastname']
            password=register_form.cleaned_data['password']
            gender=register_form.cleaned_data['gender']
            country=register_form.cleaned_data['country']
            city=register_form.cleaned_data['city']
            email=register_form.cleaned_data['email']
            repassword=register_form.cleaned_data['repassword']
            created_user=User.objects.create_user(username=username,email=email,password=password)
            created_user.is_staff=True
            created_user.first_name=username
            created_user.last_name=lastname
            created_account=Account.objects.create(user_id=created_user.id,city=city,country=country,gender=gender)
            created_user.save()
            return redirect("/")


    def form_valid(self, form):
        if(form.is_valid()):
            return True
        else:
            return False

class LoginPage(FormView):
    template_name = 'Login_Reg/loginpage.html'
    form_class = LoginForm
    def get(self, request, *args, **kwargs):
        if(self.request.user.is_authenticated):
            print(self.request.user.username)
            return redirect("/")
        else:
            return render(request=self.request,template_name=self.template_name,context={"loginform":LoginForm})
    def post(self, request, *args, **kwargs):
        request=self.request
        log_form=LoginForm(data=request.POST)
        if(self.form_valid(form=log_form)):
            username=log_form.cleaned_data.get("UserName")
            password=log_form.cleaned_data.get("Password")
            user=authenticate(self.request,username=username,password=password)
            if user is not None:

                login(self.request,user)
                print(self.request.user.username)
                return redirect("/")
            else:
                raise ValueError("You Dont Have An Account")
    def form_valid(self, form):
        if form.is_valid():
            return True
        else:
            return False



# Create your views here.
