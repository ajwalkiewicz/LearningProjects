import tkinter

root = tkinter.Tk()
root.title("My Calculator")
root.resizable(width=0, height=0)


lista_przycisków = [
    ["7", "8", "9", "/"],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '+'],
    ['(', ')']]

my_font = ('Helvetica', '30')


def wstaw_przyciski():
    przyciski = []
    for rzad in lista_przycisków:
        przyciski.append(
            [tkinter.Button(
                root, text=str(znak),
                padx=20, pady=10,
                font=my_font,
                command=lambda znak=znak: akcja_przycisku(znak)) for znak in rzad])

    for i in range(1, len(przyciski) + 1):
        for j in range(len(przyciski[i - 1])):
            przyciski[i-1][j].grid(row=i, column=j, sticky=tkinter.NSEW)


def akcja_przycisku(znak):
    obecne = pole_tekstowe.get()
    pole_tekstowe.delete(0, tkinter.END)
    pole_tekstowe.insert(0, obecne + znak)


def wynik():
    try:
        wynik = pole_tekstowe.get()
        pole_tekstowe.delete(0, tkinter.END)
        pole_tekstowe.insert(0, eval(wynik))
    except:
        pole_tekstowe.delete(0, tkinter.END)
        pole_tekstowe.insert(0, "ERROR")


def wyczysc():
    pole_tekstowe.delete(0, tkinter.END)


pole_tekstowe = tkinter.Entry(root, width=15, borderwidth=10, font=my_font)
pole_tekstowe.grid(row=0, column=0, columnspan=4, sticky=tkinter.NSEW, ipady=25)

przycisk_wynik = tkinter.Button(root, text="=", command=wynik, padx=20, font=my_font)
przycisk_wynik.grid(row=5, column=2, columnspan=2, sticky=tkinter.NSEW)

przycisk_wyczysc = tkinter.Button(
    root, text="CE", command=wyczysc, font=my_font)
przycisk_wyczysc.grid(row=4, column=3, columnspan=2, sticky=tkinter.NSEW)

wstaw_przyciski()

root.mainloop()
