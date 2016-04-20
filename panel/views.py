# -*- coding: utf-8 -*-


import logging
import json


from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView

from authentications.views import LoginRequiredMixin
from calls.models import Call


logger = logging.getLogger("PanelApp")


class HomePanelView(LoginRequiredMixin, TemplateView):
    template_name = 'panel/index.html'

    def get(self, request, *args, **kwargs):
    	logger.info("Entrando a HomePanelView")
    	logger.info("Usuario {0}".format(request.user))
        return render(request, self.template_name)


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
