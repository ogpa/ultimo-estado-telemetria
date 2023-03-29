import requests
import time
from urllib.parse import quote
import ast
import json
import pandas as pd
GOLD_URL_WIALON = "https://hst-api.wialon.com"
GOLD_URL_WIALON_POST = "https://hst-api.wialon.com/wialon/post.html"
LONGITUD_IDS = 8

lista_ids = []


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def epoch():
    epoch = int(time.time())
    return epoch


def extraer_ids(respuesta_duplicate):
    str_mongr = extraer_texto(respuesta_duplicate, '"mongr":', ',"')
    #print(str_mongr)
    # Los ids empiezan con 2 y tienen longitud de 8
    pos_2_inicio = str_mongr.find("2")
    while pos_2_inicio != -1:
        id = str_mongr[pos_2_inicio:pos_2_inicio + LONGITUD_IDS]
        nueva_posicion_inicial = pos_2_inicio + LONGITUD_IDS + 1
        lista_ids.append(id)
        pos_2_inicio = str_mongr.find("2", nueva_posicion_inicial)

    return lista_ids


def extraer_odometros(lista_ids, sid):
    url_Batch = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/batch&sid=" + sid
    lista_ids_query = ""
    cabecera_ids_query = '{"id":'
    pie_ids_query = ',"detect":{"sensors,lls,ignition":0}}'
    for x in range(len(lista_ids)):
        lista_ids_query = lista_ids_query + cabecera_ids_query + \
            lista_ids[x] + pie_ids_query + ','

    lista_ids_query = lista_ids_query[:-1]
    #print(lista_ids_query)
    # La lista de ids query debe tener el formato {"id":22833343,"detect":{"sensors,lls,ignition":0}},{"id":22786556,"detect":{"sensors,lls,ignition":0}}
    payload_Batch = quote('params={"params":[{"svc":"events/update_units","params":{"mode":"add","units":[',
                          safe="=&") + lista_ids_query + quote(']}}],"flags":0}&sid=', safe="=&") + sid
    # 'params=%7B%22params%22%3A%5B%7B%22svc%22%3A%22events%2Fupdate_units%22%2C%22params%22%3A%7B%22mode%22%3A%22add%22%2C%22units%22%3A%5B%7B%22id%22%3A' + \
    #    id_prueba + '%2C%22detect%22%3A%7B%22sensors%2Clls%2Cignition%22%3A0%7D%7D%5D%7D%7D%5D%2C%22flags%22%3A0%7D&sid=' + sid
    # payload_Batch = urllib.parse.quote(
    #    '{"params":[{"svc":"events/update_units","params":{"mode":"add","units":[{"id":22829325,"detect":{"sensors,lls,ignition":0}}]}}],"flags":0}', safe="")
    headers_Batch = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://hst-api.wialon.com',
        'referer': 'https://hst-api.wialon.com/wialon/post.html',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Batch = requests.request(
        "POST", url_Batch, headers=headers_Batch, data=payload_Batch)

    url_Check_Updates = "https://hst-api.wialon.com/wialon/ajax.html?svc=events/check_updates&sid=" + sid

    payload_Check_Updates = 'params=%7B%22detalization%22%3A3%7D&sid=' + sid
    headers_Check_Updates = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://hst-api.wialon.com',
        'referer': 'https://hst-api.wialon.com/wialon/post.html',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Check_Updates = requests.request(
        "POST", url_Check_Updates, headers=headers_Check_Updates, data=payload_Check_Updates)
    # print("Odómetro de todos los IDs")
    # print(response_Check_Updates.text)

    dict_odometros = ast.literal_eval(response_Check_Updates.text)
    lista_ids_final = []
    lista_odometros = []
    for x in range(len(lista_ids)):

        # print(dict_odometros[lista_ids[x]][0]["sensors"]["2"]["value"])
        try:
            # lista_ids.index(dict_odometros[lista_ids[x]])
            if dict_odometros[lista_ids[x]][0]["sensors"]["2"]["type"] == 3:
                lista_odometros.append(
                    dict_odometros[lista_ids[x]][0]["sensors"]["2"]["value"])
            else:
                lista_odometros.append(
                    dict_odometros[lista_ids[x]][0]["sensors"]["5"]["value"])
            # Puedes ser ["sensors"]["5"] también. Con el type:3 se puede descartar
            # 2 type 3 o 5 type 3
            lista_ids_final.append(lista_ids[x])
        except KeyError:
            print(lista_ids[x], " no existe.")

    dict_ids_y_odometros = {
        "id": lista_ids_final,
        "odometro": lista_odometros
    }
    # print(dict_odometros)
    return dict_ids_y_odometros


