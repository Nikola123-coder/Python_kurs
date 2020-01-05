'''
Napisz program z graficznym interfejsem użytkownika (GUI) do obliczania kosztów przejazdu na zadanym dystansie
na podstawie spalania samochodu oraz ceny paliwa.
Skorzystaj z modułu `tkinter`.
'''

import tkinter as tk

def oblicz():
    d = float(entry.get())
    s = float(entry.get())
    c = float(entry.get())


root = tk.Tk()
label = tk.Label(master=root, text="Cena paliwa")
label.grid(row=2, column=3)
label2 = tk.Label(master=root, text="Spalanie na km")
label2.grid(row=3, column=3)
label3 = tk.Label(master=root, text="Ilość km")
label3.grid(row=4, column=3)

przycisk = tk.Button(master=root, text="Koszty przejazdu") #zwykły tekst wyświetlany na ekranie
przycisk.grid(row=1, column=0)
entry = tk.Entry(master=root)
entry.grid(row=2, column=0)
entry1 = tk.Entry(master=root)
entry1.grid(row=2, column=4)
entry2 = tk.Entry(master=root)
entry2.grid(row=3, column=4)
entry3 = tk.Entry(master=root)
entry3.grid(row=4, column=4)

root.title("Podróż samochodem")
root.mainloop()