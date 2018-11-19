from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Geometry():
	def __init__(self, master):
		self.master = master
		master.title("Geometria")

		self.zakladka = ttk.Notebook(okno)
		self.zakladka.pack(expand=1, fill='both')


########Kwadrat#########

		self.tab1 = ttk.Frame(self.zakladka)
		self.zakladka.add(self.tab1, text='Kwadrat')

		self.ramka_kwadrat_wymiar = LabelFrame(self.tab1, text='Wymiary', fg='blue2')
		self.ramka_kwadrat_wymiar.pack(fill="both", pady = 10)

		self.left = Label(self.ramka_kwadrat_wymiar, text='Podaj długośc boku kwadratu: ')
		self.left.pack(anchor= W)

		self.bok_kwadratu = Entry(self.tab1, bg = 'SlateGray1', width=5)
		self.bok_kwadratu.place(x = 290, y = 24)

		self.przycisk1 = Button(self.tab1, text='Oblicz', bg = 'lawngreen', command=self.pole_kwadratu, width=10)
		self.przycisk1.place(x = 100, y = 90)

		self.ramka_kwadrat_wynik = LabelFrame(self.tab1, text='Wynik', fg='blue2')
		self.ramka_kwadrat_wynik.pack(fill='both', pady = 75)

		self.left = Label(self.ramka_kwadrat_wynik, text='Pole kwadratu wynosi: ')
		self.left.pack(anchor= W)

		self.wynik_kwadrat1 = Label(self.tab1, text='', font='Helvetica 14 bold')
		self.wynik_kwadrat1.place(x = 280, y = 150)


########Trojkat#########

		self.tab2 = ttk.Frame(self.zakladka)
		self.zakladka.add(self.tab2, text='Trójkąt')

		self.ramka_trojkat_wymiar = LabelFrame(self.tab2, text='Wymiary', fg='blue2')
		self.ramka_trojkat_wymiar.pack(fill="both", pady = 10)

		self.left = Label(self.ramka_trojkat_wymiar, text='Podaj długośc podstawy trójkąta: ')
		self.left.pack(anchor= W)

		self.podstawa_trojkata = Entry(self.tab2, bg = 'SlateGray1', width=5)
		self.podstawa_trojkata.place(x = 290, y = 22)

		self.left = Label(self.ramka_trojkat_wymiar, text='Podaj wysokośc trójkąta: ')
		self.left.pack(anchor= W)

		self.wysokosc_trojkata = Entry(self.tab2, bg = 'SlateGray1', width=5)
		self.wysokosc_trojkata.place(x = 290, y = 47)

		self.przycisk1 = Button(self.tab2, text='Oblicz', bg = 'lawngreen', command=self.pole_trojkata, width=10)
		self.przycisk1.place(x = 110, y = 100)

		self.ramka_trojkat_wynik = LabelFrame(self.tab2, text='Wynik', fg='blue2')
		self.ramka_trojkat_wynik.pack(fill='both', pady = 75)

		self.left = Label(self.ramka_trojkat_wynik, text='Pole trójkąta wynosi: ')
		self.left.pack(anchor= W)

		self.wynik_trojkat1 = Label(self.tab2, text='', font='Helvetica 14 bold')
		self.wynik_trojkat1.place(x = 280, y = 170)


########Koło#########

		self.tab3 = ttk.Frame(self.zakladka)
		self.zakladka.add(self.tab3, text='Koło')

		self.ramka_kolo_wymiar = LabelFrame(self.tab3, text='Wymiary', fg='blue2')
		self.ramka_kolo_wymiar.pack(fill="both", pady = 10)

		self.left = Label(self.ramka_kolo_wymiar, text='Podaj długośc promienia: ')
		self.left.pack(anchor= W)

		self.promien = Entry(self.tab3, bg = 'SlateGray1', width=5)
		self.promien.place(x = 290, y = 24)

		self.przycisk1 = Button(self.tab3, text='Oblicz', bg = 'lawngreen', command=self.pole_kola, width=10)
		self.przycisk1.place(x = 100, y = 90)

		self.ramka_kolo_wynik = LabelFrame(self.tab3, text='Wynik', fg='blue2')
		self.ramka_kolo_wynik.pack(fill='both', pady = 75)

		self.left = Label(self.ramka_kolo_wynik, text='Pole koła wynosi: ')
		self.left.pack(anchor= W)

		self.wynik_kolo1 = Label(self.tab3, text='', font='Helvetica 14 bold')
		self.wynik_kolo1.place(x = 280, y = 150)

########Inne#########

		self.button = Button(text='QUIT', command=quit)
		self.button.place(x = 280, y = 255)

		self.reset = Button(text='RESET', command=self.reset_wartosci)
		self.reset.place(x=10, y=255)


########Funkcje#########

	def pole_kwadratu(self):
		self.rownaie_kwadrat = int(self.bok_kwadratu.get()) ** 2
		self.wynik_kwadrat1.configure(text=self.rownaie_kwadrat)
		if self.bok_kwadratu.get() == '0':
			messagebox.showinfo("Warning!", "Podaj liczbę wiekszą niż 0")

	def pole_trojkata(self):
		self.rownaie_trojkat = (int(self.wysokosc_trojkata.get()) * int(self.podstawa_trojkata.get())) * 0.5
		self.wynik_trojkat1.configure(text=self.rownaie_trojkat)
		if self.wysokosc_trojkata.get() == '0':
			messagebox.showinfo("Warning!", "Podaj liczbę wiekszą niż 0")
		elif self.podstawa_trojkata.get() == '0':
			messagebox.showinfo("Warning!", "Podaj liczbę wiekszą niż 0")


	def pole_kola(self):
		self.rownaie_kolo = (int(self.promien.get())**2 * 3.14)
		self.wynik_kolo1.configure(text=self.rownaie_kolo)
		if self.promien.get() == '0':
			messagebox.showinfo("Warning!", "Podaj liczbę wiekszą niż 0")

	def reset_wartosci(self):
		self.bok_kwadratu.delete(0, END)
		self.podstawa_trojkata.delete(0, END)
		self.wysokosc_trojkata.delete(0, END)
		self.promien.delete(0, END)



okno = Tk() # tworze okno
okno.geometry('350x300+400+200')  # wielkosc okna
okno.resizable(0, 0)
aplikacja = Geometry(okno)
okno.mainloop() # Odpalam pętle
