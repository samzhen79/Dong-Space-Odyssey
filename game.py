from tkinter import Tk, PhotoImage, Label, Button, Canvas, Frame, CENTER, N, NW, SW, BOTH
import configparser

def menu(menutype="default"):
	"""Creates a menu, takes arguments such that different menus can be chosen"""

	canvas.delete("fg") #fg for foreground of course, removes all foreground canvas items

	back_button = Button(window, text="Back", font = ("Arial", 50), command=menu)

	if menutype == "play":

		ship = canvas.create_image(450,540,image = ship_image, tags="fg")

		choose_button = Button(window, text="Choose", font = ("Arial", 50),  command=lambda menutype="difficulty": menu(menutype))
		choose_canvaswindow = canvas.create_window(450,800, anchor=CENTER, window=choose_button, tags="fg")

		back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")


	elif menutype == "difficulty":

		easy_button = Button(window, text="Easy", font = ("Arial", 50), command = lambda difficulty = "easy", ship = "ship": game_start(difficulty, ship))
		normal_button = Button(window, text="Normal", font = ("Arial", 50), command = lambda difficulty = "normal", ship = "ship": game_start(difficulty, ship))
		hard_button = Button(window, text="Hard", font = ("Arial", 50), command = lambda difficulty = "hard", ship = "ship": game_start(difficulty, ship))

		easy_canvaswindow = canvas.create_window(450, 350, anchor=CENTER, window=easy_button, tags="fg")
		normal_canvaswindow = canvas.create_window(450, 550, anchor=CENTER, window=normal_button, tags="fg")
		hard_canvaswindow = canvas.create_window(450, 750, anchor=CENTER, window=hard_button, tags="fg")#


		back_button.config(command = lambda menutype="play": menu(menutype))
		back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")


	elif menutype == "settings":

		settings_label = Label(window, text="Settings")
		settings_canvaswindow = canvas.create_window(450,800, anchor=CENTER, window=settings_label, tags="fg")

		back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

	elif menutype == "about":

		about_label = Label(window, image=about_image)
		about_canvaswindow = canvas.create_window(450,800, anchor=CENTER, window=about_label, tags="fg")

		back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")		

	else:

		title_label = Label(window, image=title_image)
		play_button = Button(window, text="Play", font = ("Arial", 50), command= lambda menutype="play": menu(menutype))
		settings_button = Button(window, text="Settings", font = ("Arial", 50), command= lambda menutype="settings": menu(menutype))
		about_button = Button(window, text="About", font = ("Arial", 50), command= lambda menutype="about": menu(menutype))
		exit_button = Button(window, text="Exit", font = ("Arial", 50), command= lambda: window.destroy())

		title_canvaswindow = canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")
		play_canvaswindow = canvas.create_window(450,350, anchor=CENTER, window=play_button, tags="fg")
		settings_canvaswindow = canvas.create_window(450,550, anchor=CENTER, window=settings_button, tags="fg")
		about_canvaswindow = canvas.create_window(450,750, anchor=CENTER, window=about_button, tags="fg")
		exit_canvaswindow = canvas.create_window(450,950, anchor=CENTER, window=exit_button, tags="fg")

def game_start(difficulty, ship):
	"""Starts the game"""

	canvas.delete("fg")

	ship = canvas.create_image(450,1080, anchor = N, image = ship_image, tags="fg")

	settings = configparser.ConfigParser()
	settings.read("settings.ini")

	# Neat little for loop here to have the ship enter the scene with a simple animation
	for x in range(40):
		time.sleep(0.01)
		canvas.move(ship, 0, -10)
		window.update()

	global velx, vely
	velx, vely = 0, 0

	def key_press(event):
		"""Records key presses for movement"""
		global velx, vely
		if event.char == settings["MOVEMENT"]["Forward"] and vely > -4:
				vely -= 4
		if event.char == settings["MOVEMENT"]["Backward"] and vely < 4:
				vely += 4
		if event.char == settings["MOVEMENT"]["Left"] and velx > -4:
				velx -= 4
		if event.char == settings["MOVEMENT"]["Right"] and velx < 4:
				velx += 4

	def key_release(event):
		"""Records when key is released for movement"""
		global velx, vely
		if event.char == settings["MOVEMENT"]["Forward"]:
			vely += 4
		if event.char == settings["MOVEMENT"]["Backward"]:
			vely -= 4
		if event.char == settings["MOVEMENT"]["Left"]:
			velx += 4
		if event.char == settings["MOVEMENT"]["Right"]:
			velx -= 4

	def game_loop():
		"""This is the main game loop"""
		global x, y, velx, vely

		x, y = 0, 0

		x += velx
		y += vely

		canvas.move(ship, x, y)

		window.after(10, game_loop)

	canvas.focus_set()
	canvas.bind("<KeyPress>", key_press)
	canvas.bind("<KeyRelease>", key_release)

	game_loop()


window = Tk()

window.geometry('900x1080')

canvas = Canvas(window, width=900, height=1080, bg="blue")

background_image = PhotoImage(file="Assets/bkgd_0.png")
canvas.create_image(0,0, anchor=NW, image=background_image)

canvas.pack()

title_image = PhotoImage(file="Assets/placeholder.png")

about_image = PhotoImage(file="Assets/placeholder.png")

ship_image = PhotoImage(file="Assets/aship1.gif")

menu()

window.mainloop()
