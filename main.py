import pandas as pd
from datetime import datetime, timezone, timedelta
import boto3
from botocore.exceptions import ClientError
import time
from geotab import scan_geotab
from hunter import scan_hunter
from comsatel import scan_comsatel

ZONA_HORARIA = 5
S3_BUCKET_NOMBRE = "apps-mbr"
S3_RUTA_FOLDER = "bi-telemetria/telemetria-sin-reportar/csv/"
today = datetime.now(timezone.utc)
today = today - timedelta(hours=ZONA_HORARIA)
hoy = today.strftime("%d-%m-%Y")

print("Ejecutando Geotab.")
start_time = time.time()
geotab_df = scan_geotab(hoy)
print("Geotab tardó %s segundos." % (time.time() - start_time))

print("Ejecutando Comsatel.")
start_time = time.time()
comsatel_df = scan_comsatel(hoy)
print("Comsatel tardó %s segundos." % (time.time() - start_time))



print("Ejecutando Hunter.")
start_time = time.time()
hunter_df = scan_hunter(hoy)
print("Hunter tardó %s segundos." % (time.time() - start_time))

dfs = [hunter_df, geotab_df, comsatel_df]
#dfs = [hunter_df, geotab_df]
main_df = pd.concat(dfs)
main_df = main_df.drop_duplicates(subset="placa", keep="last")
nombre_archivo = hoy + "_data_telemetria_sin_reportar.csv"
nombre_archivo_s3 = hoy + "_data_telemetria_sin_reportar.csv"
main_df.to_csv(nombre_archivo_s3, index=False)

# s3 = boto3.client('s3')
# with open(nombre_archivo_s3, "rb") as f:
#     s3.upload_fileobj(f, S3_BUCKET_NOMBRE, S3_RUTA_FOLDER + nombre_archivo)

