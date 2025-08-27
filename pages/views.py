from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # Это для секретной комнаты!

# Комната "Главная страница"
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# Комната "О нас"
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

# СЕКРЕТНАЯ комната! Только для админа.
class SecretPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/secret.html'