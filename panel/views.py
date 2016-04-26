# -*- coding: utf-8 -*-


import logging
import json


from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import TemplateView


from authentications.views import LoginRequiredMixin
from calls.models import Call
from utils import tasks


logger = logging.getLogger("PanelApp")


class HomePanelView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/index.html'

    def get(self, request, *args, **kwargs):
        logger.info("Entrando a HomePanelView")
        logger.info("Usuario {0}".format(request.user))
        return render(request, self.template_name)


class CallDetailView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            pk = request.GET['pk']
            if pk:
                pk = int(pk, base=10)
                call = get_object_or_404(Call, pk=pk)
                call = model_to_dict(call)
                call['session_file'] = '/media/' + call['session_file'].name
                return JsonResponse(call)
        except Exception, e:
            logger.error(e)


class PanelReportExport(LoginRequiredMixin, TemplateView):

    def get(self, request, date_from, date_to, *args, **kwargs):
        logger.info("Entrando a PanelReportExport")
        parameters = dict()
        parameters['date_from'] = int(date_from, base=10)
        parameters['date_to'] = int(date_to, base=10)
        parameters['user'] = request.user.id
        try:
            tasks.send_report_by_sendgrid(**parameters)
        except Exception, e:
            logger.error(e)
        return HttpResponse()


class DynamicSearchPanelView(LoginRequiredMixin, TemplateView):

    def get(self, request, date_from, date_to, *args, **kwargs):
        logger.info("Entrando a DynamicSearchPanelView")
        parameters = dict()
        parameters['date_from'] = int(date_from, base=10)
        parameters['date_to'] = int(date_to, base=10)
        # parametros de jquery datatables
        echo = request.GET['sEcho']
        display_start = request.GET['iDisplayStart']
        display_length = request.GET['iDisplayLength']
        parameters['display_start'] = int(display_start, base=10)
        parameters['display_length'] = int(display_length, base=10)

        # query
        calls = Call.get_dynamic_calls(**parameters)
        # response
        data = {
            'sEcho': echo,
            'data': calls['data'],
            'iTotalDisplayRecords': calls['query_total'],
            'iTotalRecords': calls['query_total'],
        }
        return JsonResponse(data, safe=False)
