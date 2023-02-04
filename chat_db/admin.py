from django.contrib import admin

from chat_db.models import BotCall


class BotCallAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'stupid', 'fat', 'dump')


admin.site.register(BotCall, BotCallAdmin)
