# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from datetime import datetime
import calendar
import json
import logging


from django.db import models
from django.core import serializers


from utils import timestamp_to_date
from utils import create_tablib


logger = logging.getLogger("CallsApp")


class Call(models.Model):
    begin_call = models.DateTimeField(
        null=True, blank=True, verbose_name='Inicio de llamada')
    origin = models.BigIntegerField(
        null=True, blank=True, verbose_name='Número que llama')
    call_answered = models.BooleanField(
        default=False, verbose_name='Contestó el IVR')
    last_state = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Opción seleccioanda del IVR')
    ivr_sel = models.BigIntegerField(
        null=True, blank=True, verbose_name='Tecla que presionó')
    dial_intent_begin = models.DateTimeField(
        null=True, blank=True, verbose_name='Hora de inicio de llamado de tranferencia')
    dial_intent_caller = models.BigIntegerField(
        null=True, blank=True, verbose_name='Número que llama')
    dial_intent_called = models.BigIntegerField(
        null=True, blank=True, verbose_name='Número a donde se transfiere la llamada')
    dial_intent_end = models.DateTimeField(
        null=True, blank=True, verbose_name='Término de la llamada de transferencia')
    dial_intent_answered = models.BooleanField(
        default=False, verbose_name='La transferencia fue contestada')
    session_file = models.FileField(upload_to='audio/%Y/%m/%d{0}'.format(
        calendar.timegm(datetime.utcnow().utctimetuple())),
        null=True, verbose_name='Archivo de audio')
    hc = models.CharField(max_length=150, null=True, blank=True,
                          verbose_name='Código de término de la llamada')
    end_dial = models.DateTimeField(
        null=True, blank=True, verbose_name='Término de la llamada')
    timestamp = models.DateTimeField(
        null=True, blank=True, verbose_name='Fecha del registro')

    def __unicode__(self):
        return "{0} - {1} - {2}".format(self.timestamp, self.origin, self.call_answered)

    @classmethod
    def get_dynamic_calls(self, date_from, date_to, display_start, display_length):
        date_from = timestamp_to_date(date_from)
        date_to = timestamp_to_date(date_to)
        params = dict()
        params['timestamp__range'] = (date_from, date_to)

        # ejecución de la query
        calls = Call.objects.filter(**params).order_by('-timestamp')
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
        logger.info(calls)
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
        date_to = timestamp_to_date(date_to)
        params = dict()
        params['timestamp__range'] = (date_from, date_to)
        
        # ejecucion de la query
        data = Call.objects.filter(**params).order_by('-timestamp')

        # preparacion del reporte
        report = create_tablib(data)

        # creación de objeto
        mail = {
            'name': 'reporte.xlsx',
            'report': report.xlsx,
        }
