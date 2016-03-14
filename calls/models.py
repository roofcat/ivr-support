# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from datetime import datetime
import calendar


from django.db import models


class Call(models.Model):
	collection = models.CharField(max_length=255, blank=True, null=True)
	sp = models.CharField(max_length=255, blank=True, null=True)
	key = models.BigIntegerField(null=True, blank=True)
	begin_call = models.DateTimeField(null=True, blank=True)
	origin = models.BigIntegerField(null=True, blank=True)
	call_answered = models.BooleanField(default=False)
	last_state = models.CharField(max_length=255, blank=True, null=True)
	ivr_sel = models.BigIntegerField(null=True, blank=True)
	dial_intent_begin = models.DateTimeField(null=True, blank=True)
	dial_intent_caller = models.BigIntegerField(null=True, blank=True)
	dial_intent_called = models.BigIntegerField(null=True, blank=True)
	dial_intent_end = models.DateTimeField(null=True, blank=True)
	dial_intent_answered = models.BooleanField(default=False)
	session_file = models.FileField(
		upload_to='audio/%Y/%m/%d{0}'.format(
			calendar.timegm(datetime.utcnow().utctimetuple())),
		null=True
	)
	hc = models.CharField(max_length=150, null=True, blank=True)
	routing = models.CharField(max_length=255, null=True, blank=True)
	name = models.CharField(max_length=255, null=True, blank=True)
	end_dial = models.DateTimeField(null=True, blank=True)
	timestamp = models.DateTimeField(null=True, blank=True)
