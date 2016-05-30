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
                "mensaje": "error al procesar JSON"
            }
            return HttpResponse(json.dumps(data), status=500)

        try:
            collection = str(request_body['collection']).decode('utf-8')
            
            try:
                sp = str(request_body['sp']).decode('utf-8')
            except:
                sp = None
            
            key = request_body['key']
            
            beginCall = str(request_body['beginCall']).decode('utf-8')
            beginCall = string_date_to_datetime(beginCall)

            try:
                origin = request_body['origin']
                origin = int(origin, base=10)
            except:
                origin = 0

            try:
                callAnswered = str(request_body['callAnswered']).decode('utf-8')
                if callAnswered == 'true':
                    callAnswered = True
                else:
                    callAnswered = False
            except:
                callAnswered = False

            try:
                lastState = str(request_body['lastState']).decode('utf-8')
            except:
                lastState = None

            try:
                IVRSel = request_body['IVRSel']
                if len(IVRSel) > 0:
                    IVRSel = int(IVRSel, base=10)
                else:
                    IVRSel = None
            except:
                IVRSel = None
            
            try:
                dialIntentBegin1 = str(request_body['dialIntentBegin1']).decode('utf-8')
                dialIntentBegin1 = string_date_to_datetime(dialIntentBegin1)
            except:
                dialIntentBegin1 = None

            try:
                dialIntentCaller1 = request_body['dialIntentCaller1']
                dialIntentCaller1 = int(dialIntentCaller1, base=10)
            except:
                dialIntentCaller1 = None

            try:
                dialIntentCalled1 = request_body['dialIntentCalled1']
                dialIntentCalled1 = int(dialIntentCalled1, base=10)
            except:
                dialIntentCalled1 = None
            
            try:
                dialIntentEnd1 = str(request_body['dialIntentEnd1']).decode('utf-8')
                dialIntentEnd1 = string_date_to_datetime(dialIntentEnd1)
            except:
                dialIntentEnd1 = None

            try:
                dialIntentAnswered1 = str(request_body['dialIntentAnswered1']).decode('utf-8')
                if dialIntentAnswered1 == 'true':
                    dialIntentAnswered1 = True
                else:
                    dialIntentAnswered1 = False
            except:
                dialIntentAnswered1 = False

            try:
                sessionFile = str(request_body['sessionFile']).decode('utf-8')
            except:
                sessionFile = None
            
            try:
                hc = str(request_body['hc']).decode('utf-8')
            except:
                hc = None
            
            try:
                routing = str(request_body['routing']).decode('utf-8')
            except Exception, e:
                routing = None
            
            try:
                name = str(request_body['name']).decode('utf-8')
            except:
                name = None
            
            endDial = str(request_body['endDial']).decode('utf-8')
            endDial = string_date_to_datetime(endDial)

            try:
                timeStamp = str(request_body['timeStamp']).decode('utf-8')
                timeStamp = string_date_to_datetime(timeStamp)
            except Exception, e:
                raise e

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
