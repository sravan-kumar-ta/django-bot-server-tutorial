from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from chat_db.forms import CustomUserCreationForm, LoginForm
from chat_db.models import BotCall, Bot


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
    text = payload.get('text').lower()
    bot = Bot.objects.get(text=text)
    try:
        bot_call = BotCall.objects.get(user=user, bot=bot)
    except:
        bot_call = BotCall.objects.create(user=user, bot=bot)

    bot_call.calls = bot_call.calls + 1
    bot_call.save()


def records_view(request, bot_id):
    bot = Bot.objects.get(id=bot_id)

    context = {
        'calls': BotCall.objects.filter(bot=bot),
        'bots': Bot.objects.filter(is_active=True),
        'bot': bot
    }
    return render(request, 'account/records.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
