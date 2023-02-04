from django.contrib import admin

from chat_db.models import Bot, BotCall


class BotAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_active')
    list_editable = ('is_active',)


class BotCallAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'calls')


admin.site.register(Bot, BotAdmin)
admin.site.register(BotCall, BotCallAdmin)
