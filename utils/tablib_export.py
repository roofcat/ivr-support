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

	if data is not None:
		for row in data:
			timeStamp = date_to_format(row.timeStamp)
			if row.beginCall is not None:
				beginCall = date_to_format(row.beginCall)
			else:
				beginCall = ''
			origin = unicode(row.origin)
			if row.callAnswered:
				callAnswered = u'CONTESTADA'
			else:
				callAnswered = u'NO CONTESTADA'
			if row.lastState is not None:
				lastState = unicode(row.lastState)
			else:
				lastState = ''
			if row.IVRSel is not None:
				IVRSel = unicode(row.IVRSel)
			else:
				IVRSel = ''
			if row.dialIntentBegin1 is not None:
				dialIntentBegin1 = date_to_format(row.dialIntentBegin1)
			else:
				dialIntentBegin1 = ''
			if row.dialIntentCaller1 is not None:
				dialIntentCaller1 = unicode(row.dialIntentCaller1)
			else:
				dialIntentCaller1 = ''
			if row.dialIntentCalled1 is not None:
				dialIntentCalled1 = unicode(row.dialIntentCalled1)
			else:
				dialIntentCalled1 = ''
			if row.dialIntentEnd1 is not None:
				dialIntentEnd1 = date_to_format(row.dialIntentEnd1)
			else:
				dialIntentEnd1 = ''
			if row.dialIntentAnswered1:
				dialIntentAnswered1 = u'CONTESTADA'
			else:
				dialIntentAnswered1 = u'NO CONTESTADA'
			if row.hc is not None:
				hc = unicode(row.hc)
			else:
				hc = ''
			if row.endDial is not None:
				endDial = date_to_format(row.endDial)
			else:
				endDial = ''

			data_row = (
				timeStamp, beginCall, origin, callAnswered, lastState, IVRSel,
				dialIntentBegin1, dialIntentCaller1, dialIntentCalled1, dialIntentEnd1,
				dialIntentAnswered1, hc, endDial
			)
			my_tab.append(data_row)
		logger.info('Se generó el excel exitosamente')
		return 	my_tab
	else:
		logger.info('No hay datos para generar excel')
		return None
