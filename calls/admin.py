# -*- coding: utf-8 -*-


from django.contrib import admin


from .models import Call


class CallAdmin(admin.ModelAdmin):
	list_display = ('begin_call', 'origin', 'call_answered',)
	list_filter = ('begin_call', 'origin', 'call_answered',)
	search_fields = ('begin_call', 'origin', 'call_answered',)


admin.site.register(Call, CallAdmin)
