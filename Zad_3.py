'''
Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.
Skorzystaj z modułu `urllib.request`, `json` oraz API MetaWeather.
'''

from urllib.request import urlopen
import json
'''
with urlopen("https://www.metaweather.com/api/location/search/?query=madrid") as plik:
    napis = plik.read().decode('utf-8')
    wynik = json.load(napis)
    id = wynik(0, 'woied')
    print(napis)
'''


gdzie = input("Podaj miasto: ")

with urlopen(f"https://www.metaweather.com/api/location/search/?query={gdzie}") as plik:
    wynik = json.loads(plik.read().decode('utf-8'))

woeid = wynik[0]['woeid']
print(f'WOEID: {woeid}')

with urlopen(f"https://www.metaweather.com/api/location/{woeid}") as plik:
    wynik = json.loads(plik.read().decode('utf-8'))

consolidated = wynik['consolidated_weather']

print(consolidated)

prognozy = wynik['consolidated_weather']
for prognoza in prognozy:
    print(f'Prognoza na dzień {prognoza["applicable_date"]}:')
    print(f"\ttemp: {prognoza['min_temp']}--{prognoza['max_temp']:.2f}")








