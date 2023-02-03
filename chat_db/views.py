from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from chat_db.forms import CustomUserCreationForm, LoginForm
from chat_db.models import Message


class RegistrationView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "account/register.html"
    success_url = reverse_lazy("login")


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request=self.request, user=user)
            messages.success(self.request, 'Successfully logged in')
        else:
            messages.error(self.request, "Invalid credentials..!")
            return redirect('login')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid Credentials')
        return redirect('login')


def store_calls(payload):
    user = User.objects.get(username=payload.get('username'))
    text = payload.get('text')
    try:
        bot_msg = Message.objects.get(user=user, text=text)
    except:
        bot_msg = Message.objects.create(user=user, text=text, calls=0)
    bot_msg.calls = bot_msg.calls+1
    bot_msg.save()
