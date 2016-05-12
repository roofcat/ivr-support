# -*- coding: utf-8 -*-


import logging


from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import CallInputIVRSerializer


logger = logging.getLogger("CallApiApp")


class CallInputIVRView(APIView):
    serializer_class = CallInputIVRSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        call = self.serializer_class(data=request.data)
        if call.is_valid():
            call.save()
            logger.info('Se ha creado la llamada')
            logger.info(call.data)
            return Response({'status': 200})
        else:
            logger.error(call.errors)
            return Response(call.errors)
