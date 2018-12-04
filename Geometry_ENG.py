from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Geometry():
	def __init__(self, master):
		self.master = master
		master.title("Geometry")

		self.overlap = ttk.Notebook(window)
		self.overlap.pack(expand=1, fill='both')


########Square#########

		self.tab1 = ttk.Frame(self.overlap)
		self.overlap.add(self.tab1, text='Square')

		self.square_frame_dimension = LabelFrame(self.tab1, text='Dimension', fg='blue2')
		self.square_frame_dimension.pack(fill="both", pady = 10)

		self.left = Label(self.square_frame_dimension, text='The length of the square: ')
		self.left.pack(anchor= W)

		self.side_of_square = Entry(self.tab1, bg ='SlateGray1', width=5)
		self.side_of_square.place(x = 290, y = 24)

		self.button1 = Button(self.tab1, text='Calculate', bg ='lawngreen', command=self.square, width=10)
		self.button1.place(x = 100, y = 90)

		self.square_result_box = LabelFrame(self.tab1, text='Result', fg='blue2')
		self.square_result_box.pack(fill='both', pady = 75)

		self.left = Label(self.square_result_box, text='The square field is: ')
		self.left.pack(anchor= W)

		self.square_result1 = Label(self.tab1, text='', font='Helvetica 14 bold')
		self.square_result1.place(x = 280, y = 150)


########Triangle#########

		self.tab2 = ttk.Frame(self.overlap)
		self.overlap.add(self.tab2, text='Triangle')

		self.triangle_frame_dimension = LabelFrame(self.tab2, text='Dimension', fg='blue2')
		self.triangle_frame_dimension.pack(fill="both", pady = 10)

		self.left = Label(self.triangle_frame_dimension, text='The length of the triangle: ')
		self.left.pack(anchor= W)

		self.base_of_triangle = Entry(self.tab2, bg ='SlateGray1', width=5)
		self.base_of_triangle.place(x = 290, y = 22)

		self.left = Label(self.triangle_frame_dimension, text='The height of the square: ')
		self.left.pack(anchor= W)

		self.height_of_triangle = Entry(self.tab2, bg ='SlateGray1', width=5)
		self.height_of_triangle.place(x = 290, y = 47)

		self.button1 = Button(self.tab2, text='Calculate', bg ='lawngreen', command=self.triangle, width=10)
		self.button1.place(x = 110, y = 100)

		self.triangle_result_box = LabelFrame(self.tab2, text='Result', fg='blue2')
		self.triangle_result_box.pack(fill='both', pady = 75)

		self.left = Label(self.triangle_result_box, text='The triangle field is: ')
		self.left.pack(anchor= W)

		self.triangle_result1 = Label(self.tab2, text='', font='Helvetica 14 bold')
		self.triangle_result1.place(x = 280, y = 170)


########Circle#########

		self.tab3 = ttk.Frame(self.overlap)
		self.overlap.add(self.tab3, text='Circle')

		self.circle_frame_dimension = LabelFrame(self.tab3, text='Dimension', fg='blue2')
		self.circle_frame_dimension.pack(fill="both", pady = 10)

		self.left = Label(self.circle_frame_dimension, text='The radius of the circle: ')
		self.left.pack(anchor= W)

		self.radius = Entry(self.tab3, bg ='SlateGray1', width=5)
		self.radius.place(x = 290, y = 24)

		self.button1 = Button(self.tab3, text='Calculate', bg ='lawngreen', command=self.circle, width=10)
		self.button1.place(x = 100, y = 90)

		self.circle_result_box = LabelFrame(self.tab3, text='Result', fg='blue2')
		self.circle_result_box.pack(fill='both', pady = 75)

		self.left = Label(self.circle_result_box, text='The circle field is: ')
		self.left.pack(anchor= W)

		self.circle_result1 = Label(self.tab3, text='', font='Helvetica 14 bold')
		self.circle_result1.place(x = 280, y = 150)

########Other#########

		self.button = Button(text='QUIT', command=quit)
		self.button.place(x = 280, y = 255)

		self.reset = Button(text='RESET', command=self.reset_value)
		self.reset.place(x=10, y=255)


########Functions#########

	def square(self):
		self.square_equation = int(self.side_of_square.get()) ** 2
		self.square_result1.configure(text=self.square_equation)
		if self.side_of_square.get() == '0':
			messagebox.showinfo("Warning!", "Input greater than 0!")

	def triangle(self):
		self.triangle_equation = (int(self.height_of_triangle.get()) * int(self.base_of_triangle.get())) * 0.5
		self.triangle_result1.configure(text=self.triangle_equation)
		if self.height_of_triangle.get() == '0':
			messagebox.showinfo("Warning!", "Input greater than 0!")
		elif self.base_of_triangle.get() == '0':
			messagebox.showinfo("Warning!", "Input greater than 0!")


	def circle(self):
		self.circle_equation = (int(self.radius.get()) ** 2 * 3.14)
		self.circle_result1.configure(text=self.circle_equation)
		if self.radius.get() == '0':
			messagebox.showinfo("Warning!", "Input greater than 0!")

	def reset_value(self):
		self.side_of_square.delete(0, END)
		self.base_of_triangle.delete(0, END)
		self.height_of_triangle.delete(0, END)
		self.radius.delete(0, END)



window = Tk() # tworze okno
window.geometry('350x300+400+200')  # wielkosc okna
window.resizable(0, 0)
application = Geometry(window)
window.mainloop() # Odpalam p?tle
