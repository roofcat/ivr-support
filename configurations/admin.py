from django.contrib import admin


from .models import SendGridConfiguration
from .models import TemplateReport


class SendGridConfigurationAdmin(admin.ModelAdmin):
	list_display = ('api_key', 'api_user', 'api_pass')


class TemplateReportAdmin(admin.ModelAdmin):
	list_display = ('asunto', 'html_template',)


admin.site.register(SendGridConfiguration, SendGridConfigurationAdmin)
admin.site.register(TemplateReport, TemplateReportAdmin)
