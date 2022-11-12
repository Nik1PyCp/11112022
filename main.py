from bs4 import BeautifulSoup
import requests
response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all(
        'td',
        {
            'data-label': 'Офіційний курс'
        }
    )
    print('Офіційний курс')
    print('SEK =', soup_list[31].text)
    print('CAD =', soup_list[13].text)
    print('EUR =', soup_list[8].text)
    print('CHF =', soup_list[32].text)
    print('USD =', soup_list[7].text)
    print('CZK =', soup_list[31].text)
    print('KZT =', soup_list[27].text)
    print('EGP =', soup_list[9].text)