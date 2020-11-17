from tkinter import Tk, PhotoImage, Label, Button, CENTER

def main_menu():
	"""Main menu"""

	for widgets in window.winfo_children():	#Cleans the window by destroting all the widgets except the background
		if widgets != background_label:
			widgets.destroy()

	title_label = Label(window, image=title_image)
	title_label.pack(anchor=CENTER, pady=50)
	
	play_button = Button(window, image=playbutton_image, command=play_menu)
	play_button.pack(anchor=CENTER, pady=(0,5))

	howtoplay_button = Button(window, image=howtoplaybutton_image, command=howtoplay_menu)
	howtoplay_button.pack(anchor=CENTER, pady=(5,5))

	about_button = Button(window, image=aboutbutton_image, command=about_menu)
	about_button.pack(anchor=CENTER, pady=(5,5))

	exit_button = Button(window, image=exitbutton_image, command=exit)
	exit_button.pack(anchor=CENTER, pady=(5,5))

	window.mainloop()

def play_menu():
	"""Menu for when play is chosen, can choose ships"""

	for widgets in window.winfo_children():
		if widgets != background_label:
			widgets.destroy()

	title_label = Label(window, image=title_image)
	title_label.pack(anchor=CENTER, pady=50)

	ship_label = Label(window, image=ship_image)
	ship_label.pack(anchor=CENTER, pady=(350,0))

	play_button = Button(window, image=playbutton_image, command=play_menu)
	play_button.pack(anchor=CENTER, pady=(150,0))

	back_button = Button(window, image=backbutton_image, command=main_menu)
	back_button.place(y=1080-152)	# minus the height of the image of the back button

def howtoplay_menu():
	"""How to play the game including controls and objectives"""

	for widgets in window.winfo_children():
		if widgets != background_label:
			widgets.destroy()

	title_label = Label(window, image=title_image)
	title_label.pack(anchor=CENTER, pady=50)

	howtoplay_label = Label(window, image=howtoplay_image)
	howtoplay_label.pack(anchor=CENTER, pady=(100,0))

	back_button = Button(window, image=backbutton_image, command=main_menu)
	back_button.place(y=1080-152)
			
def about_menu():
	"""Menu with information about the game and credits"""

	for widgets in window.winfo_children():	
		if widgets != background_label:
			widgets.destroy()

	title_label = Label(window, image=title_image)
	title_label.pack(anchor=CENTER, pady=50)

	about_label = Label(window, image=about_image)
	about_label.pack(anchor=CENTER, pady=(100,0))

	back_button = Button(window, image=backbutton_image, command=main_menu)
	back_button.place(y=1080-152)

def exit():
	"""Closes the game"""

	window.destroy()

window = Tk()

window.geometry('900x1080')
window.resizable(False, False)

background_image = PhotoImage(file="Assets/bkgd_0.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_image = PhotoImage(file="Assets/placeholder.png")

playbutton_image = PhotoImage(file="Assets/placeholder.png")
howtoplaybutton_image = PhotoImage(file="Assets/placeholder.png")
aboutbutton_image = PhotoImage(file="Assets/placeholder.png")
exitbutton_image = PhotoImage(file="Assets/placeholder.png")
backbutton_image = PhotoImage(file="Assets/placeholder.png")

howtoplay_image = PhotoImage(file="Assets/placeholder.png")
about_image = PhotoImage(file="Assets/placeholder.png")

ship_image = PhotoImage(file="Assets/placeholder.png")

main_menu()
