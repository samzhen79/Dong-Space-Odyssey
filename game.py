from tkinter import Tk, PhotoImage, Label, Button, Canvas, Frame, messagebox, ttk, CENTER, N, NE, NW, S, SW, BOTH
from configparser import ConfigParser
import time, json, math

def menu(menutype="default"):
	"""Creates a menu, takes arguments so that different menus can be chosen"""

	canvas.delete("fg") #Removes all foreground canvas items

	settings = ConfigParser()
	settings.read("settings.ini")

	back_button = Button(window, text="Back", font = ("Impact", 50), command=menu)

	if menutype == "play":

		newgame_button = Button(window, text="New Game", font = ("Impact", 50), command = lambda menutype="chooseship": menu(menutype))
		loadgame_button = Button(window, text="Load Game", font = ("Impact", 50), command = lambda difficulty = None, ship = None, state="saved": game_start(difficulty, ship, state))


		canvas.create_window(450, 350, anchor=CENTER, window=newgame_button, tags="fg")
		canvas.create_window(450, 550, anchor=CENTER, window=loadgame_button, tags="fg")

		canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")

	elif menutype == "chooseship":

		ship = canvas.create_image(450,540,image = ship_image, tags="fg")

		choose_button = Button(window, text="Choose", font = ("Impact", 50),  command=lambda menutype="difficulty": menu(menutype))
		canvas.create_window(450,800, anchor=CENTER, window=choose_button, tags="fg")

		back_button.config(command = lambda menutype="play": menu(menutype))
		canvas.create_window(0,1080, anchor=SW, window=back_button, tags="fg")


	elif menutype == "difficulty":

		easy_button = Button(window, text="Easy", font = ("Impact", 50), command = lambda difficulty = "easy", ship = "ship": game_start(difficulty, ship))
		normal_button = Button(window, text="Normal", font = ("Impact", 50), command = lambda difficulty = "normal", ship = "ship": game_start(difficulty, ship))
		hard_button = Button(window, text="Hard", font = ("Impact", 50), command = lambda difficulty = "hard", ship = "ship": game_start(difficulty, ship))

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
		play_button = Button(window, text="Play", font = ("Impact", 50), command= lambda menutype="play": menu(menutype))
		settings_button = Button(window, text="Settings", font = ("Impact", 50), command= lambda menutype="settings": menu(menutype))
		about_button = Button(window, text="About", font = ("Impact", 50), command= lambda menutype="about": menu(menutype))
		exit_button = Button(window, text="Exit", font = ("Impact", 50), command= lambda: window.destroy())

		canvas.create_window(450,100, anchor=CENTER, window=title_label, tags="fg")
		canvas.create_window(450,350, anchor=CENTER, window=play_button, tags="fg")
		canvas.create_window(450,550, anchor=CENTER, window=settings_button, tags="fg")
		canvas.create_window(450,750, anchor=CENTER, window=about_button, tags="fg")
		canvas.create_window(450,950, anchor=CENTER, window=exit_button, tags="fg")

def changekey(control, button):
	"""Starts the control key change process, takes the specific control being changed and the value of the button that was pressed"""
	def change(key):
		"""Changes the key in the settings.ini file to hte key the user pressed"""

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

	keyprompt_label = Label(window, text="Press a key...", font = ("Impact", 30), width=500, height=600)
	keyprompt_canvaswindow = canvas.create_window(450, 540, anchor=CENTER, window=keyprompt_label, tags="fg")

	window.bind("<Key>", change)

