from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.db.models import Q

from .backends import AuthBackend
from .forms import RegistationForm, LoginForm

def index(request):
    return render(request, 'auth/index.html', {"us": request.user})

class SignUpView(CreateView):
    form_class = RegistationForm
    template_name = 'auth/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class LoginView(CreateView): #добавить верстку, возврат пароля!!!!
    form_class = LoginForm
    template_name = 'auth/login.html'
    auth = AuthBackend()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Авторизация"
        return context

    def post(self, request, *args, **kwargs):
        user = self.auth.authenticate(self.request, email=self.request.POST.get("phone"), password=self.request.POST.get("password"))

        if user:
            login(self.request, user)
        return redirect('index')

def log_out(request):
    logout(request)
    return redirect('index')