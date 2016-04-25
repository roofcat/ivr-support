# -*- coding: utf-8 -*-


from datetime import datetime
import logging
import tablib


from utils import date_to_format


logger = logging.getLogger('TabLibExport')


def create_tablib(data):
	my_tab = tablib.Dataset(title="Registro Llamadas")
	my_tab.headers = (
		'Fecha registro', 'Fecha inicio llamada', 'No que llama', 'Conteto IVR',
		'Opcion IVR', 'Anexo', 'Fecha llamada transferencia', 'No que llama', 
		'No donde se transfiere llamada', 'Fecha termino llamada transferencia',
		'Transferencia contestada', 'Código termino llamada', 'Fecha termino llamada'
	)

	if data:
		for row in data:
			logger.info(row)
			timestamp = date_to_format(row.timestamp)
			begin_call = date_to_format(row.begin_call)
			origin = unicode(row.origin)
			if row.call_answered:
				call_answered = u'CONTESTADA'
			else:
				call_answered = u'NO CONTESTADA'
			last_state = unicode(row.last_state)
			ivr_sel = unicode(row.ivr_sel)
			dial_intent_begin = date_to_format(row.dial_intent_begin)
			dial_intent_caller = unicode(row.dial_intent_caller)
			dial_intent_called = unicode(row.dial_intent_called)
			dial_intent_end = date_to_format(row.dial_intent_end)
			if row.dial_intent_answered:
				dial_intent_answered = u'CONTESTADA'
			else:
				dial_intent_answered = u'NO CONTESTADA'
			hc = unicode(row.hc)
			end_dial = date_to_format(row.end_dial)

			data_row = (
				timestamp, begin_call, origin, call_answered, last_state, ivr_sel,
				dial_intent_begin, dial_intent_caller, dial_intent_called, dial_intent_end,
				dial_intent_answered, hc, end_dial
			)
			my_tab.append(data_row)
		return 	my_tab
	else:
		return None
