# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from datetime import datetime
import calendar


from django.db import models


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

    def __unicode__():
        return "{0} - {1} - {2}".format(timestamp, origin, call_answered)
