import requests
import urllib
from datetime import datetime
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import os
import openpyxl
filename_horas_trabajadas = "Horas_Trabajadas.xlsx"
filename_kilometraje_horas = "Kilometraje_Horas.xlsx"


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def fecha(delta):
    d = datetime.today() - timedelta(days=delta)
    fecha_ddmmyyyy = d.strftime("%d/%m/%Y")
    return fecha_ddmmyyyy


def convertir_placa(descripcion_vehiculo):
    c = "-"
    pos_guion = descripcion_vehiculo.find(c)
    if pos_guion != -1:
        placa = descripcion_vehiculo[pos_guion-3:pos_guion+4]
    else:
        placa = descripcion_vehiculo
    return placa


def convertir_latitud_longitud(hipervinculo):
    # https://www.google.com/maps?q=-14.09808,-72.30887
    latitud = extraer_texto(hipervinculo, "=", ",")
    longitud = extraer_texto(hipervinculo, ",", "x")
    return latitud, longitud


def ayer():
    d = datetime.today() - timedelta(days=1)
    d_p = d.strftime("%Y%m%d")
    d_df = d.strftime("%d/%m/%Y")
    return d_p, d_df


def procesar_ultimos_reportes(filename_ultimos_reportes):
    wb = openpyxl.load_workbook(filename_ultimos_reportes)
    ws = wb["Últimos datos de la unidad"]
    lista_latitud = []
    lista_longitud = []
    # min_row=2 porque los datos empiezan en la fila 2
    for x in ws.iter_rows(min_col=3, max_col=3, min_row=2):
        # Agrego "x" para que sea fácil encontrarlo
        hipervinculo = x[0].hyperlink.target + "x"
        coordenadas = convertir_latitud_longitud(hipervinculo)
        lista_latitud.append(coordenadas[0])
        lista_longitud.append(coordenadas[1])

    dict_coordenadas = {
        "latitud": lista_latitud,
        "longitud": lista_longitud
    }

    df_coordenadas = pd.DataFrame(dict_coordenadas)
    # print(df_coordenadas)
    df = pd.read_excel(filename_ultimos_reportes, engine="openpyxl",
                       sheet_name="Últimos datos de la unidad")
    # Reemplazo № para poder usar print

    df = df.rename(
        columns={df.columns[0]: "N", df.columns[1]: "placa", df.columns[2]: "fecha_ultima_actualizacion", df.columns[3]: "direccion"})

    df["fecha"] = df.apply(
        lambda x: x["fecha_ultima_actualizacion"][0:10], axis=1)  # extrae la placa
    df["hora"] = df.apply(
        lambda x: x["fecha_ultima_actualizacion"][11:16], axis=1)  # extrae la placa
    df_ultimos_reportes = pd.merge(df, df_coordenadas,
                                   left_index=True, right_index=True)
    df_ultimos_reportes["proveedor"] = "goldcar"
    del df_ultimos_reportes[df_ultimos_reportes.columns[0]]
    return df_ultimos_reportes


def procesar_odometros(filename_odometro):
    df = pd.read_excel(filename_odometro, engine="openpyxl",
                       sheet_name="Odometro")
    df = df.rename(
        columns={df.columns[0]: "N", df.columns[1]: "placa", df.columns[2]: "odometro"})
    df_odometros = df
    del df_odometros[df_odometros.columns[0]]
    return df_odometros


def procesar_df_odometros(df_odometro):
    # print(df_odometro)
    df_odometro["placa"] = df_odometro["placa"].astype(str)
    # df = df_odometro.drop(
    #    df_odometro[df_odometro['placa'].str.len() > 7].index, inplace=True)
    mask = (df_odometro['placa'].str.len() < 8)
    df = df_odometro.loc[mask]
    # df.reset_index(drop=True)
    return df


def crear_csv(filename_ultimos_reportes, df_odometro, hora_reporte):
    df_ur = procesar_ultimos_reportes(filename_ultimos_reportes)
    #df_od = procesar_odometros(filename_odometro)
    # Se eliminan "placas" que son nombre de grupos
    # print(type(df_odometro))
    df_od = procesar_df_odometros(df_odometro)
    # print(type(df_ur))
    # print(df_ur)
    # print(type(df_od))
    # print(df_od)
    df_goldcar = pd.merge(df_ur, df_od, on="placa")
    df_goldcar.to_csv("goldcar.csv", index=False)
    return df_goldcar


#crear_csv("Ultimos_Reportes_Goldcar.xlsx", "Odometro_Goldcar.xlsx", "Hoy")
