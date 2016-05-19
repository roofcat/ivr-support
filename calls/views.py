# -*- coding: utf-8 -*-


import json
import logging


from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Call
from .serializers import CallInputIVRSerializer
from utils.generics import string_date_to_datetime


logger = logging.getLogger("CallApiApp")


class CallInputIVRView(APIView):
    serializer_class = CallInputIVRSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        logger.info("Imprimiendo el request")
        logger.info(request.data)
        call = self.serializer_class(data=request.data)
        if call.is_valid():
            call.save()
            logger.info('Se ha creado la llamada')
            logger.info(call.data)
            return Response({'status': 200})
        else:
            logger.error(call.errors)
            return Response(call.errors)


class CallInputTemplateView(TemplateView):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CallInputTemplateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        data = {
            'mensaje': 'Metodo GET no implementado',
        }
        return HttpResponse(json.dumps(data))

    def post(self, request, *args, **kwargs):
        logger.info("Entrando a CallInputTemplateView")
        logger.info("Recibiendo request")
        logger.info(type(request.body))
        logger.info(request.body)

        try:
            request_body = json.loads(request.body.decode('utf-8'))
            logger.info("Imprimiendo json request_body")
            logger.info(request_body)
        except Exception, e:
            data = {
                "mensaje": "error al procesar JSON \n" + e
            }
            return HttpResponse(json.dumps(data), status=500)

        try:
            collection = str(request_body['collection']).decode('utf-8')
            
            sp = str(request_body['sp']).decode('utf-8')
            
            key = request_body['key']
            
            beginCall = str(request_body['beginCall']).decode('utf-8')
            beginCall = string_date_to_datetime(beginCall)

            origin = request_body['origin']

            callAnswered = str(request_body['callAnswered']).decode('utf-8')
            if callAnswered == 'true':
                callAnswered = True
            else:
                callAnswered = False

            lastState = str(request_body['lastState']).decode('utf-8')

            IVRSel = request_body['IVRSel']
            
            dialIntentBegin1 = str(request_body['dialIntentBegin1']).decode('utf-8')
            dialIntentBegin1 = string_date_to_datetime(dialIntentBegin1)

            dialIntentCaller1 = request_body['dialIntentCaller1']
            dialIntentCalled1 = request_body['dialIntentCalled1']
            
            dialIntentEnd1 = str(request_body['dialIntentEnd1']).decode('utf-8')
            dialIntentEnd1 = string_date_to_datetime(dialIntentEnd1)

            dialIntentAnswered1 = str(request_body['dialIntentAnswered1']).decode('utf-8')
            if dialIntentAnswered1 == 'true':
                dialIntentAnswered1 = True
            else:
                dialIntentAnswered1 = False

            sessionFile = str(request_body['sessionFile']).decode('utf-8')
            
            hc = str(request_body['hc']).decode('utf-8')
            
            routing = str(request_body['routing']).decode('utf-8')
            
            name = str(request_body['name']).decode('utf-8')
            
            endDial = str(request_body['endDial']).decode('utf-8')
            endDial = string_date_to_datetime(endDial)

            timeStamp = str(request_body['timeStamp']).decode('utf-8')
            timeStamp = string_date_to_datetime(timeStamp)

            # proceso de guardado
            new_call = Call.objects.create(
                collection=collection,
                sp=sp,
                key=key,
                beginCall=beginCall,
                origin=origin,
                callAnswered=callAnswered,
                lastState=lastState,
                IVRSel=IVRSel,
                dialIntentBegin1=dialIntentBegin1,
                dialIntentCaller1=dialIntentCaller1,
                dialIntentCalled1=dialIntentCalled1,
                dialIntentEnd1=dialIntentEnd1,
                dialIntentAnswered1=dialIntentAnswered1,
                sessionFile=sessionFile,
                hc=hc,
                routing=routing,
                name=name,
                endDial=endDial,
                timeStamp=timeStamp,
            )
            new_call.save()
            data = {
                "mensaje": "objeto creado exitosamente",
                "objeto": model_to_dict(new_call)
            }
            return JsonResponse(data)
        except Exception, e:
            logger.error(e)
            return HttpResponse(e, status=500)
