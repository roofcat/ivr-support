# -*- coding: utf-8 -*-


from datetime import datetime
import pytz


tz = pytz.timezone('America/Santiago')


def timestamp_to_date(x, zone=False):
	x = to_unix_timestamp(x)
	if zone:
		return datetime.fromtimestamp(x, tz=tz)
	else:
		return datetime.fromtimestamp(x)


def to_unix_timestamp(x):
	if x is not None:
		if len(str(x)) > 10:
			x = int(str(x)[0:10], base=10)
		return x
	else:
		return None


def date_to_format(x):
	return datetime.strftime(x, '%Y-%m-%d %H:%M:%S')
