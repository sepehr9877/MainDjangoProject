from django.forms import ModelForm,TextInput
from .models import Comments

class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['Description']
        widgets={
            'Description':TextInput(attrs={"class":"mt","rows":4,"cols":"50","form":"usrform"})
        }