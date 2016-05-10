# -*- coding: utf-8 -*-


from rest_framework.serializers import ModelSerializer


from .models import Call


class CallInputIVRSerializer(ModelSerializer):

    class Meta:
        model = Call
        fields = (
            'collection', 'sp', 'key', 'beginCall', 'origin', 'callAnswered', 
            'lastState', 'IVRSel', 'dialIntentBegin1', 'dialIntentCaller1', 
            'dialIntentCalled1', 'dialIntentEnd1', 'dialIntentAnswered1', 
            'sessionFile', 'hc', 'routing', 'name', 'endDial', 'timeStamp', 
        )
