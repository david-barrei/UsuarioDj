from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import User

from .forms import UserRegisterForm

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['username'], #recuperar el dato desde el formulario
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
        )
        return super(UserRegisterView, self).form_valid(form)
