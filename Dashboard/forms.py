from django.forms import Form,CharField,TextInput,ImageField,EmailField
class UpdateProfile(Form):
    username=CharField(
        widget=TextInput(attrs={"class":"form-control"}),required=False
    )
    lastname = CharField(
        widget=TextInput(attrs={"class": "form-control"}),required=False
    )
    phone = CharField(
        widget=TextInput(attrs={"class": "form-control"}),required=False
    )
    image=ImageField(required=False)
    email=EmailField(widget=TextInput(attrs={"class": "form-control"}),required=False)
