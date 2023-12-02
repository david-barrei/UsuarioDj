from django.shortcuts import render
from django.views.generic import CreateView

from .forms import UserRegisterForm

# Create your views here.

class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    from_class = UserRegisterForm
    success_url = '.'
