import mygeotab
import pandas as pd
from obtener_fecha_y_hora import obtener_fecha_y_hora
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from hoy_geotab import hoy_geotab
from asignar_region import asignar_region
POLY_TALLER_MOLINA = Polygon([(-12.071496, -76.955457), (-12.071008, -76.954843),
                              (-12.070704, -76.953837), (-12.072157, -76.953322), (-12.0726576, -76.954998)])
ODOMETRO_METROS_A_KILOMETROS = 1000

dbs = ["mibanco", "sanfernando", "farmacias_peruanas", "sandvik_peru", "mitsuidelperu", "grio", "atlas_copco_peru", "iess", "bureauveritas", "cofasa", "mobilitylatam", "tnc_contratistas",
       "esencia_inmobiliaria", "samsungperu", "emasa_peru", "agricolachira", "car_sharing", "ponedora", "grupopacasmayo", "mbs_peru", "hipraperu", "bimbo_peru", "supermercados_peruanos"]

#dbs = ["cofasa"]


def scan_geotab(hoy):

    lista_fecha = []
    lista_hora = []
    lista_deviceid = []
    lista_latitud = []
    lista_longitud = []
    lista_alias = []
    lista_placa = []
    lista_tallermolina = []
    lista_proveedor = []
    #lista_region = []
    lista_odometro = []
    lista_deviceid_temp = []
    lista_database_temp = []
    cant_dbs = len(dbs)
    ahora_geotab = hoy_geotab()
    lista_database = []
    for x in range(cant_dbs):
        print(dbs[x])
        api = mygeotab.API(username='bot-telemetria@mb-renting.com',
                           password='FlotasMBRenting2k23$', database=dbs[x])
        credenciales = api.authenticate()
        dsi = api.get('DeviceStatusInfo')

        multi_calls = []
        multi_calls_odometro = []
        multi_calls.clear()
        multi_calls_odometro.clear()

        for s in dsi:
            result_fechahora = obtener_fecha_y_hora(s["dateTime"])
            lista_fecha.append(result_fechahora[0])
            lista_hora.append(result_fechahora[1])
            lista_deviceid.append(s["device"]["id"])
            lista_latitud.append(s["latitude"])
            lista_longitud.append(s["longitude"])
            lista_proveedor.append("geotab")
            lista_database.append(dbs[x])
            lista_tallermolina.append(POLY_TALLER_MOLINA.contains(
                Point(s["latitude"], s["longitude"])))
            #r = asignar_region(s["latitude"], s["longitude"])
            # lista_region.append(r)
            multi_calls.append(
                ["Get", dict(typeName="Device", search={"id": s["device"]["id"]})])

            # multi_calls_odometro.append(["Get", dict(typeName="StatusData", search={"fromDate": ahora_geotab, "toDate": ahora_geotab, "deviceSearch": {
            #                             "id": s["device"]["id"]}, "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})])
            multi_calls_odometro.append(["Get", dict(typeName="StatusData", search={"fromDate": ahora_geotab, "toDate": ahora_geotab, "deviceSearch": {
                                        "id": s["device"]["id"]}, "diagnosticSearch": {"id": "DiagnosticRawOdometerId"}})])
            # DiagnosticOdometerAdjustmentId
        r_multi = api.multi_call(multi_calls)
        r_multi_odometro = api.multi_call(multi_calls_odometro)
        # print(r_multi_odometro)
        for r in r_multi:
            lista_placa.append(r[0]["licensePlate"])
            lista_alias.append(r[0]["name"])

        for r_o in r_multi_odometro:
            if len(r_o) > 0:
                deviceid = r_o[0]["device"]["id"]
                lista_deviceid_temp.append(deviceid)
                lista_database_temp.append(dbs[x])
                odometro = r_o[0]["data"]
                lista_odometro.append(
                    odometro / ODOMETRO_METROS_A_KILOMETROS)

    dict_odometro = {
        "deviceid": lista_deviceid_temp,
        "odometro": lista_odometro,
        "database": lista_database_temp
    }

    dict_datos = {
        "alias": lista_alias,
        "placa": lista_placa,
        "fecha": lista_fecha,
        "hora": lista_hora,
        "latitud": lista_latitud,
        "longitud": lista_longitud,
        "deviceid": lista_deviceid,
        "taller_molina": lista_tallermolina,
        "proveedor": lista_proveedor,

        "database": lista_database
    }

    df_datos = pd.DataFrame(dict_datos)
    # print(df_datos)
    df_odometro = pd.DataFrame(dict_odometro)
    # print(df_odometro)
    geotab_df = pd.merge(df_datos, df_odometro, on=["deviceid", "database"])
    # print(geotab_df)
    geotab_csv_filename = hoy + "_geotab.csv"
    geotab_df.to_csv(geotab_csv_filename, index=False)
    return geotab_df


scan_geotab("Hoy")
