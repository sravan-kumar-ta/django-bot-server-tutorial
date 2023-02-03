from django.contrib import admin

from chat_db.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'text', 'calls')


admin.site.register(Message, MessageAdmin)