def extraer_placas(lista_ids, sid):
    url_Batch = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/batch&sid=" + sid

    lista_ids_query = ""
    cabecera_ids_query = '"'
    pie_ids_query = '"'
    for x in range(len(lista_ids)):
        lista_ids_query = lista_ids_query + cabecera_ids_query + \
            lista_ids[x] + pie_ids_query + ','

    lista_ids_query = lista_ids_query[:-1]

    # La lista de ids query debe tener el formato {"id":22833343,"detect":{"sensors,lls,ignition":0}},{"id":22786556,"detect":{"sensors,lls,ignition":0}}
    payload_Batch = quote('params={"params":[{"svc":"core/update_data_flags","params":{"spec":[{"type":"col","data":[',
                          safe="=&") + lista_ids_query + quote('],"flags":4294967295,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"id","data":22630230,"flags":513,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit","flags":8397079,"mode":1}]}},{"svc":"item/update_custom_property","params":{"itemId":22630230,"name":"inf_map","value":""}},{"svc":"render/set_locale","params":{"tzOffset":-134170192,"language":"en","flags":259,"formatDate":"%Y-%m-%E %H:%M:%S"}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":4097,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1048577,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":519,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1031,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit_group","flags":21,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":313,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_unit_group","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"user","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":769,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":66049,"mode":1}]}},{"svc":"core/search_items","params":{"spec":{"itemsType":"avl_resource","propName":"*","propValueMask":"*","sortType":""},"force":1,"flags":1,"from":0,"to":4294967295}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1,"mode":1}]}},{"svc":"core/search_items","params":{"spec":{"itemsType":"avl_retranslator","propName":"*","propValueMask":"*","sortType":""},"force":1,"flags":1,"from":0,"to":4294967295}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_retranslator","flags":1,"mode":1}]}},{"svc":"core/search_items","params":{"spec":{"itemsType":"avl_route","propName":"*","propValueMask":"*","sortType":""},"force":1,"flags":1,"from":0,"to":4294967295}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_route","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":33281,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":131585,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":2097665,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":8389121,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":8197,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"user","flags":2053,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":49439,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":1,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":32769,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":458783,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":131073,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":14680095,"mode":1}]}},{"svc":"core/update_data_flags","params":{"spec":[{"type":"type","data":"avl_resource","flags":6291487,"mode":1}]}},{"svc":"core/get_hw_types","params":{"includeType":true}}],"flags":0}&sid=', safe="=&") + sid
    headers_Batch = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://hst-api.wialon.com',
        'referer': 'https://hst-api.wialon.com/wialon/post.html',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Batch = requests.request(
        "POST", url_Batch, headers=headers_Batch, data=payload_Batch)

    f = response_Batch.text
    dict_temp = f.replace('\\', "")
    dict_temp = dict_temp.replace('"{', "{")
    dict_temp = dict_temp.replace('}"', "}")
    dict_temp = dict_temp.replace('"[', "[")
    dict_temp = dict_temp.replace(']"', "]")

    dict = json.loads(dict_temp)
    lista_ids = []
    lista_placas = []

    for d in dict:
        for sd in d:
            try:
                lista_placas.append(sd["d"]["nm"])
                lista_ids.append(sd["i"])
            except Exception as e:
                pass

    dict_ids_y_placas = {
        "id": lista_ids,
        "placa": lista_placas
    }
    # print(len(lista_ids))
    # print(lista_ids)
    # print(len(lista_placas))
    # print(lista_placas)
    return dict_ids_y_placas


def obtener_odometros(respuesta_duplicate, sid):
    # Obtener lista_ids
    lista_ids = extraer_ids(respuesta_duplicate)
    dict_ids_y_odometros = extraer_odometros(lista_ids, sid)
    dict_ids_y_placas = extraer_placas(lista_ids, sid)
    df_odometros = pd.DataFrame(dict_ids_y_odometros)
    df_placas = pd.DataFrame(dict_ids_y_placas)
    df_placas["id"] = df_placas["id"].astype(str)
    #print(type(df_odometros["id"][1]))
    #print(df_odometros)
    #print(type(df_placas["id"][1]))
    #print(df_placas)
    df_ids_placas_odometros = pd.merge(df_odometros, df_placas, on=["id"])
    return df_ids_placas_odometros
