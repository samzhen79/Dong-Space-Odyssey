from tkinter import Tk, PhotoImage, Label, Button, CENTER

def main_menu():
	"""Main menu"""

	for widgets in window.winfo_children():	#Cleans the window by destroting all the widgets except the background
		if widgets != background_label:
			widgets.destroy()

	title_label = Label(window, image=title_image)
	title_label.pack(anchor=CENTER, pady=50)
	
	play_label = Button(window, image=play_image, command=play_menu)
	play_label.pack(anchor=CENTER, pady=(0,5))

	howToPlay_label = Button(window, image=howToPlay_image, command=howtoplay_menu)
	howToPlay_label.pack(anchor=CENTER, pady=(5,5))

	about_label = Button(window, image=about_image, command=about_menu)
	about_label.pack(anchor=CENTER, pady=(5,5))

	exit_label = Button(window, image=exit_image, command=exit)
	exit_label.pack(anchor=CENTER, pady=(5,5))

	window.mainloop()



def play_menu():
	"""Menu for when play is chosen, can choose ships"""

	for widgets in window.winfo_children():
		if widgets != background_label:
			widgets.destroy()

	ship_label = Label(window, image=ship_image)
	ship_label.pack(anchor=CENTER, pady=(400,0))

	play_label = Button(window, image=play_image, command=play_menu)
	play_label.pack(anchor=CENTER, pady=(150,0))

	back_label = Button(window, image=back_image, command=main_menu)
	back_label.place(y=1080-152)

def howtoplay_menu():
	"""How to play the game including controls and objectives"""

	for widgets in window.winfo_children():
		if widgets != background_label:
			widgets.destroy()

	back_label = Button(window, image=back_image, command=main_menu)
	back_label.place(y=1080-152)
			
def about_menu():
	"""Menu with information about the game and credits"""

	for widgets in window.winfo_children():	
		if widgets != background_label:
			widgets.destroy()

	back_label = Button(window, image=back_image, command=main_menu)
	back_label.place(y=1080-152)

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
play_image = PhotoImage(file="Assets/placeholder.png")
howToPlay_image = PhotoImage(file="Assets/placeholder.png")
about_image = PhotoImage(file="Assets/placeholder.png")
exit_image = PhotoImage(file="Assets/placeholder.png")
back_image = PhotoImage(file="Assets/placeholder.png")
ship_image = PhotoImage(file="Assets/placeholder.png")

main_menu()
