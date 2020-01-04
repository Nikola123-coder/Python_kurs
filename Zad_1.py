'''
Napisz program wypisujący na konsolę zawartość wskazanego pliku wraz z numerami linii.
Obsłuż sytuację, gdy użytkownik nie poda nazwy pliku lub poda błędną nazwę.
Przykład użycia:$ python test.txt

1: pierwsza linia pliku
2: druga linia pliku
'''

nazwa = input("Podaj nazwę pliku:")
try:
    with open(nazwa, encoding = 'utf-8') as plik: #encoding - żeby nie było krzaczków w miejscu polskich znaków
        for nr, linia in enumerate (plik, 1):
            print(f'{nr:5}: {linia}', end='')

except FileNotFoundError:
    print("Nie ma takiego pliku")



