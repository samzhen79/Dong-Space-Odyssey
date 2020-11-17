from tkinter import Tk, PhotoImage, Label, Button, CENTER
def main_menu():
	"""Main menu"""
	window = Tk()

	#Window parameters
	window.geometry('900x1080')
	window.resizable(False, False)

	background_image = PhotoImage(file="Assets/bkgd_0.png")
	background_label = Label(window, image=background_image)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

	title_image = PhotoImage(file="Assets/placeholder.png")
	title_label = Label(window, image=title_image)
	title_label.pack(anchor=CENTER, pady=50)

	play_image = PhotoImage(file="Assets/placeholder.png")
	play_label = Button(window, image=play_image)
	play_label.pack(anchor=CENTER, pady=(100,5))

	howToPlay_image = PhotoImage(file="Assets/placeholder.png")
	howToPlay_label = Button(window, image=howToPlay_image)
	howToPlay_label.pack(anchor=CENTER, pady=(5,5))

	about_image = PhotoImage(file="Assets/placeholder.png")
	about_label = Button(window, image=about_image)
	about_label.pack(anchor=CENTER, pady=(5,5))

	exit_image = PhotoImage(file="Assets/placeholder.png")
	exit_label = Button(window, image=exit_image)
	exit_label.pack(anchor=CENTER, pady=(5,5))

	window.mainloop()

main_menu()