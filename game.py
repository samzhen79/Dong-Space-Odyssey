from tkinter import Tk, PhotoImage, Label, Button, Canvas, Frame, messagebox, CENTER, N, NW, SW, BOTH
import time
from configparser import ConfigParser

def menu(menutype="default"):
	"""Creates a menu, takes arguments so that different menus can be chosen"""

	canvas.delete("fg") #fg for foreground of course, removes all foreground canvas items

	settings = ConfigParser()
	settings.read("settings.ini")

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
		global controls

		changeshoot_button = Button(window, text = "Shoot key is: \n' " + settings["CONTROLS"]["Shoot"] + " '\nPress to change key.", font = ("Impact", 18), 
			command = lambda control = "Shoot", button = 0: changekey(control, button))
		changeforward_button = Button(window, text = "Forward key is: \n' " + settings["CONTROLS"]["Forward"] + " '\nPress to change key.", font = ("Impact", 18), 
			command = lambda control = "Forward", button = 1: changekey(control, button))
		changebackward_button = Button(window, text = "Backward key is: \n' " + settings["CONTROLS"]["Backward"] + " '\nPress to change key.", font = ("Impact", 18), 
			command = lambda control = "Backward", button = 2: changekey(control, button))
		changeleft_button = Button(window, text = "Left key is: \n' " + settings["CONTROLS"]["Left"] + " '\nPress to change key.", font = ("Impact", 18), 
			command = lambda control = "Left", button = 3: changekey(control, button))
		changeright_button = Button(window, text = "Right key is: \n' " + settings["CONTROLS"]["Right"] + " '\nPress to change key.", font = ("Impact", 18), 
			command = lambda control = "Right", button = 4: changekey(control, button))


		controls = [changeshoot_button, changeforward_button, changebackward_button, changeleft_button,changeright_button]
		settingsTitle = canvas.create_image(450,100, anchor=CENTER, image=settingsTitle_image, tags="fg")

		controlsTitle = canvas.create_image(450,200, anchor=CENTER, image=controlsTitle_image, tags="fg")

		changeshoot_canvaswindow = canvas.create_window(450, 300, anchor=CENTER, window=changeshoot_button, tags="fg")

		changeforward_canvaswindow = canvas.create_window(450, 450, anchor=CENTER, window=changeforward_button, tags="fg")
		changebackward_canvaswindow = canvas.create_window(450, 575, anchor=CENTER, window=changebackward_button, tags="fg")
		changeleft_canvaswindow = canvas.create_window(225, 500, anchor=CENTER, window=changeleft_button, tags="fg")
		changeright_canvaswindow = canvas.create_window(675, 500, anchor=CENTER, window=changeright_button, tags="fg")

		back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

	elif menutype == "about":

		about_label = Label(window, image=about_image)
		about_canvaswindow = canvas.create_window(450,800, anchor=CENTER, window=about_label, tags="fg")

		back_canvaswindow = canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")		

	else: # This is the default menutype i.e. the main menu

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

def changekey(control, button):

	def change(key):
		global controls
		canvas.delete(message_canvaswindow)

		settings = ConfigParser()
		settings.read("settings.ini")
		settings.set("CONTROLS", control, key.keysym)

		with open("settings.ini", "w") as configfile:

			settings.write(configfile)

		settings.read("settings.ini")

		controls[button].config(text = control + " key is: \n' " + settings["CONTROLS"][control] + " '\nPress to change key.")

	message_label = Label(window, text="Press a key...", font = ("Arial", 30), width=500, height=600)
	message_canvaswindow = canvas.create_window(450, 540, anchor=CENTER, window=message_label, tags="fg")

	canvas.bind_all("<Key>", change)

def game_start(difficulty, ship):
	"""Starts the game"""

	canvas.delete("fg")

	ship = canvas.create_image(450,1080, anchor = N, image = ship_image, tags="fg")

	settings = ConfigParser()
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

	canvas.bind("<KeyPress>", key_press)
	canvas.bind("<KeyRelease>", key_release)

	def game_loop():
		"""This is the main game loop"""

		global x, y, velx, vely

		x, y = 0, 0

		x += velx
		y += vely

		x0, y0, x1, y1 = canvas.bbox(ship)

		# This set of if statements sets the bounds for the ship, if the ship reaches these bounds it will bounce off them.
		if x0 <= -100:
			x = 4
		if x1 >= 1000:
			x = -4
		if y0 <= 0:
			y = 4
		if y1 >= 1100:
			y = -4

		canvas.move(ship, x, y) 

		window.after(10, game_loop)

	game_loop()


window = Tk()

window.geometry('900x1080')

canvas = Canvas(window, width=900, height=1080, bg="blue")

background_image = PhotoImage(file="Assets/bkgd_0.png")
canvas.create_image(0,0, anchor=NW, image=background_image)

canvas.pack()

title_image = PhotoImage(file="Assets/placeholder.png")

settingsTitle_image = PhotoImage(file="Assets/settings.png")
controlsTitle_image = PhotoImage(file="Assets/controls.png")


about_image = PhotoImage(file="Assets/placeholder.png")

ship_image = PhotoImage(file="Assets/aship1.png")

menu()

window.mainloop()
