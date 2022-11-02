from django.forms import Form,TextInput,CharField,EmailInput,Select
class ShippingForm(Form):
    Country = (
        ('1', 'india'),
        ('2', 'United States'),
        ('3', 'France'),
        ('4', 'Italy'),
        ('5', 'others')
    )
    firstname=CharField(widget=TextInput(attrs={"class":"form-control"}))
    lastname=CharField(widget=TextInput(attrs={"class":"form-control"}))
    phone=CharField(widget=TextInput(attrs={"class":"form-control"}))
    email=CharField(widget=EmailInput(attrs={"class":"form-control"}))
    Country=CharField(widget=Select(attrs={"class":"form-control"},choices=Country))
    state=CharField(widget=TextInput(attrs={"class":"form-control"}))
    street=CharField(widget=TextInput(attrs={"class":"form-control"}))
    building=CharField(widget=TextInput(attrs={"class":"form-control"}))
    house=CharField(widget=TextInput(attrs={"class":"form-control"}))
    postalcode=CharField(widget=TextInput(attrs={"class":"form-control"}))
    zip=CharField(widget=TextInput(attrs={"class":"form-control"}))