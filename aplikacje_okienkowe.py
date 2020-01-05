'''

'''

import tkinter as tk  # dzięki temu skraca się zapis tkinter - zamist tego odwołujemy się z tk

class FloatPrzycisk(tk.Entry):
    def get(self):
        return float(super().get())

def fun():
    napis = entry.get()
    label.configure(text=napis)

root = tk.Tk()
przycisk = tk.Button(master=root, text="Click me!", command=fun)  # master - w momencie tworzenia obiektu przekazuje info kto zarządza przyciskiem
# info że tym przyciskiem będzie zarządzać root
przycisk.grid(row=0, column=0) #pozycja przycisku, gdzie ma się wyświetlić
przycisk2 = tk.Button(master=root, text="Click me 2!")
przycisk2.grid(row=0, column=1)
label = tk.Label(master=root, text="Jakiś label") #zwykły tekst wyświetlany na ekranie
label.grid(row=1, column=0, sticky=tk.W)
entry = tk.Entry(master=root) #pole tekstowe
entry.grid(row=1, column=1)


root.title("Moje pierwsze okienko")
root.mainloop() # uruchomienie pętli zdarzeń

