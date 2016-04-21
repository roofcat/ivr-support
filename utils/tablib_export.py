from datetime import datetime
import logging
import tablib


logger = logging.getLogger('TabLibExport')


from .generics import timestamp_to_date


def create_tablib(data):
	my_tab = tablib.Dataset(title="Registro Llamadas")
	my_tab.headers = (
		'Fecha registro', 'Inicio llamada', 'N que llama', 'Respondio IVR', 
		'Opcion IVR Seleccionada', 'Anexo', 'Fecha inicio de llamada transferencia',
		'N que llama', 'N a donde se transfiere llamada', 'Termino de llamada de transferencia',
		'Transferencia contestada', 'Codigo de termino de llamada'
	)

	if data:
		for row in data:
			timestamp = timestamp_to_date(row.timestamp)
			begin_call = timestamp_to_date(row.begin_call)
			origin = unicode(row.origin)
			if row.call_answered:
				call_answered = u'CONTESTADA'
			else:
				call_answered = u'NO CONTESTADA'
			last_state = unicode(row.last_state)
			ivr_sel = unicode(row.ivr_sel)
			dial_intent_begin = timestamp_to_date(row.dial_intent_begin)
			dial_intent_caller = unicode(row.dial_intent_caller)
			dial_intent_called = unicode(row.dial_intent_called)
			dial_intent_end = timestamp_to_date(row.dial_intent_end)
			if row.dial_intent_answered:
				dial_intent_answered = u'CONTESTADA'
			else:
				dial_intent_answered = u'NO CONTESTADA'
			hc = unicode(row.hc)
			end_dial = timestamp_to_date(row.end_dial)

			data_row = (
				timestamp, begin_call, origin, call_answered, last_state, ivr_sel,
				dial_intent_begin, dial_intent_caller, dial_intent_called, dial_intent_end,
				dial_intent_answered, hc, end_dial
			)
			my_tab.append(data_row)
		return 	my_tab
	else:
		return None
