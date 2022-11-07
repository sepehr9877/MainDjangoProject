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

class CreditCardForm(Form):
    Month=(
        ('1',"Jan"),
        ('2',"Feb"),
        ('3',"Mar"),
        ('4',"Apr"),
        ('5','May'),
        ('6','June'),
        ('7','July'),
        ('8','Aug'),
        ('9','Sep'),
        ('10','Oct'),
        ('11','Nov'),
        ('12','Dec')

    )
    cardnumber=CharField(
        widget=TextInput(attrs={"class":"form-control mr-2","placeholder":"xxxx-xxxx-xxxx-xxxx"})
    )
    card_year=CharField(
        widget=TextInput(attrs={"class":"form-control mr-2","style":"width:100px","placeholder":"YY"})
    )
    card_month = CharField(
        widget=Select(attrs={"class":"form-control mr-2","style":"width:100px"},choices=Month)
    )
    cardcsv=CharField(
        widget=TextInput(attrs={"class":"form-control mr-2","placeholder":"Csv","style":"width:100px","maxlength":"3"})
    )
