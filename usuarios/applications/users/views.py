from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import FormView
from .models import User
from .functions import code_generator

from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        #Genereamos el codigo
        codigo = code_generator()


        User.objects.create_user(
            form.cleaned_data['username'], #recuperar el dato desde el formulario
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            codregistro = codigo
        )
        #enviar el codigo al email del user
        asunto = 'Confirmacion de email'
        mensaje = 'Codigo de verificacion' + codigo
        email_remitente = 'davbarreiro4@gmail.com'
        #
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email']])
        #redigir a la pantalla de validacion

        return HttpResponseRedirect(
               reverse(
                    'users_app:user-login'
               )
          )
    
class LoginUser(FormView):
        template_name = 'users/login.html'
        form_class = LoginForm
        success_url = reverse_lazy('home_app:panel')

        def form_valid(self, form):
            user = authenticate( #Autenticar usuario
                 username = form.cleaned_data['username'],
                 password = form.cleaned_data['password']
            )
            login(self.request, user)
            return super(LoginUser, self).form_valid(form)
        
class LogoutView(View):
     
     def get(self, request, *args, **kargs):
          logout(request)
          return HttpResponseRedirect(
               reverse(
                    'users_app:user-login'
               )
          )


class UpdatePasswordView(LoginRequiredMixin, FormView):
        template_name = 'users/update.html'
        form_class = UpdatePasswordForm
        success_url = reverse_lazy('users_app:user-login')
        login_url = reverse_lazy('users_app:user-login')

        def form_valid(self, form):
            usuario = self.request.user #Usuario logiado
            user = authenticate( #Autenticar usuario
                 username =usuario.username,
                 password = form.cleaned_data['password1']
            )
            if user:
               new_password = form.cleaned_data['password2']
               usuario.set_password(new_password)
               usuario.save()#Guardar contraseña nueva

            logout(self.request)
            return super(UpdatePasswordView, self).form_valid(form)
