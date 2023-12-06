import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import(
    TemplateView
)

# Create your views here.

class FechaMixin(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now() #obtenga la fecha
        return context

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('users_app:user-login')#Verificar si el usuario esta logiado


    
class TemplatePruebaMixin(FechaMixin,TemplateView):
    template_name = "home/mixin.html"
    