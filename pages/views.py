from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin # Это для секретной комнаты!

# Комната "Главная страница"
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# Комната "О нас"
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

# Для всех зарегистрированных пользователей
class SecretPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/secret.html'
    login_url = '/admin/login/'  # Куда перенаправлять неавторизованных

class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'