from tkinter import Tk, PhotoImage, Label, Button, Canvas, Frame, CENTER, NW, SW, BOTH

def main_menu():
	"""Main menu"""

	canvas.delete("fg")

	title_label = Label(window, image=title_image)
	title_canvaswindow = canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")
	
	play_button = Button(window, text="Play", font = ("Arial", 50), command=play_menu)
	play_canvaswindow = canvas.create_window(450,350, anchor=CENTER, window=play_button, tags="fg")

	howtoplay_button = Button(window, text="How to Play", font = ("Arial", 50), command=howtoplay_menu)
	howtoplay_canvaswindow = canvas.create_window(450,550, anchor=CENTER, window=howtoplay_button, tags="fg")

	about_button = Button(window, text="About", font = ("Arial", 50), command=about_menu)
	about_canvaswindow = canvas.create_window(450,750, anchor=CENTER, window=about_button, tags="fg")

	exit_button = Button(window, text="Exit", font = ("Arial", 50), command=exit)
	exit_canvaswindow = canvas.create_window(450,950, anchor=CENTER, window=exit_button, tags="fg")

def play_menu():
	"""Menu for when play is chosen, can choose ships"""

	canvas.delete("fg")

	title_label = Label(window, image=title_image)
	title_canvaswindow = canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")

	ship = canvas.create_image(450,540,image = ship_image, tags="fg")

	play_button = Button(window, text="Choose", font = ("Arial", 50),  command=lambda: difficulty_menu(ship))
	play_canvaswindow = canvas.create_window(450,800, anchor=CENTER, window=play_button, tags="fg")

	back_button = Button(window, text="Back", font = ("Arial", 50), command=main_menu)
	back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

def howtoplay_menu():
	"""How to play the game including controls and objectives"""

	canvas.delete("fg")

	title_label = Label(window, image=title_image)
	title_canvaswindow = canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")

	howtoplay_label = Label(window, image=howtoplay_image)
	howtoplay_canvaswindow = canvas.create_window(450,800, anchor=CENTER, window=howtoplay_label, tags="fg")

	back_button = Button(window, text="Back", font = ("Arial", 50), command=main_menu)
	back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")
			
def about_menu():
	"""Menu with information about the game and credits"""

	canvas.delete("fg")

	title_label = Label(window, image=title_image)
	title_canvaswindow = canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")

	about_label = Label(window, image=about_image)
	about_canvaswindow = canvas.create_window(450,800, anchor=CENTER, window=about_label, tags="fg")

	back_button = Button(window, text="Back", font = ("Arial", 50), command=main_menu)
	back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

def difficulty_menu(ship):
	"""Menu to choose difficulty"""

	canvas.delete("fg")

	title_label = Label(window, image=title_image)
	title_canvaswindow = canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")

	easy_button = Button(window, text="Easy", font = ("Arial", 50), command = lambda: game_loop("easy", ship))
	normal_button = Button(window, text="Normal", font = ("Arial", 50), command = lambda: game_loop("normal", ship))
	hard_button = Button(window, text="Hard", font = ("Arial", 50), command = lambda: game_loop("hard", ship))

	easy_canvaswindow = canvas.create_window(450, 350, anchor=CENTER, window=easy_button, tags="fg")
	normal_canvaswindow = canvas.create_window(450, 550, anchor=CENTER, window=normal_button, tags="fg")
	hard_canvaswindow = canvas.create_window(450, 750, anchor=CENTER, window=hard_button, tags="fg")

	back_button = Button(window, text="Back", font = ("Arial", 50), command=play_menu)
	back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

def exit():
	"""Closes the game"""

	window.destroy()

def game_loop(difficulty, ship):
	"""The main game"""

window = Tk()

window.geometry('900x1080')

canvas = Canvas(window, width=900, height=1080, bg="blue")

background_image = PhotoImage(file="Assets/bkgd_0.png")
canvas.create_image(0,0, anchor=NW, image=background_image)

canvas.pack()

title_image = PhotoImage(file="Assets/placeholder.png")

howtoplay_image = PhotoImage(file="Assets/placeholder.png")
about_image = PhotoImage(file="Assets/placeholder.png")

ship_image = PhotoImage(file="Assets/aship1.gif")

main_menu()

window.mainloop()
