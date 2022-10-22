from django.shortcuts import render
from .forms import RegistrationForm,RepasswordForm
def Registration(request):
    userid=request.user.id
    if request.method=="POST":
        Register_form=RegistrationForm(data=request.POST)
        Repassword_form = RepasswordForm(data=request.POST)
        if Repassword_form.is_valid():
            repassword=Repassword_form.cleaned_data['password']
            print(repassword)
        if Register_form.is_valid():
            firstname=Register_form.cleaned_data['firstname']
            lastname=Register_form.cleaned_data['lastname']
            gender=Register_form.cleaned_data['gender']
            country=Register_form.cleaned_data['country']
            city=Register_form.cleaned_data['city']
            password=Register_form.cleaned_data['password']
            email=Register_form.cleaned_data['email']

    Register_form=RegistrationForm()
    Repassword_form=RepasswordForm()
    context={"Registration":Register_form,
             "Repassword":Repassword_form}
    return render(request,"Login_Reg/Registration.html",context)
# Create your views here.
