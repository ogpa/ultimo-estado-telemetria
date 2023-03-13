import requests
import time


GOLD_URL_WIALON = "https://hst-api.wialon.com"
GOLD_URL_WIALON_POST = "https://hst-api.wialon.com/wialon/post.html"


def epoch():
    epoch = int(time.time())
    return epoch


def duplicate(sid):

    url_Post_1 = "https://hst-api.wialon.com/wialon/post.html"

    payload_Post_1 = {}
    headers_Post_1 = {
        'authority': 'hst-api.wialon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'http://gpsenperu.gpsgoldcar.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    response_Post_1 = requests.request(
        "GET", url_Post_1, headers=headers_Post_1, data=payload_Post_1)

    # print(response.text)
    url_Duplicate_1 = "https://hst-api.wialon.com/wialon/ajax.html?svc=core/duplicate&sid=" + sid

    payload_Duplicate_1 = 'params=%7B%22operateAs%22%3A%22%22%2C%22continueCurrentSession%22%3Atrue%2C%22checkService%22%3A%22ccardenas%22%2C%22restore%22%3A1%2C%22appName%22%3A%22web%2Fgpsenperu.gpsgoldcar.com%22%2C%22siteName%22%3A%22ccardenas%22%7D&sid=' + sid
    headers_Duplicate_1 = {
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

    response_Duplicate_1 = requests.request(
        "POST", url_Duplicate_1, headers=headers_Duplicate_1, data=payload_Duplicate_1)
    return response_Duplicate_1.text
