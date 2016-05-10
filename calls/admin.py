# -*- coding: utf-8 -*-


from django.contrib import admin


from .models import Call


class CallAdmin(admin.ModelAdmin):
    list_display = ('beginCall', 'origin', 'callAnswered',)
    list_filter = ('beginCall', 'origin', 'callAnswered',)
    search_fields = ('beginCall', 'origin', 'callAnswered',)


admin.site.register(Call, CallAdmin)
