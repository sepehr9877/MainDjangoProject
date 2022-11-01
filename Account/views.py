from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView

from .forms import RegistrationForm,LoginForm
from .models import Account
def Registration(request):
    userid=request.user.id
    # if User.is_authenticated:
    #     return redirect("/")
    if request.method=="POST":
        Register_form=RegistrationForm(data=request.POST or request.GET)
        if Register_form.is_valid():
            firstname=Register_form.cleaned_data['username']
            lastname=Register_form.cleaned_data['lastname']
            gender=Register_form.cleaned_data['gender']
            country=Register_form.cleaned_data['country']
            city=Register_form.cleaned_data['city']
            password=Register_form.cleaned_data['password']
            email=Register_form.cleaned_data['email']
            repassword=Register_form.cleaned_data['Repassword']
            print(repassword)
            User_Account=Account.Object.create_user(username=firstname,
                                                    firstname=firstname,
                                                    lastname=lastname,
                                                    email=email,
                                                    password=password,
                                                    gender=gender,
                                                    city=city,
                                                    country=country)

    else:
        Register_form=RegistrationForm()
    context={"Registration":Register_form,}
    return render(request,"Login_Reg/Registration.html",context)
class LoginPage(FormView):
    template_name = 'Login_Reg/loginpage.html'
    form_class = LoginForm
    def post(self, request, *args, **kwargs):
        request=self.request
        log_form=LoginForm(data=request.POST)
        print(log_form.errors)
        if(self.form_valid(form=log_form)):
            print("eee")
            username=log_form.cleaned_data.get("UserName")
            password=log_form.cleaned_data.get("Password")

    def form_valid(self, form):
        if form.is_valid():
            return True
        else:
            return False

    def get_context_data(self, *args,**kwargs):
        context=super(LoginPage, self).get_context_data(*args,**kwargs)
        context['loginform']=LoginPage()
        return context


# Create your views here.
