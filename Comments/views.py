from django.shortcuts import render
from django.views.generic import CreateView

from .forms import CommentForm
class CommentSection(CreateView):
    form_class = CommentForm
    template_name = 'DetailView/ReviewSection.html'
    def form_valid(self, form):
        print(form)
        pass
    def get_context_data(self, *args,**kwargs):
        context=super(CommentSection, self).get_context_data(*args,**kwargs)
# Create your views here.
