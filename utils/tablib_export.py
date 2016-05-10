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
			beginCall = date_to_format(row.beginCall)
			origin = unicode(row.origin)
			if row.callAnswered:
				callAnswered = u'CONTESTADA'
			else:
				callAnswered = u'NO CONTESTADA'
			lastState = unicode(row.lastState)
			IVRSel = unicode(row.IVRSel)
			dialIntentBegin1 = date_to_format(row.dialIntentBegin1)
			dialIntentCaller1 = unicode(row.dialIntentCaller1)
			dialIntentCalled1 = unicode(row.dialIntentCalled1)
			dialIntentEnd1 = date_to_format(row.dialIntentEnd1)
			if row.dialIntentAnswered1:
				dialIntentAnswered1 = u'CONTESTADA'
			else:
				dialIntentAnswered1 = u'NO CONTESTADA'
			hc = unicode(row.hc)
			endDial = date_to_format(row.endDial)

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
