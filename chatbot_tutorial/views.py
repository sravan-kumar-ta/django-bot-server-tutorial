import random
from django.shortcuts import render

from chat_db.models import Bot


def chat(request):
    context = {
        'bots': Bot.objects.filter(is_active=True)
    }
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    text = message['text'].lower()
    bot = Bot.objects.get(text=text)
    bot_joke = [bot.joke1, bot.joke2]
    result_message = {'type': 'text', 'text': random.choice(bot_joke)}

    return result_message
