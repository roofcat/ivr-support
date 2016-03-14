# -*- coding: utf-8 -*-


from rest_framework.serializers import ModelSerializer, FileField


from .models import Call


class CallInputIVRSerializer(ModelSerializer):
    session_file = FileField(
        use_url=False, max_length=None, allow_null=True, allow_empty_file=True)

    class Meta:
        model = Call
        fields = (
            'begin_call', 'call_answered', 'collection', 'dial_intent_answered',
            'dial_intent_begin', 'dial_intent_called', 'dial_intent_caller',
            'dial_intent_end', 'end_dial', 'hc', 'ivr_sel', 'key', 'last_state', 
            'name', 'origin', 'routing', 'session_file', 'sp', 'timestamp',
        )
