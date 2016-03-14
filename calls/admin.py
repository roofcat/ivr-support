# -*- coding: utf-8 -*-


from django.contrib import admin


from .models import Call


class CallAdmin(admin.ModelAdmin):
	list_display = ()
	list_filter = ()
	search_fields = ()


admin.site.register(Call, CallAdmin)
