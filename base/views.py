from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin,TemplateView):
	template_name = 'base/base.html'
	login_url = 'base:login'

class Perfil(LoginRequiredMixin,TemplateView):
    template_name = 'base/perfil.html'
    login_url = 'base:login'