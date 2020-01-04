'''
Napisz program wczytujący plik z logami aktywności użytkowników w systemie.
Na podstawie wczytanych danych wyświetl informację o sumarycznym czasie przebywania każdego użytkownika w systemie.
Przykład użycia:$ python read_logs.py logs.txt
Czas przebywania w systemie:
- user-1: 92 s
- user-2: 51 s
- user-3: 20 s
'''

with open('logs.txt') as plik:
    wiersze = plik.read().split('\n')

loginy = {} #uzytkownik -> suma czasów logowania
logouty = {}

for wiersz in wiersze:
    lista = wiersz.split(';')
    print(lista)
    kto = lista[0]
    operacja = lista[1]
    czas = int(lista[2])
    if operacja == "LOGIN":
        if kto not in loginy:
            loginy[kto] = 0
        loginy[kto] += czas
    if operacja == "LOGOUT":
        if kto not in logouty:
            logouty[kto] = 0
        logouty[kto] += czas

print(loginy)
print(logouty)

czas_w_systemie = {u: logouty[u] - loginy[u] for u in logouty}
for k, v in sorted(czas_w_systemie.items(), key=lambda x: x[1]):
    print(k, v)



