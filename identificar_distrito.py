import pandas as pd
from convertir_coordinates import convertir_coordinates
import ast
from shapely.geometry import Point


def coordenadas(string_coordenadas):
    dict = ast.literal_eval(string_coordenadas)
    coordenadas = dict["coordinates"]
    return coordenadas


def tipo_geometry(string_coordenadas):
    dict = ast.literal_eval(string_coordenadas)
    tipo = dict["type"]
    return tipo


def coordenadas_a_string(dict_coordenadas):
    string = ' '.join(dict_coordenadas)
    return string


def asignar_distrito(latitud, longitud, df_poly, cantidad_distritos):

    for n in range(cantidad_distritos):
        if df_poly["poly_final"][n].contains(Point(longitud, latitud)):
            break
    return df_poly["NOMBDIST"][n], df_poly["NOMBPROV"][n], df_poly["NOMBDEP"][n]


def identificar_distrito(ruta_csv_distritos, main_df):
    #df_goldcar = pd.read_csv("goldcar.csv")
    df = pd.read_csv(ruta_csv_distritos, sep=";")
    # 1 Geo Shape
    # 3 NOMBDEP
    # 5 NOMBPROV
    # 7 NOMBDIST
    # 8 CAPITAL
    # 9 UBIGEO
    # 13 DESCRIPCIO

    df = df.iloc[:, [1, 3, 5, 7, 8, 9, 13]]
    df["tipo_geometry"] = df.apply(
        lambda x: tipo_geometry(x["Geo Shape"]), axis=1)
    df["coordenadas"] = df.apply(lambda x: coordenadas(x["Geo Shape"]), axis=1)
    df["poly_final"] = df.apply(lambda x: convertir_coordinates(
        x["coordenadas"], x["tipo_geometry"]), axis=1)
    df.drop(["tipo_geometry", "coordenadas", "Geo Shape"], axis=1)
    cantidad_distritos = len(df)
    main_df[["distrito", "provincia", "region"]] = main_df.apply(lambda x: asignar_distrito(
        x["latitud"], x["longitud"], df, cantidad_distritos), axis='columns', result_type='expand')
    return main_df
    #main_df.to_csv("distritos_goldcar.csv", index=False)
