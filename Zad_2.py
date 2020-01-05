'''

'''

from urllib.request import urlopen
import json

with urlopen("https://api.nbp.pl/api/cenyzlota?format=json") as plik:
    #urlopen - wysyła zapytanie, czeka na odpowiedx i zwraca nam coś plikopodobnego
    napis = plik.read().decode('utf-8') #zamienia byte code na string

print(type(napis))
print(napis)  #wyświetla cały byte code strony google
obiekt = json.loads(napis)



