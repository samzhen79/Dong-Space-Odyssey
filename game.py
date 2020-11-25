from tkinter import Tk, PhotoImage, Label, Button, Canvas, Frame, messagebox, CENTER, N, NE, NW, SW, BOTH
from configparser import ConfigParser
import time, json, math

def menu(menutype="default"):
	"""Creates a menu, takes arguments so that different menus can be chosen"""

	canvas.delete("fg") #fg for foreground of course, removes all foreground canvas items

	settings = ConfigParser()
	settings.read("settings.ini")

	back_button = Button(window, text="Back", font = ("Arial", 50), command=menu)

	if menutype == "play":

		newgame_button = Button(window, text="New Game", font = ("Impact", 50), command = lambda menutype="chooseship": menu(menutype))
		loadgame_button = Button(window, text="Load Game", font = ("Impact", 50), command = lambda difficulty = None, ship = None, state="saved": game_start(difficulty, ship, state))


		canvas.create_window(450, 350, anchor=CENTER, window=newgame_button, tags="fg")
		canvas.create_window(450, 550, anchor=CENTER, window=loadgame_button, tags="fg")

		canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

	elif menutype == "chooseship":

		ship = canvas.create_image(450,540,image = ship_image, tags="fg")

		choose_button = Button(window, text="Choose", font = ("Arial", 50),  command=lambda menutype="difficulty": menu(menutype))
		canvas.create_window(450,800, anchor=CENTER, window=choose_button, tags="fg")

		back_button.config(command = lambda menutype="play": menu(menutype))
		canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")


	elif menutype == "difficulty":

		easy_button = Button(window, text="Easy", font = ("Arial", 50), command = lambda difficulty = "easy", ship = "ship": game_start(difficulty, ship))
		normal_button = Button(window, text="Normal", font = ("Arial", 50), command = lambda difficulty = "normal", ship = "ship": game_start(difficulty, ship))
		hard_button = Button(window, text="Hard", font = ("Arial", 50), command = lambda difficulty = "hard", ship = "ship": game_start(difficulty, ship))

		canvas.create_window(450, 350, anchor=CENTER, window=easy_button, tags="fg")
		canvas.create_window(450, 550, anchor=CENTER, window=normal_button, tags="fg")
		canvas.create_window(450, 750, anchor=CENTER, window=hard_button, tags="fg")


		back_button.config(command = lambda menutype="chooseship": menu(menutype))
		canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")


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
		changepause_button = Button(window, text = "Pause key is: \n' " + settings["CONTROLS"]["Pause"] + " '\nPress to change key.", font = ("Impact", 18), 
			command = lambda control = "Pause", button = 5: changekey(control, button))

		controls = [changeshoot_button, changeforward_button, changebackward_button, changeleft_button, changeright_button, changepause_button] #This is needed to update the key shown on the button
		canvas.create_image(450,100, anchor=CENTER, image=settingsTitle_image, tags="fg")

		canvas.create_image(450,200, anchor=CENTER, image=controlsTitle_image, tags="fg")

		canvas.create_window(450, 300, anchor=CENTER, window=changeshoot_button, tags="fg")

		canvas.create_window(450, 450, anchor=CENTER, window=changeforward_button, tags="fg")
		canvas.create_window(450, 575, anchor=CENTER, window=changebackward_button, tags="fg")
		canvas.create_window(225, 500, anchor=CENTER, window=changeleft_button, tags="fg")
		canvas.create_window(675, 500, anchor=CENTER, window=changeright_button, tags="fg")
		canvas.create_window(450, 725, anchor=CENTER, window=changepause_button, tags="fg")

		canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

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

		canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")
		canvas.create_window(450,350, anchor=CENTER, window=play_button, tags="fg")
		canvas.create_window(450,550, anchor=CENTER, window=settings_button, tags="fg")
		canvas.create_window(450,750, anchor=CENTER, window=about_button, tags="fg")
		canvas.create_window(450,950, anchor=CENTER, window=exit_button, tags="fg")

def changekey(control, button):
	"""Starts the control key change process, takes the specific control being changed and the value of the button that was pressed"""
	def change(key):
		"""Changes the key in the settings.ini file to a key the user presses"""

		global controls
		canvas.delete(keyprompt_canvaswindow) 

		settings = ConfigParser()
		settings.read("settings.ini")
		settings.set("CONTROLS", control, key.keysym)

		with open("settings.ini", "w") as configfile:

			settings.write(configfile)

		settings.read("settings.ini")

		controls[button].config(text = control + " key is: \n' " + settings["CONTROLS"][control] + " '\nPress to change key.")

		window.unbind("<Key>")

	keyprompt_label = Label(window, text="Press a key...", font = ("Arial", 30), width=500, height=600)
	keyprompt_canvaswindow = canvas.create_window(450, 540, anchor=CENTER, window=keyprompt_label, tags="fg")

	window.bind("<Key>", change)

