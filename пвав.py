

import requests

data={'custname': 'gcghhgv',
'custtel': '456346783',
'custemail': 'kjl,ha@mail.ru',
'size': ',klikhgmj',
'topping': '`aewqew`',
'delivery': '22:45',
'comments': 'asewqds'}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru",
    "Host": "httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "X-Amzn-Trace-Id": "Root=1-658f012b-46a835bc17a28d4d4a03e319"
}

response = requests.post('http://httpbin.org/post', headers=headers,data=data)

print(response.text)
