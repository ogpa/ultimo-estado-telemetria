import requests
import urllib
from extraer_datos_session import extraer_datos_session
import requests

GOLD_URL_LOGIN = "http://gpsenperu.gpsgoldcar.com/"
GOLD_URL_OAUTH = "http://gpsenperu.gpsgoldcar.com/oauth.html"
GOLD_URL_MONITORING_LOGIN = "http://gpsenperu.gpsgoldcar.com/frontend/monitoring_login_bac3329bea18834ef562.js"
GOLD_URL_TAG_MANAGER = "http://www.googletagmanager.com/gtm.js?id=GTM-PMGGDP"
GOLD_URL_G_L6 = "http://www.googletagmanager.com/gtag/js?id=G-L6NP7TDMF6&l=dataLayer&cx=c"
GOLD_URL_GA = "http://www.google-analytics.com/ga.js"
USUARIO = "mbrenting"
CLAVE = "mbrenting2021"
GOLD_URL_WIALON = "https://hst-api.wialon.com"
GOLD_URL_WIALON_POST = "https://hst-api.wialon.com/wialon/post.html"


def extraer_texto(textomaster, ini_cabecera, fin_cabecera):
    ini = textomaster.find(ini_cabecera)
    # empieza a buscar el fin a partir del inicio
    fin = textomaster.find(fin_cabecera, ini+len(ini_cabecera))
    # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
    texto = textomaster[ini+len(ini_cabecera):fin]
    return texto


