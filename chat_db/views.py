from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from chat_db.forms import CustomUserCreationForm, LoginForm
from chat_db.models import BotCall


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
            login(request=self.request)
            return redirect('chat')
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
        bot_call = BotCall.objects.get(user=user)
    except:
        bot_call = BotCall.objects.create(user=user)

    if text == 'Dump':
        bot_call.dump = bot_call.dump + 1
    elif text == 'Stupid':
        bot_call.stupid = bot_call.stupid + 1
    elif text == 'Fat':
        bot_call.fat = bot_call.fat + 1

    bot_call.save()


def records_view(request):
    calls = BotCall.objects.all()
    return render(request, 'account/records.html', {'calls': calls, })


def logout_user(request):
    logout(request)
    return redirect('login')
