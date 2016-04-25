# -*- coding: utf-8 -*-


import logging


from sendgrid import Mail
from sendgrid import SendGridClient


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


from configurations.models import SendGridConfiguration
from configurations.models import TemplateReport


logger = logging.getLogger('SGEmailClient')


class SGEmailClient(object):

	def __init__(self):
		self.email_config = SendGridConfiguration.objects.all()[:1].get()
		self.sg = SendGridClient(self.email_config.api_key)
		self.message = Mail()
		self.message.set_from(self.email_config.email_from)
		self.message.set_from_name(self.email_config.email_from_name)
		self.message.set_subject(self.email_config.email_subject)

	def send_report_email(self, email, report):
		template_config = TemplateReport.objects.all()[:1].get()
		user = get_object_or_404(User, pk=email)
		logger.info(user)
		html = unicode(template_config.html_template).format(
			user_name=user.first_name,
		)
		self.message.add_to(user.email)
		self.message.add_to_name(user.first_name)
		self.message.set_html(html)

		if report['report']:
			self.message.add_attachment_stream(
				report['name'] , report['report']
			)

		status, msg = self.sg.send(self.message)
		logger.info('{0} - {1}'.format(status, msg))
