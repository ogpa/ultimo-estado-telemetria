from login_hunter_pro import login_hunter_pro
from ultimo_estado_hunter_pro import ultimo_estado_hunter_pro
import pandas as pd

lista_usuario = [["mbrenting.dpizarro", "mbrenting2022!"],
                 ["dpizarros", "renting22!"]]


def convertir_placa(alias):
    c = "-"
    pos_guion = alias.find(c)
    if pos_guion != -1:
        placa = alias[pos_guion-3:pos_guion+4]
    else:
        placa = alias
    return placa


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def convertir_fecha(ultimo_reporte):
    fecha = extraer_texto(ultimo_reporte, "", " ")
    return fecha


def convertir_hora(ultimo_reporte):
    temp_ultimo_reporte = ultimo_reporte + "x"
    hora = extraer_texto(temp_ultimo_reporte, " ", "x")
    return hora[:5]


def scan_hunter_pro(hora_reporte):

    df_hunter_pro_columnas = [
        "placa", "alias", "fecha", "proveedor"]

    df_hunter_pro = pd.DataFrame(columns=df_hunter_pro_columnas)

    for u in lista_usuario:
        l = login_hunter_pro(u)
        df_ue = ultimo_estado_hunter_pro(l)
        # print(df_ue)
        #df_pr = productividad(l, hora_reporte)
        # print(df_pr)
        df_hunter_pro = pd.concat([df_hunter_pro, df_ue])
    df_hunter_pro["proveedor"] = "hunter_pro"
    df_hunter_pro["placa"] = df_hunter_pro.apply(
        lambda x: convertir_placa(x["alias"]), axis=1)
    df_hunter_pro["fecha"] = df_hunter_pro.apply(
        lambda x: convertir_fecha(x["fecha_ultima_actualizacion"]), axis=1)
    df_hunter_pro["hora"] = df_hunter_pro.apply(
        lambda x: convertir_hora(x["fecha_ultima_actualizacion"]), axis=1)
    df_hunter_pro.to_csv("hunter_pro_prueba.csv", index=False)
    return df_hunter_pro


# scan_hunter_pro("Hoy")
