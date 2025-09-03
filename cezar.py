import tkinter as tk

okno = tk.Tk()
okno.title("Szyfr cezara")
okno.geometry("300x300")
okno.resizable(False, False)

text1 = tk.StringVar()

def szyfr():
    zwykly_tekst = text1.get()
    cezar_tekst = ""
    klucz = 3

    for literka in zwykly_tekst:
        if literka.isupper():
            cezar_tekst += chr((ord(literka) + klucz - 65) % 26 + 65)
        elif literka.islower():
            cezar_tekst += chr((ord(literka) + klucz - 97) % 26 + 97)
        else:
            cezar_tekst += literka  

    label4 = tk.Label(okno, text=cezar_tekst)
    label4.grid(row=3, column=0)

label1 = tk.Label(okno, text="Zaszyfruj wiadomość")
label1.grid(row=0, column=0)

entry1 = tk.Entry(okno, textvariable=text1)
entry1.grid(row=1, column=0)

b1 = tk.Button(okno, text="Szyfruj", command=szyfr)
b1.grid(row=2, column=0)

okno.mainloop()
