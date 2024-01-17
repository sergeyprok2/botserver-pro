from bs4 import BeautifulSoup as bs
import requests, csv, json, os, sys, time

def main():
    import requests

    cookies = {
        'sputnik_session': '1703785411826|3',
        '_ym_d': '1703783413',
        '_ym_isad': '1',
        '_ym_uid': '1703783413345998708',
        'sp_test': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Sec-Fetch-Site': 'none',
        # 'Cookie': 'sputnik_session=1703785411826|3; _ym_d=1703783413; _ym_isad=1; _ym_uid=1703783413345998708; sp_test=1',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'navigate',
        'Host': 'fssp.gov.ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15',
        'Accept-Language': 'ru',
        'Sec-Fetch-Dest': 'document',
        'Connection': 'keep-alive',
    }

    params = {
        'is[variant]': '1',
        'is[last_name]': 'Синев',
        'is[first_name]': 'Валентин',
        'is[patronymic]': 'Иванович',
        'is[date]': '16.05.1975',
        'is[region_id][0]': '74',
    }

    # response = requests.get('https://fssp.gov.ru/iss/ip/', params=params, cookies=cookies, headers=headers)
    response = requests.get('https://fssp.gov.ru/iss/ip/?is%5Bvariant%5D=1&is%5Blast_name%5D=Синев&is%5Bfirst_name%5D=Валентин&is%5Bpatronymic%5D=Иванович&is%5Bdate%5D=16.05.1975&is%5Bregion_id%5D%5B0%5D=74',  cookies=cookies, headers=headers)
    response.encoding = 'CP1251'

    soup = bs(response.text, 'html.parser')
    print(soup)
    print('soup')
    with open('file_апа.txt', 'w') as file:
        # Записываем текст в файл
        file.write(str(soup))



if __name__ == '__main__':
    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)