def game_start(difficulty, ship, state="new"):
	"""Starts the game"""

	canvas.delete("fg")

	global maxvelocity, velx, vely, shoot, pausestate, savestate, gametime, enemylist, ship_stats, attackinterval, score
	maxvelocity = 8
	velx, vely, gametime, attackinterval, score = 0, 0, 0, 0, 0
	shoot, pausestate = False, False


	#Start New or Saved Game
	if state == "new": # New Game

		hitbox = canvas.create_oval(450-11,1080+116,450+12,1080+116+27, tags=("fg", "ship","game"))
		canvas.create_image(450, 1080, anchor = N, image = ship_image, tags=("fg", "game", "ship", "shipbody","gameimage"))	

		ship_stats = {
			"type": 1,
			"health": 100,
			"level": 1,
			"fireratemultiplier":	1,
			"damagemultiplier": 1,
		}

		enemylist = []
		specialenemybulletlist = []
		enemybulletspreadlist = []

		# Neat little for loop here to have the ship enter the scene with a simple animation
		for x in range(40):
			time.sleep(0.01)
			canvas.move("ship", 0, -10)
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
			specialenemybulletlist = json.loads(information[3])
			enemybulletspreadlist = json.loads(information[4])
			score = int(information[5])

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

			shipx, shipy = canvas.coords("ship")
			hitbox = canvas.create_oval(shipx-11,shipy+116,shipx+12,shipy+116+27, tags=("fg", "ship","game"))

			#Due to having to recreate all the canvas items, the item handle written in enemylist is now incorrect and must be updated with the new handle.
			i = 0
			for enemy in canvas.find_withtag("enemy"):

				enemylist[i][0] = enemy
				i += 1

			#Same for the tracking bullets and spread bullets too
			i = 0
			for bullet in canvas.find_withtag("enemybullettrack"):

				specialenemybulletlist[i][0] = bullet
				i += 1

			i = 0
			for bullet in canvas.find_withtag("enemybulletspread"):

				enemybulletspreadlist[i][0] = bullet
				i += 1

			file.close()
			savestate = open("savestate.txt", "w")


	#UI Elements
	score_label = Label(window, text="Score: " + str(score).zfill(10), font = ("Impact", 18))

	canvas.create_window(900, 0, anchor=NE, window=score_label, tags=("fg", "game"))
	healthbarbg = canvas.create_line(0, 1070, 900, 1070, fill="red", width=10, tags=("fg", "game"))
	healthbarfg = canvas.create_line(0, 1070, 900, 1070, fill="green", width=10, tags=("fg", "game"))


	#Player Movement and shooting
	settings = ConfigParser()
	settings.read("settings.ini")

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

	#Enemy spawn
	def enemy_spawn(type, spawnx, spawny, movement, stopx = 0, stopy = 0):
		"""Spawn an enemy entity, different available types of enemy"""

		if type == 1: #Regular enemy type, shoots two simple lasers
			enemy = canvas.create_image(spawnx, spawny, image = enemy1_image, tag=("fg","enemy","game","gameimage"))
			enemystats = {
				"type": 1,
				"health" : 100,
				"movement" : movement,
				"stopx" : stopx,
				"stopy" : stopy,
				"speed" : 3,
				"damage" : 10,
				"points" : 1000
			}

		elif type == 2: #Similar to type 1, but only moves horizontally and follows the player
			enemy = canvas.create_image(spawnx, spawny, image = enemy2_image, tag=("fg","enemy","game","gameimage"))
			enemystats = {
				"type": 2,
				"health" : 50,
				"movement" : "followx",
				"stopx" : stopx,
				"stopy" : stopy,
				"speed" : 4,
				"damage" : 10,
				"points" : 1000
			}

		elif type == 3: #Shoots a 3 shot burst
			enemy = canvas.create_image(spawnx, spawny, image = enemy3_image, tag=("fg","enemy","game","gameimage"))
			enemystats = {
				"type": 3,
				"health" : 150,
				"movement" : movement,
				"stopx" : stopx,
				"stopy" : stopy,
				"speed" : 3,
				"damage" : 10,
				"points" : 1500
			}

		elif type == 4:	#Slow moving also only moves horizontally, shoots a high damage tracking bullet
			enemy = canvas.create_image(spawnx, spawny, image = enemy4_image, tag=("fg","enemy","game","gameimage"))
			enemystats = {
				"type": 4,
				"health" : 100,
				"movement" : movement,
				"stopx" : stopx,
				"stopy" : stopy,
				"speed" : 1,
				"damage" : 20,
				"points" : 1500
			}

		elif type == 5: #Elite type, shoots a single round bullet (cross) that itself shoots out a bunch of round bullets
			enemy = canvas.create_image(spawnx, spawny, image = enemy5_image, tag=("fg","enemy","game","gameimage"))
			enemystats = {
				"type": 5,
				"health" : 350,
				"movement" : movement,
				"stopx" : stopx,
				"stopy" : stopy,
				"speed" : 1,
				"damage" : 10,
				"points" : 2500
			}

		elif type == "boss": #Pretty self explanatory
			enemy = canvas.create_image(spawnx, spawny, image = boss1_image, tag=("fg","enemy","game","gameimage"))
			enemystats = {
				"type": "boss",
				"health" : 5000,
				"movement" : movement,
				"stopx" : stopx,
				"stopy" : stopy,
				"speed" : 2,
				"damage" : 10,
				"points" : 100000
			}

		return enemy, enemystats

	def enemybullet(type, x, y, shipx=0, shipy=0):
		"""Spawn an enemy bullet, different types of bullets available"""

		if type == "simple": #Straight laser

			canvas.create_image(x, y, anchor=N, image=enemylaserstraight_image, tag=("fg","enemybullet","enemybulletstraight","game","gameimage"))

		elif type == "track": #Round laser that is pointed towards given player position

			bullet = canvas.create_image(x, y, anchor=N, image=enemylaserround_image, tag=("fg","enemybullet","enemybullettrack","game","gameimage"))

			#Maths to work out which direction the bullet needs to move in to move towards the player position
			bulletbbox = canvas.bbox(bullet)
			bulletx = (bulletbbox[0]+bulletbbox[2])/2
			bullety = (bulletbbox[1]+bulletbbox[3])/2
			directDist = math.sqrt(((shipx-bulletx) ** 2) + ((shipy-bullety) ** 2))
			movex = (shipx-bulletx) / directDist
			movey = (shipy-bullety) / directDist
			movementcoords = [movex*10, movey*10]

			#Need to keep track of which bullet is moving in what direction
			specialenemybulletlist.append([bullet, movementcoords])

		elif type == "radiate": #Round laser that radiates more round lasers

			bullet = canvas.create_image(x, y, anchor=N, image=enemylaserroundcross_image, tag=("fg","enemybullet","enemybulletspread","game","gameimage"))

			spreadcounter = 0

			enemybulletspreadlist.append([bullet, spreadcounter])


	#Game Saving
	def saveonclose():
		"""Saves the game state on window close"""
		savestate.close()
		window.destroy()

	def saveonreturn():
		"""Saves the game state when returning to main menu"""
		savestate.close()
		menu()

	#The Actual Game
	def game_loop():
		"""This is the main game loop"""

		global x, y, velx, vely, shoot, pausestate, savestate, gametime, ship_stats, enemylist, attackinterval, score
		savestate.seek(0)
		savestate.truncate(0)

		canvas.itemconfig("game",state = "normal" )
		canvas.delete("pausebutton")

		window.protocol("WM_DELETE_WINDOW", saveonclose)

		score_label.config(text="Score: " + str(score).zfill(10))
		canvas.coords(healthbarfg, 0, 1070, 900*(ship_stats["health"]/100), 1070) #Assuming max health is 100

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

				canvas.create_image(x0+90,y0+180, image = playerlaserstraight_image, tag=("fg","playerbullet","game","gameimage"))
				canvas.create_image(x1-90,y0+180, image = playerlaserstraight_image, tag=("fg","playerbullet","game","gameimage"))

			attackinterval += 1

		else:	# Can think of this as preloading a shot

			if (attackinterval % 10) != 0:

				attackinterval += 1

			#For creating round bullets on higher ship levels
			# 	canvas.create_image(x1,y1, image = playerlaserround_image, tag = ("fg","playerbullet"))
	
		canvas.move("playerbullet", 0 , -30)
		# canvas.move("round", 0 , -150)



		#Enemy
		for enemy in enemylist:

			enemystats = enemy[1]
			enemyitem = enemy[0]
			enemybbox = canvas.bbox(enemyitem)

			#Movement
			if enemystats["movement"] == "forward":
				canvas.move(enemyitem, 0, enemystats["speed"])
			elif enemystats["movement"] == "right":
				canvas.move(enemyitem, enemystats["speed"], 0)
			elif enemystats["movement"] == "left":
				canvas.move(enemyitem, -enemystats["speed"], 0)
			elif enemystats["movement"] == "diagonalright":
				canvas.move(enemyitem, enemystats["speed"]*(math.sqrt(2)/2), enemystats["speed"]*(math.sqrt(2)/2))
			elif enemystats["movement"] == "diagonalleft":
				canvas.move(enemyitem, -enemystats["speed"]*(math.sqrt(2)/2), enemystats["speed"]*(math.sqrt(2)/2))
			elif enemystats["movement"] == "followx": #Moves towards the x of the player ship
				shipx = (x0+x1)/2
				enemyx = (enemybbox[0]+enemybbox[2])/2
				if enemyx < shipx-2:
					canvas.move(enemyitem, enemystats["speed"], 0)
				elif enemyx > shipx+2:
					canvas.move(enemyitem, -enemystats["speed"], 0)
			elif enemystats["movement"] == "stop":
				#Maths to work out which direction to move the enemy to reach stopx and stopy
				enemyx = (enemybbox[0]+enemybbox[2])/2
				enemyy = (enemybbox[1]+enemybbox[3])/2
				directDist = math.sqrt(((enemystats["stopx"]-enemyx) ** 2) + ((enemystats["stopy"]-enemyy) ** 2))
				if directDist > 0:
					movex = (enemystats["stopx"]-enemyx) / directDist
					movey = (enemystats["stopy"]-enemyy) / directDist
					canvas.move(enemy,movex*enemystats["speed"], movey*enemystats["speed"])


			#Shooting
			if enemystats["type"] == 1:	#Types 1 and 2 shoot the same, simple two shot laser

				if not(gametime % 70):

					enemybullet("simple", enemybbox[0]+15, enemybbox[3])
					enemybullet("simple", enemybbox[2]-15, enemybbox[3])

			elif enemystats["type"] == 2:

				if not(gametime % 70):

					enemybullet("simple", enemybbox[0]+45, enemybbox[3])
					enemybullet("simple", enemybbox[2]-45, enemybbox[3])

			elif enemystats["type"] == 3:	#3 round burst fire (Not true burst fire, just spawns three lasers)

				if not(gametime % 70):

					enemybullet("simple", enemybbox[0]+24, enemybbox[3])
					enemybullet("simple", enemybbox[0]+24, enemybbox[3]+42)
					enemybullet("simple", enemybbox[0]+24, enemybbox[3]+84)

			elif enemystats["type"] == 4:	#Round laser shot towards the player, a bit more complex compared to other bullet types

				if not(gametime % 100):

					shipx = (x0+x1)/2
					shipy = (y0+y1)/2

					enemybullet("track", enemybbox[0]+76, enemybbox[3], shipx, shipy)

			elif enemystats["type"] == 5: #Special round bullet that radiates other round bullets

				if not(gametime % 150):

					enemybullet("radiate",enemybbox[0]+97, enemybbox[3])

			elif enemystats["type"] == "boss": #A combination of the shooting types

				if not(gametime % 150): #Cross Bullet

					enemybullet("radiate", enemybbox[0]+97, enemybbox[3])

				if not(gametime % 70) or not(gametime % 80) or not(gametime % 90):	#Burst fire

					enemybullet("simple", enemybbox[0]+24, enemybbox[3])
					enemybullet("simple", enemybbox[0]-24, enemybbox[3])

			#Enemy Collisions and Damage
			for bullet in canvas.find_withtag("playerbullet"):

				bulletbbox = canvas.bbox(bullet)

				if (bulletbbox[3] >= enemybbox[1]) and (bulletbbox[1] <= enemybbox[3]) and (bulletbbox[2] >= enemybbox[0]) and (bulletbbox[0] <= enemybbox[2]): #If the bullet is within the bounds of the enemy ship

					canvas.delete(bullet)
					enemystats["health"] -= 10 * ship_stats["damagemultiplier"] #Damage calculation, implement variable base damage in the future

					if enemystats["health"] <=0:

						try:
							canvas.delete(enemyitem)
							enemylist.remove(enemy)
							score += enemystats["points"]

						except ValueError:	#Catches the exception when two bullets both collide with an enemy and program tries to remove the enemy twice

							pass

		#Enemy Bullet Movement
		canvas.move("enemybulletstraight", 0, 10)

		for bullet in enemybulletspreadlist: #Loop to spawn radiating bullets around spread type bullets
			canvas.move(bullet[0], 0, 5)
			if not(bullet[1] % 50) and (bullet[1] != 0):

				bulletbbox = canvas.bbox(bullet[0])
				bulletx = (bulletbbox[0]+bulletbbox[2])/2
				bullety = (bulletbbox[1]+bulletbbox[3])/2

				dist = 2	#Spawn distance fron the cross bullet
				distdiag = dist*(math.sqrt(2)/2)
				movex = [0, distdiag, dist, distdiag, 0, -distdiag, -dist, -distdiag] #N, NE, E, SE, S, SW, W, NW
				movey = [-dist, -distdiag, 0, distdiag, dist, distdiag, 0, -distdiag]

				for i in range (8):

					bulletcreate = canvas.create_image(bulletx+movex[i], bullety+movey[i], anchor=N, image=enemylaserround_image, tag=("fg","enemybullet","enemybullettrack","game","gameimage"))

					movementcoords = [movex[i], movey[i]]

					specialenemybulletlist.append([bulletcreate, movementcoords])


			bullet[1] += 1

		for bullet in specialenemybulletlist:	#For bullets that don't go straight down

			canvas.move(bullet[0], bullet[1][0], bullet[1][1])


		#Player Collision and Damage
		for bullet in canvas.find_withtag("enemybullet"):

			bulletbbox = canvas.bbox(bullet)
			hitboxbbox = canvas.bbox(hitbox)

			if (bulletbbox[3]-12 >= hitboxbbox[1]) and (bulletbbox[1]+12 <= hitboxbbox[3]) and (bulletbbox[2]-12 >= hitboxbbox[0]) and (bulletbbox[0]+12 <= hitboxbbox[2]): 

				ship_stats["health"] -= 1 #Damage calculation, implement variable base damage in the future
				canvas.coords(healthbarfg, 0, 1070, 900*(ship_stats["health"]/100), 1070)

				#Need to make sure the bullet is also removed from the list
				for bullet2 in specialenemybulletlist:
					if bullet == bullet2[0]:
						specialenemybulletlist.remove(bullet2)

				for bullet2 in enemybulletspreadlist:
					if bullet == bullet2[0]:
						enemybulletspreadlist.remove(bullet2)

				canvas.delete(bullet)

				if ship_stats["health"] <=0:

					return

		#Stages
		if gametime == 20:
			enemylist.append(enemy_spawn(5, 225, 200, "stop", 225, 200))
			# enemylist.append(enemy_spawn(1, 625, 0, "forward"))


		#Autosave
		savestate.write(" " + str(gametime) + "~" + json.dumps(ship_stats) + "~" + json.dumps(enemylist) + "~" + json.dumps(specialenemybulletlist) + "~" +json.dumps(enemybulletspreadlist) + "~" + str(score) + "\n")
		for item in canvas.find_withtag("gameimage"):	# Finds every canvas item with tag "game" and saves their coordinates and configuration

			savestate.write(str(canvas.coords(item)) + "~" + str(canvas.itemconfigure(item)) + "\n")

		#Cleaning
		for bullet in canvas.find_withtag("playerbullet"): # Clears bullets that exit the canvas

			if canvas.coords(bullet)[1] <= -100:
				canvas.delete(bullet)

		for bullet in canvas.find_withtag("enemybullet"): # Clears bullets that exit the canvas

			if canvas.coords(bullet)[1] >= 1080+10:

				#Need to make sure the bullet is also removed from the list
				for bullet2 in specialenemybulletlist:
					if bullet == bullet2[0]:
						specialenemybulletlist.remove(bullet2)

				for bullet2 in enemybulletspreadlist:
					if bullet == bullet2[0]:
						enemybulletspreadlist.remove(bullet2)

				canvas.delete(bullet)

		for enemy in enemylist:
			enemyx, enemyy = canvas.coords(enemy[0])
			if enemyy >= 1080+200:
				canvas.delete(enemy)
				enemylist.remove(enemy)


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
#Player Bullets
playerlaserstraight_image = PhotoImage(file="Assets/playerlaserstraight.png")
playerlaserround_image = PhotoImage(file="Assets/playerlaserround.png")

#Enemies
enemy1_image = PhotoImage(file="Assets/enemy1.png")
enemy2_image = PhotoImage(file="Assets/enemy2.png")
enemy3_image = PhotoImage(file="Assets/enemy3.png")
enemy4_image = PhotoImage(file="Assets/enemy4.png")
enemy5_image = PhotoImage(file="Assets/enemy5.png")
boss1_image = PhotoImage(file="Assets/boss1.png")
#Enemy Bullets
enemylaserstraight_image = PhotoImage(file="Assets/enemylaserstraight.png")
enemylaserround_image = PhotoImage(file="Assets/enemylaserround.png")
enemylaserroundcross_image = PhotoImage(file="Assets/enemylaserroundcross.png")

menu()
window.mainloop()