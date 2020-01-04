f = open('plik.txt')
#napis = f.read()
#print(repr(napis))
#print(f.readlines()) #metoda - zapoznaj się


print(f.read())
f.close()

with open ('plik.txt') as plik: #manager kontekstu
    print(plik.read())

