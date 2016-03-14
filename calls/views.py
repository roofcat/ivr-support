# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404


from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import Call
from .serializers import CallInputIVRSerializer


class CallInputIVRView(APIView):
	serializer_class = CallInputIVRSerializer
	permission_classes = (permissions.AllowAny,)

	def get(self, request, id=None, format=None):
		if id is not None:
			call = get_object_or_404(Call, pk=id)
			response = self.serializer_class(call, many=False)
		else:
			calls = Call.objects.all()
			response = self.serializer_class(calls, many=True)
		return Response(response.data)

	def post(self, request, format=None):
		call = self.serializer_class(data=request.data)
		if call.is_valid():
			call.save()
			print call
			return Response({'status': 200})
		else:
			print call.errors
			return Response(call.errors)
