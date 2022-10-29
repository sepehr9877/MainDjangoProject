from django.forms import ModelForm,TextInput,Textarea
from .models import Comments
class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['Description']
        widgets={
            'Description':Textarea()
        }

def passform(request):
    return dict(commentform=CommentForm())
def pass_all_comments(request):
    return dict(comments=Comments.objects.all())