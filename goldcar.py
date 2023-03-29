from login_goldcar import login_goldcar
from focus_reportes import focus_reportes
from generar_reporte_ultimos_reportes import generar_reporte_ultimos_reportes
from descargar_reporte_ultimos_reportes import descargar_reporte_ultimos_reportes
from obtener_reporte import crear_csv
from generar_reporte_odometro import generar_reporte_odometro
from descargar_reporte_odometro import descargar_reporte_odometro
from focus_monitoring import focus_monitoring
from duplicate import duplicate
from obtener_odometros import obtener_odometros


def scan_goldcar():
    sid = login_goldcar()
    print(sid)
    #29/03/2023 Goldcar cambió el método de hacer focus
    focus_reportes(sid)
    # Aquí se coloca el from to de las fechas
    generar_reporte_ultimos_reportes("Hoy", sid)
    path_ultimos_reportes = descargar_reporte_ultimos_reportes(sid)

    focus_monitoring(sid)
    resp = duplicate(sid)
    #print(resp) # Da {"error":1}
    df_odometros = obtener_odometros(resp, sid)
    #generar_reporte_odometro("Hoy", sid)
    #path_odometro = descargar_reporte_odometro(sid)

    #goldcar_df = crear_csv(path_ultimos_reportes, path_odometro, "Hoy")
    goldcar_df = crear_csv(path_ultimos_reportes, df_odometros, "Hoy")
    return goldcar_df


# scan_goldcar()