def game_start(difficulty, ship, state="new"):
	"""Starts the game"""

	canvas.delete("fg")

	global maxvelocity, velx, vely, shoot, interval, pausestate, savestate, gametime, enemylist, ship_stats, attackinterval, score
	maxvelocity = 8
	velx, vely, gametime, attackinterval, score = 0, 0, 0, 0, 0
	shoot, interval, pausestate = False, False, False

	score_label = Label(window, text="Score: " + str(score).zfill(10), font = ("Impact", 18))

	score_canvaswindow = canvas.create_window(900, 0, anchor=NE, window=score_label, tags=("fg", "game"))


	if state == "new": # New Game

		canvas.create_image(450.0,1080.0, anchor = N, image = ship_image, tags=("fg", "game", "ship", "shipbody"))

		ship_stats = {
			"type": 1,
			"health": 100,
			"level": 1,
			"fireratemultiplier":	1,
			"damagemultiplier": 1,
		}

		enemylist = []

		# Neat little for loop here to have the ship enter the scene with a simple animation
		for x in range(40):
			time.sleep(0.01)
			canvas.move(ship, 0, -10)
			window.update()

		savestate = open("savestate.txt", "w")

	elif state == "saved": # Load saved game, if no saved game available then starts a new game

		file = open("savestate.txt", "r")
		check = file.read(1)

		if not check:	# If no saved game then start new game

			file.close()
			menu("chooseship")
			return

		else:

			savestateobjects = file.read().splitlines()

			information = savestateobjects[0].split("~")
			gametime = int(information[0])
			ship_stats = json.loads(information[1])
			enemylist = json.loads(information[2])
			score = int(information[3])

			for object in savestateobjects[1:]:
				#This code is needed to interpret the savestate.txt, Effectively splits the text file into the necessary parts and then cleans each part until it is useable in create_image()
				object = object.split("~")

				coords = object[0].replace("[", "")
				coords = coords.replace("]", "")
				coords = coords.split(", ")

				config = object[1][1:-1].replace("'',","")
				config = config.split("), ")

				anchor = config[1][34:-1]
				
				image = config[3][23:-1]

				tags = config[5][21:-2].split()
				tagstring = ""

				for tag in tags:

					tagstring += '"' + str(tag) +'", '

				tagstring = tagstring[0:-2]

				#creates the needed objects from the interpreted savestate.txt
				canvas.create_image(coords[0], coords[1], anchor = anchor, image = image, tags = (eval(tagstring)))

			i = 0

			#Due to having to recreate all the canvas items, the item handle written in enemylist is now incorrect and must be updated with the new handle.
			for enemy in canvas.find_withtag("enemy"):

				enemylist[i][0]=enemy
				i+1

			file.close()
			savestate = open("savestate.txt", "w")


	settings = ConfigParser()
	settings.read("settings.ini")

	#Player Movement and shooting
	def key_press(event):
		"""Records key presses for controls"""
		global velx, vely, shoot, pausestate

		#Movement
		if event.keysym.upper() == settings["CONTROLS"]["Forward"].upper() and vely > -maxvelocity:
				vely -= maxvelocity
		if event.keysym.upper() == settings["CONTROLS"]["Backward"].upper() and vely < maxvelocity:
				vely += maxvelocity
		if event.keysym.upper() == settings["CONTROLS"]["Left"].upper() and velx > -maxvelocity:
				velx -= maxvelocity
		if event.keysym.upper() == settings["CONTROLS"]["Right"].upper() and velx < maxvelocity:
				velx += maxvelocity

		#Shooting
		if event.keysym.upper() == settings["CONTROLS"]["Shoot"].upper():

			shoot = True

		#Pause
		if event.keysym.upper() == settings["CONTROLS"]["Pause"].upper():
			pausestate = True

	def key_release(event):
		"""Records when a key is released for movement and shooting"""
		global maxvelocity, velx, vely, shoot

		#Movement
		if event.keysym.upper() == settings["CONTROLS"]["Forward"].upper():
			vely += maxvelocity
		if event.keysym.upper() == settings["CONTROLS"]["Backward"].upper():
			vely -= maxvelocity
		if event.keysym.upper() == settings["CONTROLS"]["Left"].upper():
			velx += maxvelocity
		if event.keysym.upper() == settings["CONTROLS"]["Right"].upper():
			velx -= maxvelocity

		#Shooting
		if event.keysym.upper() == settings["CONTROLS"]["Shoot"].upper():

			shoot = False

	canvas.bind_all("<KeyPress>", key_press)
	canvas.bind_all("<KeyRelease>", key_release)

	def enemy_spawn(type, spawnx, spawny, movement):
		"""Spawn an enemy entity"""
		if type == 1:
			enemy = canvas.create_image(spawnx, spawny, image = enemy1_image, tag=("fg","enemy","game"))
			enemystats = {
				"type": 1,
				"health" : 50,
				"movement" : movement,
				"points" : 100
			}
			return enemy, enemystats

	def saveonclose():
		"""Saves the game state on window close"""
		savestate.close()
		window.destroy()

	def saveonreturn():
		"""Saves the game state when returning to main menu"""
		savestate.close()
		menu()

	def game_loop():
		"""This is the main game loop"""

		global x, y, velx, vely, shoot, interval, pausestate, savestate, gametime, enemylist, attackinterval, score

		savestate.seek(0)
		savestate.truncate(0)

		canvas.itemconfig("game",state = "normal" )
		canvas.delete("pausebutton")

		window.protocol("WM_DELETE_WINDOW", saveonclose)

		score_label.config(text="Score: " + str(score).zfill(10))

		#Player Movement
		x, y = 0, 0

		x += velx
		y += vely

		x0, y0, x1, y1 = canvas.bbox("shipbody")

			#This set of if statements sets the bounds for the ship, if the ship reaches these bounds it will bounce off them.
		if x0 <= -100:
			x = maxvelocity
		if x1 >= 1000:
			x = -maxvelocity
		if y0 <= 0:
			y = maxvelocity
		if y1 >= 1100:
			y = -maxvelocity

		if x != 0 and y != 0:	#Normalise diagonal movement 
			x = x*(math.sqrt(2)/2)
			y = y*(math.sqrt(2)/2)

		canvas.move("ship", x, y)

		# Player Shooting
		if shoot == True:

			if not(attackinterval % 10): # % x indicates fire rate

				canvas.create_image(x0+85,y0+200, image = playerlaserstraight_image, tag=("fg","bullet","playerbullet","straight","game"))
				canvas.create_image(x1-85,y0+200, image = playerlaserstraight_image, tag=("fg","bullet","playerbullet","straight","game"))

			attackinterval += 1

		else:	# Can think of this as keeping a round in the chamber

			if (attackinterval % 10) != 0: # Fire rate number

				attackinterval += 1

			#For creating round bullets on higher ship levels
			# if interval == True:
			# 	canvas.create_image(x1,y1, image = playerlaserround_image, tag = ("fg","playerbullet","round"))
	
		canvas.move("straight", 0 , -30)
		# canvas.move("round", 0 , -150)

		for bullet in canvas.find_withtag("bullet"): # Clears bullets that exit the canvas
			if canvas.coords(bullet)[1] <= -100:
				canvas.delete(bullet)


		#Enemy Movement


		#Collisions and Damage
		for enemy in enemylist:

			enemystats = enemy[1]
			enemyitem = enemy[0]
			enemybbox = canvas.bbox(enemyitem)

			for bullet in canvas.find_withtag("playerbullet"):

				bulletbbox = canvas.bbox(bullet)

				if (bulletbbox[1] <= enemybbox[3]) and (bulletbbox[2] >= enemybbox[0]) and (bulletbbox[0] <= enemybbox[2]): #If the bullet is within the bounds of the enemy ship (Does not account for bullets hitting the top of the enemy, but this cannot not happen anyway)

					canvas.delete(bullet)
					enemystats["health"] -= 3 * ship_stats["damagemultiplier"] #Damage calculation, implement variable base damage in the future

					if enemystats["health"] <=0:

						try:
							canvas.delete(enemyitem)
							enemylist.remove(enemy)
							score += enemystats["points"]

						except ValueError:	#Catches the exception when two bullets both collide with an enemy and program tries to remove the enemy twice

							pass


		#Stages
		if gametime == 0:
			enemylist.append(enemy_spawn(1, 450, 300, "forward"))


		#Autosave
		savestate.write(str(gametime) + "~" + json.dumps(ship_stats) + "~" + json.dumps(enemylist) + "~" + str(score) + "\n")
		for item in canvas.find_withtag("game"):	# Finds every canvas item with tag "game" and saves their coordinates and configuration

			savestate.write(str(canvas.coords(item)) + "~" + str(canvas.itemconfigure(item)) + "\n")


		#Pausing
		if pausestate == True:

				canvas.itemconfig("game",state = "hidden" )

				resume_button =  Button(window, text="Resume", font = ("Impact", 50), command = game_loop )
				mainmenu_button =  Button(window, text="Main Menu", font = ("Impact", 50), command = saveonreturn)

				canvas.create_window(450,300, anchor=CENTER, window=resume_button, tags=("fg", "pausebutton"))
				canvas.create_window(450,500, anchor=CENTER, window=mainmenu_button, tags=("fg", "pausebutton"))

				pausestate = False

		else:
			gametime += 1
			window.after(16, game_loop) 

	game_loop()


window = Tk()

window.geometry('900x1080')

canvas = Canvas(window, width=900, height=1080, bg="blue")

background_image = PhotoImage(file="Assets/bkgd_0.png")
canvas.create_image(0,0, anchor=NW, image=background_image)

canvas.pack()


#Menu Titles
title_image = PhotoImage(file="Assets/placeholder.png")
settingsTitle_image = PhotoImage(file="Assets/settings.png")
controlsTitle_image = PhotoImage(file="Assets/controls.png")
about_image = PhotoImage(file="Assets/placeholder.png")


#Player Ship 
ship_image = PhotoImage(file="Assets/aship1.png")
playerlaserstraight_image = PhotoImage(file="Assets/playerlaserstraight.png")
playerlaserround_image = PhotoImage(file="Assets/playerlaserround.png")

#Enemies
enemy1_image = PhotoImage(file="Assets/enemy1.png")
menu()

window.mainloop()