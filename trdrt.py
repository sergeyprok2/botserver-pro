

import requests
import requests,pprint

import requests

import requests

import requests

import requests

headers = {
    'Content-Type': 'application/JSON',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'If-None-Match': 'W/"ab2bfd22279f57c1664ee7e29473a18d0a58f983"',
    'Accept-Language': 'ru',
    'Sec-Fetch-Mode': 'cors',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://kino-prk.ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
    'Referer': 'https://kino-prk.ru/',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Host': 'kinokassa.kinoplan24.ru',
    'X-Application-Token': 'BLPlyTae3IwRIuGvAeohxiBsp36doVMX',
    'X-Platform': 'widget',
}

params = {
    'city_id': '313',
    'date': '2024-01-03',
}

response = requests.get('https://kinokassa.kinoplan24.ru/api/v2/release/playbill', params=params, headers=headers)
# response = requests.get('https://kinokassa.kinoplan24.ru/api/v2/release/19962?city_id=313', headers=headers)
if response.status_code==200:
    pprint.pprint(response.json())
else:
    print("HTTP response", response.status_code)