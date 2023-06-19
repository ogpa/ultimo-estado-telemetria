import pandas as pd
from datetime import datetime, timezone, timedelta
import boto3
import time
from geotab import scan_geotab
from hunter import scan_hunter
from comsatel import scan_comsatel
from goldcar import scan_goldcar
from hunter_pro import scan_hunter_pro
from identificar_distrito import identificar_distrito
from unzip import unzip
from taller_molina import taller_molina

ZONA_HORARIA = 5
S3_BUCKET_NOMBRE = "apps-mbr-innovacion"
S3_RUTA_FOLDER = "bi-telemetria/ultimo-estado/"
today = datetime.now(timezone.utc)
today = today - timedelta(hours=ZONA_HORARIA)
hoy = today.strftime("%d-%m-%Y")
ruta_zip_distritos = "distritos-peru.zip"
unzip(ruta_zip_distritos)

print("Ejecutando Comsatel.")
start_time = time.time()
comsatel_df = scan_comsatel(hoy)
print("Comsatel tardó %s segundos." % (time.time() - start_time))

# print("Ejecutando Hunter Pro.")
# start_time = time.time()
# hunter_pro_df = scan_hunter_pro(hoy)
# print("Hunter Pro tardó %s segundos." % (time.time() - start_time))

# print("Ejecutando Geotab.")
# start_time = time.time()
# geotab_df = scan_geotab(hoy)
# print("Geotab tardó %s segundos." % (time.time() - start_time))

# print("Ejecutando Goldcar.")
# start_time = time.time()
# goldcar_df = scan_goldcar()
# print("Goldcar tardó %s segundos." % (time.time() - start_time))


# print("Ejecutando Hunter.")
# start_time = time.time()
# hunter_df = scan_hunter(hoy)
# print("Hunter tardó %s segundos." % (time.time() - start_time))


# dfs = [geotab_df]
dfs = [hunter_pro_df, goldcar_df, comsatel_df, hunter_df, geotab_df]
# dfs = [hunter_df, geotab_df]

main_df = pd.concat(dfs)
# main_df.to_csv("antes_alias.csv", index=False)
# main_df["alias"] = main_df.apply(lambda x: x["alias"].replace(",", ""), axis=1)
main_df = main_df.drop_duplicates(subset="placa", keep="last")

ruta_csv_distritos = "distritos-peru.csv"
main_df["latitud"] = main_df["latitud"].astype(float)
main_df["longitud"] = main_df["longitud"].astype(float)
print("Identificando distritos.")
start_time = time.time()
final_df = identificar_distrito(ruta_csv_distritos, main_df)
print(
    "El bot tardó %s segundos en identificar los distritos."
    % (time.time() - start_time)
)
final_df = taller_molina(final_df)
nombre_archivo = hoy + "_ultimo_estado.csv"
nombre_archivo_s3 = hoy + "_ultimo_estado.csv"
# Reordenar columnas
final_df = final_df[
    [
        "alias",
        "fecha_ultima_actualizacion",
        "latitud",
        "longitud",
        "direccion",
        "odometro",
        "placa",
        "taller_molina",
        "fecha",
        "hora",
        "proveedor",
        "deviceid",
        "database",
        "id",
        "distrito",
        "provincia",
        "region",
    ]
]
final_df.to_csv(nombre_archivo_s3, index=False)

# s3 = boto3.client('s3')
# with open(nombre_archivo_s3, "rb") as f:
#     s3.upload_fileobj(f, S3_BUCKET_NOMBRE, S3_RUTA_FOLDER + nombre_archivo)