def login_goldcar():
    payload_Login = {}
    headers_Login = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response_Login = requests.request(
        "GET", GOLD_URL_LOGIN, headers=headers_Login, data=payload_Login)
    sign_Login = extraer_datos_session(response_Login)
    #print(sign_Login.replace('\\', ''))
    # session = requests.Session()
    # session.get(GOLD_URL_LOGIN)
    # session.get(GOLD_URL_GA)
    # headers_GA = {
    #     'authority': 'www.google-analytics.com',
    #     'accept': '*/*',
    #     'accept-language': 'en-US,en;q=0.9',
    #     'referer': GOLD_URL_LOGIN,
    #     'sec-fetch-dest': 'script',
    #     'sec-fetch-mode': 'no-cors',
    #     'sec-fetch-site': 'cross-site',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    # }
    # session.get(GOLD_URL_GA, headers=headers_GA)
    # print(session.cookies)
    # # https://stackoverflow.com/questions/29928591/not-getting-all-cookie-info-using-python-requests-module
    # # session.get("http://gpsgoldcar.com")
    # # session.get("https://gpsgoldcar.com")
    # # session.get("http://gpsenperu.gpsgoldcar.com")
    # # session.get("http://gpsenperu.gpsgoldcar.com/")
    # # print(session.cookies)
    # # print(session.headers)
    # # print(d_Login)
    # # session = requests.Session()
    # # r = requests.post("http://google.com")
    # # a = r.cookies.get_dict()
    # # print(response_Login.headers)
    # ga_inicio = obtener_millis(response_Login.headers["Date"])
    # # https://stackoverflow.com/questions/25091976/python-requests-get-cookies
    # print(ga_inicio)
    # payload_Monitoring_Login = {}
    # # Usar selenium y requests a la vez
    # headers_Monitoring_Login = {
    #     'Accept': '*/*',
    #     'Accept-Language': 'en-US,en;q=0.9',
    #     'Connection': 'keep-alive',
    #     'Referer': GOLD_URL_LOGIN,
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    # }
    # response_Monitoring_Login = requests.request(
    #     "GET", GOLD_URL_MONITORING_LOGIN, headers=headers_Monitoring_Login, data=payload_Monitoring_Login)
    # # print(response_Monitoring_Login.cookies)
    # # print(response_Monitoring_Login.text)

    # payload_Tag_Manager = {}
    # headers_Tag_Manager = {
    #     'Accept': '*/*',
    #     'Accept-Language': 'en-US,en;q=0.9',
    #     'Connection': 'keep-alive',
    #     'Referer': GOLD_URL_LOGIN,
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    # }
    # response_Tag_Manager = requests.request(
    #     "GET", GOLD_URL_TAG_MANAGER, headers=headers_Tag_Manager, data=payload_Tag_Manager)
    # # print(response_Tag_Manager.headers)
    # # print(response_Tag_Manager.text)

    # payload_GL6 = {}
    # headers_GL6 = {
    #     'Accept': '*/*',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    # }
    # response_GL6 = requests.request(
    #     "GET", GOLD_URL_G_L6, headers=headers_GL6, data=payload_GL6)
    # # print(response_GL6.headers)
    # # print(response_GL6.text)
    # print(type(sign_Login))
    #sign_Login_no_backslash = sign_Login.replace('\\', '')
    # print(sign_Login)
    payload_Oauth = 'wialon_sdk_url=https%3A%2F%2Fhst-api.wialon.com&client_id=GPS%2BGOLDCAR&access_type=-1&activation_time=0&duration=2592000&flags=7&response_type=hash&sign=' + \
        urllib.parse.quote(sign_Login.replace('\\', ''), safe="") + '&login=' + USUARIO + '&passw=' + CLAVE + \
        '&redirect_uri=http%3A%2F%2Fgpsenperu.gpsgoldcar.com%2Fpost_message.html&request_id=1'
    # print(payload_Oauth)
    #ga_fin = obtener_millis_now()
    headers_Oauth = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': "gpsenperu.gpsgoldcar.com",
        'Origin': 'http://gpsenperu.gpsgoldcar.com',
        'Referer': 'http://gpsenperu.gpsgoldcar.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    response_Oauth = requests.request(
        "POST", GOLD_URL_OAUTH, allow_redirects=False, headers=headers_Oauth, data=payload_Oauth)
    # print(response_Oauth.text)
    # print(response_Oauth.headers["Location"])

    url_Authorize = response_Oauth.headers["Location"]
    payload_Authorize = {}
    headers_Authorize = {
        'authority': 'hst-api.wialon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'http://gpsenperu.gpsgoldcar.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response_Authorize = requests.request(
        "GET", url_Authorize, allow_redirects=False, headers=headers_Authorize, data=payload_Authorize)

    url_Post_Message = response_Authorize.headers["location"]
    print("url_Post_Message o location de Authorize")
    print(url_Post_Message)
    payload_Post_Message = {}
    headers_Post_Message = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'http://gpsenperu.gpsgoldcar.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response_Post_Message = requests.request(
        "GET", url_Post_Message, headers=headers_Post_Message, data=payload_Post_Message)

    # print("response_Post_Message.text")
    # print(response_Post_Message.text)

    auth_hash = extraer_texto(url_Post_Message, "access_hash=", "&user_name")

    print("auth_hash")
    print(auth_hash)

    url_Ajax = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/use_auth_hash&params=%7B%22authHash%22%3A%22" + auth_hash + \
        "%22%2C%22appName%22%3A%22web%2Fgpsenperu.gpsgoldcar.com%22%2C%22siteName%22%3A%22ccardenas%22%2C%22checkService%22%3A%22%22%7D&callback=__wialon_sdk_jsonp_1"

    payload_Ajax = {}
    headers_Ajax = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'http://gpsenperu.gpsgoldcar.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response_Ajax = requests.request(
        "GET", url_Ajax, headers=headers_Ajax, data=payload_Ajax)
    # print("response_Ajax.text")
    # print(response_Ajax.text)
    sid = extraer_texto(response_Ajax.text, '"eid":"', '"')
    print(sid)

    url_Sid = "http://gpsenperu.gpsgoldcar.com/?sid=" + sid
    payload_Sid = {}
    headers_Sid = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'lang=en; _ga=GA1.1.1376740462.1673995120; _ga_L6NP7TDMF6=GS1.1.1673995119.1.0.1673995128.0.0.0; gr=1',
        'Referer': 'http://gpsenperu.gpsgoldcar.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response_Sid = requests.request(
        "GET", url_Sid, headers=headers_Sid, data=payload_Sid)
    # print("response_Sid.text")
    # print(response_Sid.text)
    #scrape_filename = "goldcar_sid_data.html"
    # with open(scrape_filename, "w", encoding="utf-8") as f:  # Descomentar para hacer primer request
    #    f.write(response_Sid.text)  # Descomentar para hacer primer request
    # doc = BeautifulSoup(
    #     open(scrape_filename, "r", encoding="utf-8"), "html.parser")
    # print(doc)

    # Click en pestaña "Reports"
    url_Get_Locale = "https://hst-api.wialon.com/wialon/ajax.html?svc=user/get_locale&sid=" + sid

    payload_Get_Locale = 'params=%7B%22userId%22%3A22630230%7D&sid=' + sid
    headers_Get_Locale = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Get_Locale = requests.request(
        "POST", url_Get_Locale, headers=headers_Get_Locale, data=payload_Get_Locale)

    url_Set_locale = "https://hst-api.wialon.com/wialon/ajax.html?svc=render/set_locale&sid=" + sid

    payload_Set_locale = 'params=%7B%22tzOffset%22%3A-134170192%2C%22language%22%3A%22en%22%2C%22flags%22%3A259%2C%22formatDate%22%3A%22%25Y-%25m-%25E%20%25H%3A%25M%3A%25S%22%7D&sid=' + sid
    headers_Set_locale = {
        'authority': 'hst-api.wialon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': GOLD_URL_WIALON,
        'referer': GOLD_URL_WIALON_POST,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Set_locale = requests.request(
        "POST", url_Set_locale, headers=headers_Set_locale, data=payload_Set_locale)

    return sid


# return x
# login_goldcar()
