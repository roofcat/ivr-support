# -*- coding: utf-8 -*-


import logging


from celery import Celery


from calls.models import Call
from utils import create_tablib
from utils import SGEmailClient
from utils import timestamp_to_date


logger = logging.getLogger('CeleryTasks')
app = Celery('reportes', backend='amqp', broker='amqp://')


@app.task
def send_report_by_sendgrid(user, date_from, date_to):
    logger.info('Entrando a send_report_by_sendgrid')

    parameters = dict()
    parameters['date_from'] = date_from
    parameters['date_to'] = date_to
    # query
    data = Call.get_dynamic_calls_async(**parameters)
    # preparacion del reporte
    report = create_tablib(data)
    logger.info(report)

    if report is not None:
        data = {
            'name': 'reporte_llamadas.xlsx',
            'report': report.xlsx,
        }
        # preparación para enviar correo
        mail = SGEmailClient()
        mail.send_report_email(user, data)
    else:
        logger.info('no hay datos para crear excel')


@app.task
def test_hola_mundo():
    logger.info("COLA DE hola mundo")
    print "hola"
