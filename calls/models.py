# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from datetime import datetime, timedelta
import calendar
import json
import logging


from django.db import models
from django.core import serializers


from utils import timestamp_to_date


logger = logging.getLogger("CallsApp")
time_delta = timedelta(hours=23.999999999)


class Call(models.Model):
    collection = models.CharField(max_length=150)
    sp = models.CharField(max_length=150)
    key = models.BigIntegerField()
    beginCall = models.DateTimeField()
    origin = models.BigIntegerField()
    callAnswered = models.BooleanField(default=False)
    lastState = models.CharField(max_length=150, null=True)
    IVRSel = models.BigIntegerField(null=True)
    dialIntentBegin1 = models.DateTimeField(null=True)
    dialIntentCaller1 = models.BigIntegerField()
    dialIntentCalled1 = models.BigIntegerField()
    dialIntentEnd1 = models.DateTimeField()
    dialIntentAnswered1 = models.BooleanField()
    sessionFile = models.CharField(max_length=255, null=True, blank=True)
    hc = models.CharField(max_length=150)
    routing = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    endDial = models.DateTimeField()
    timeStamp = models.DateTimeField()

    def __unicode__(self):
        return "{0} - {1} - {2}".format(self.timeStamp, self.origin, self.callAnswered)

    @classmethod
    def get_dynamic_calls(self, date_from, date_to, display_start, display_length):
        date_from = timestamp_to_date(date_from)
        date_to = timestamp_to_date(date_to) + time_delta
        params = dict()
        params['timeStamp__range'] = (date_from, date_to)

        # ejecución de la query
        calls = Call.objects.filter(**params).order_by('-timeStamp')
        logger.info(calls.query)
        query_total = calls.count()
        logger.info("Total query count: {0}".format(query_total))
        if display_start is 0:
            calls = calls[display_start:display_length]
        else:
            calls = calls[display_start:display_length + display_start]
        if calls:
            query_length = calls.count()
        else:
            query_length = 0
        calls = serializers.serialize('json', calls)
        calls = json.loads(calls)
        data = []
        for c in calls:
            call = c['fields']
            call['pk'] = c['pk']
            data.append(call)
        return {
            'query_total': query_total,
            'query_length': query_length,
            'data': data,
        }

    @classmethod
    def get_dynamic_calls_async(self, date_from, date_to):
        date_from = timestamp_to_date(date_from)
        date_to = timestamp_to_date(date_to) + time_delta
        params = dict()
        params['timeStamp__range'] = (date_from, date_to)
        
        # ejecucion de la query
        data = Call.objects.filter(**params).order_by('-timeStamp')
        logger.info(data.count())

        if data:
            return data
        else:
            return None
