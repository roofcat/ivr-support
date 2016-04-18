from datetime import datetime
import pytz


tz = pytz.timezone('America/Santiago')


def timestamp_to_date(x):
	x = to_unix_timestamp(x)
	return datetime.fromtimestamp(x, tz=tz)


def to_unix_timestamp(x):
	if x is not None:
		if len(str(x)) > 10:
			x = int(str(x)[0:10], base=10)
		return x
	else:
		return None
