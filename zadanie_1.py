import json

#json.load()    #wariant do operowania na napisach
#json.loads()   #wariant do operowania na plikach
#json.dump()
#json.dumps()

obiekt = {"imie": "Jan", "cos": [None, 1, 2, 3]}  #obiekt w json musi być listą lub słownikiem, może zawierać jedną pozycję, ale nie może być jedną liczbą typu int

#pusty napis w json wyrzuci błąd
napis = json.dumps(obiekt)
print(napis)
print(type(napis))
print(repr(napis))

wynik = json.loads(napis)
print(type(wynik))
print(repr(wynik))

with open("test.json") as plik:
    obiekt = json.load(plik)
print(obiekt)
obiekt.append(123)
with open("test.json", "w") as plik:
    json.dump(obiekt, plik)