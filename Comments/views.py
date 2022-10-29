from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .context_processors import CommentForm
from .models import Comments
class AddingComment(CreateView):
    template_name = 'DetailView/ReviewSection.html'
    form_class = CommentForm
    productid=None
    slug_field = 'int'
    slug_url_kwarg = 'ID'
    def post(self, request, *args, **kwargs):
        self.productid=self.kwargs[self.slug_url_kwarg]
        commetform=CommentForm(data=self.request.POST)
        validation=self.form_valid(form=commetform)
        if validation:
            Description=commetform.cleaned_data['Description']
            user_id=self.request.user.id
            Comments.objects.create(User_Comment_id=3,Description=Description)
            return redirect(f'/ProductDetail/{self.productid}')
    def form_valid(self, form):
        if form.is_valid():
            return True
        return False
# Create your views here.