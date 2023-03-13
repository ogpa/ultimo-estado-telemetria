import mygeotab
from datetime import datetime
import pytz


def hoy_geotab():
    tz_Lima = pytz.timezone('America/Lima')
    tiempo_Lima = datetime.now(tz_Lima)
    ahora_geotab = mygeotab.dates.format_iso_datetime(tiempo_Lima)
    # print(ahora_geotab)
    return ahora_geotab


# hoy_geotab()
