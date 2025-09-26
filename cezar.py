import tkinter as tk

okno = tk.Tk()
okno.title("Szyfr cezara")
okno.geometry("400x400")
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
    wynik = funkcja(cezar_tekst)     
    tekst.delete("1.0", tk.END)  
    tekst.insert(tk.END, wynik) 
def  funkcja(cezar_tekst):
    return f"Szyfrem do tego kodu jest: {cezar_tekst}"


label1 = tk.Label(okno, text="Zaszyfruj wiadomość")
label1.pack(pady=10)

entry1 = tk.Entry(okno, textvariable=text1,width=30)

entry1.pack(ipady=20)

b1 = tk.Button(okno, text="Szyfruj", command=szyfr)
b1.pack()

tekst = tk.Text(okno, height=20, width=30)
tekst.pack(pady=20)
okno.mainloop()
