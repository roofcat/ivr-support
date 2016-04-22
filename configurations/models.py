from __future__ import unicode_literals


from django.db import models


class SendGridConfiguration(models.Model):
    api_key = models.CharField(max_length=255, db_index=True)
    api_user = models.CharField(max_length=200, db_index=True)
    api_pass = models.CharField(max_length=200, db_index=True)
    email_from = models.EmailField(max_length=255, db_index=True)
    email_from_name = models.CharField(max_length=255, db_index=True)
    email_subject = models.CharField(max_length=255, db_index=True)

    def __unicode__(self):
        return u'{0}'.format(self.api_user)


class TemplateReport(models.Model):
    asunto = models.CharField(max_length=200, db_index=True)
    html_template = models.TextField()

    def __unicode__(self):
        return u'{0}'.format(self.asunto)
