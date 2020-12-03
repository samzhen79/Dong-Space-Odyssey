#Window size is 900x1017, Game was built on 3440x1440, Supports 1920x1080
#Credits:
#Background - Parallax Space Scene by LuminousDragonGames (https://opengameart.org/content/parallax-space-scene-seamlessly-scrolls-too)
#Player Ship - Modular Ships by surt (https://opengameart.org/content/modular-ships)
#Enemy Ships - Retro Spaceships by Jerom (https://opengameart.org/content/retro-spaceships)
#Bullets - Lasers and Beams by Rawdanitsu (https://opengameart.org/content/lasers-and-beams)

import json
import math
import os
import time
from configparser import ConfigParser
from tkinter import Tk, PhotoImage, Label, Button, Entry, Canvas, CENTER, N, NE, NW, SW

class Menu:

	def __init__(self, windowlength, windowheight):
		self.windowlength = windowlength
		self.windowheight = windowheight
		self.controls = []
		self.settings = ConfigParser()
		self.settings.read("settings.ini")

	def createmenu(self, menutype="default"):
		"""Creates a menu, takes arguments so that different menus can be chosen"""
		canvas.delete("fg")  # Removes all foreground canvas items

		back_button = Button(window, text="Back", font=("Impact", 50), command=self.createmenu)

		if menutype == "play":

			newgame_button = Button(window, text="New Game", font=("Impact", 50),
									command=lambda menutype="chooseship": self.createmenu(menutype))
			loadgame_button = Button(window, text="Load Game", font=("Impact", 50),
									 command=lambda windowlength=self.windowlength, windowheight=self.windowheight,
													difficulty=None, ship=None: Game(windowlength, windowheight,
																					 difficulty, ship).loadgame())

			canvas.create_window(self.windowlength / 2, 350, anchor=CENTER, window=newgame_button, tags="fg")
			canvas.create_window(self.windowlength / 2, 550, anchor=CENTER, window=loadgame_button, tags="fg")

			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")

		elif menutype == "chooseship":

			ship = canvas.create_image(self.windowlength / 2, 440, image=shipA[1], tags="fg")

			choose_button = Button(window, text="Choose", font=("Impact", 50),
								   command=lambda menutype="difficulty": self.createmenu(menutype))
			canvas.create_window(self.windowlength / 2, 700, anchor=CENTER, window=choose_button, tags="fg")

			back_button.config(command=lambda menutype="play": self.createmenu(menutype))
			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")

		elif menutype == "difficulty":

			easy_button = Button(window, text="Easy", font=("Impact", 50),
								 command=lambda windowlength=self.windowlength, windowheight=self.windowheight,
												difficulty="easy", ship="ship": Game(windowlength, windowheight,
																					 difficulty, ship).newgame())
			normal_button = Button(window, text="Normal", font=("Impact", 50),
								   command=lambda windowlength=self.windowlength, windowheight=self.windowheight,
												  difficulty="normal", ship="ship": Game(windowlength, windowheight,
																						 difficulty, ship).newgame())
			hard_button = Button(window, text="Hard", font=("Impact", 50),
								 command=lambda windowlength=self.windowlength, windowheight=self.windowheight,
												difficulty="hard", ship="ship": Game(windowlength, windowheight,
																					 difficulty, ship).newgame())

			canvas.create_window(self.windowlength / 2, 300, anchor=CENTER, window=easy_button, tags="fg")
			canvas.create_window(self.windowlength / 2, 500, anchor=CENTER, window=normal_button, tags="fg")
			canvas.create_window(self.windowlength / 2, 700, anchor=CENTER, window=hard_button, tags="fg")

			back_button.config(command=lambda menutype="chooseship": self.createmenu(menutype))
			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")

		elif menutype == "settings":

			changeshoot_button = Button(window, text="Shoot key is: \n' " + self.settings["CONTROLS"][
				"Shoot"] + " '\nPress to change key.", font=("Impact", 18),
										command=lambda control="Shoot", button=0: self.changekey(control, button))
			changeforward_button = Button(window, text="Forward key is: \n' " + self.settings["CONTROLS"][
				"Forward"] + " '\nPress to change key.", font=("Impact", 18),
										  command=lambda control="Forward", button=1: self.changekey(control, button))
			changebackward_button = Button(window, text="Backward key is: \n' " + self.settings["CONTROLS"][
				"Backward"] + " '\nPress to change key.", font=("Impact", 18),
										   command=lambda control="Backward", button=2: self.changekey(control, button))
			changeleft_button = Button(window, text="Left key is: \n' " + self.settings["CONTROLS"][
				"Left"] + " '\nPress to change key.", font=("Impact", 18),
									   command=lambda control="Left", button=3: self.changekey(control, button))
			changeright_button = Button(window, text="Right key is: \n' " + self.settings["CONTROLS"][
				"Right"] + " '\nPress to change key.", font=("Impact", 18),
										command=lambda control="Right", button=4: self.changekey(control, button))
			changepause_button = Button(window, text="Pause key is: \n' " + self.settings["CONTROLS"][
				"Pause"] + " '\nPress to change key.", font=("Impact", 18),
										command=lambda control="Pause", button=5: self.changekey(control, button))
			changebosskey_button = Button(window, text="Bosskey key is: \n' " + self.settings["CONTROLS"][
				"Bosskey"] + " '\nPress to change key.", font=("Impact", 18),
										  command=lambda control="Bosskey", button=6: self.changekey(control, button))

			self.controls = [changeshoot_button, changeforward_button, changebackward_button, changeleft_button,
							 changeright_button, changepause_button,
							 changebosskey_button]  # This is needed to update the key shown on the button

			canvas.create_image(self.windowlength / 2, 100, anchor=CENTER, image=settingsTitle_image, tags="fg")

			canvas.create_image(self.windowlength / 2, 200, anchor=CENTER, image=controlsTitle_image, tags="fg")

			canvas.create_window(self.windowlength / 2, 300, anchor=CENTER, window=changeshoot_button, tags="fg")

			canvas.create_window(self.windowlength / 2, 450, anchor=CENTER, window=changeforward_button, tags="fg")
			canvas.create_window(self.windowlength / 2, 575, anchor=CENTER, window=changebackward_button, tags="fg")
			canvas.create_window(225, 500, anchor=CENTER, window=changeleft_button, tags="fg")
			canvas.create_window(675, 500, anchor=CENTER, window=changeright_button, tags="fg")
			canvas.create_window(self.windowlength / 2, 725, anchor=CENTER, window=changepause_button, tags="fg")
			canvas.create_window(self.windowlength / 2, 850, anchor=CENTER, window=changebosskey_button, tags="fg")

			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")

		elif menutype == "howtoplay":

			canvas.create_image(self.windowlength / 2, 100, anchor=CENTER, image=howtoplayTitle_image,
													  tags="fg")
			canvas.create_image(self.windowlength / 2, 200, anchor=N, image=howtoplay_image,
													  tags="fg")

			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")

		elif menutype == "about":
			

			canvas.create_image(self.windowlength / 2, 100, anchor=CENTER, image=aboutTitle_image,
													  tags="fg")
			canvas.create_image(self.windowlength / 2, 200, anchor=N, image=about_image,
													  tags="fg")

			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")

		elif menutype == "leaderboard":

			file = open("leaderboard.txt", "r")
			leaderboard_read = file.read().split("\n")
			file.close()

			leaderboard_list = []
			for item in leaderboard_read[:-1]:
				leaderboard_list.append(json.loads(item))

			def getscore(x):

				return x["score"]

			leaderboard_list.sort(reverse=True, key=getscore)

			leaderboard_list = leaderboard_list[:25] #Only get the top 25 items

			leaderboard_text = ""
			i = 0
			for item in leaderboard_list:
				i += 1
				leaderboard_text += (str(i) + ". " + item["name"] + ": " + str(item["score"]) + "\n")

			leaderboard_label = Label(window, text=leaderboard_text, font=("Impact", 18))

			canvas.create_image(self.windowlength/2, 0+100, image=leaderboardTitle_image, tags=("fg"))
			canvas.create_window(self.windowlength/2, 0+150, anchor=N, window=leaderboard_label, tags=("fg"))

			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")


		else:  # This is the default menutype i.e. the main menu


			play_button = Button(window, text="Play", font=("Impact", 50), width=8, height=1,
								 command=lambda menutype="play": self.createmenu(menutype))
			settings_button = Button(window, text="Settings", font=("Impact", 30), width=10, height=1,
									 command=lambda menutype="settings": self.createmenu(menutype))
			about_button = Button(window, text="About", font=("Impact", 30), width=10, height=1,
								  command=lambda menutype="about": self.createmenu(menutype))
			leaderboard_button = Button(window, text="Leaderboard", font=("Impact", 30), width=10, height=1,
								  command=lambda menutype="leaderboard": self.createmenu(menutype))
			howtoplay_button = Button(window, text="How to Play", font=("Impact", 30), width=10, height=1,
								  command=lambda menutype="howtoplay": self.createmenu(menutype))
			exit_button = Button(window, text="Exit", font=("Impact", 30), command=lambda: window.destroy())

			canvas.create_image(self.windowlength / 2, 150, anchor=CENTER, image=title_image, tags="fg")
			canvas.create_window(self.windowlength / 2, 350, anchor=CENTER, window=play_button, tags="fg")
			canvas.create_window((self.windowlength / 4)+100, 500, anchor=CENTER, window=leaderboard_button, tags="fg")			
			canvas.create_window(((3*self.windowlength) / 4)-100, 500, anchor=CENTER, window=settings_button, tags="fg")
			canvas.create_window((self.windowlength / 4)+100, 650, anchor=CENTER, window=howtoplay_button, tags="fg")
			canvas.create_window(((3*self.windowlength) / 4)-100, 650, anchor=CENTER, window=about_button, tags="fg")
			canvas.create_window(self.windowlength / 2, 800, anchor=CENTER, window=exit_button, tags="fg")

	def changekey(self, control, button):
		"""Starts the control key change process, takes the specific control being changed and the value of the button that was pressed"""

		def change(key):
			"""Changes the key in the settings.ini file to hte key the user pressed"""
			canvas.delete(keyprompt_canvaswindow)

			self.settings.set("CONTROLS", control, key.keysym)

			with open("settings.ini", "w") as configfile:
				self.settings.write(configfile)

			self.settings.read("settings.ini")

			self.controls[button].config(
				text=control + " key is: \n' " + self.settings["CONTROLS"][control] + " '\nPress to change key.")

			window.unbind("<Key>")

		keyprompt_label = Label(window, text="Press a key...", font=("Impact", 30), width=500, height=600)
		keyprompt_canvaswindow = canvas.create_window(self.windowlength / 2, 540, anchor=CENTER, window=keyprompt_label,
													  tags="fg")

		window.bind("<Key>", change)
		

class Game:

	def __init__(self, windowlength, windowheight, difficulty, ship):

		self.windowlength = windowlength
		self.windowheight = windowheight

		if difficulty == "easy":
			self.damagemodifier = 0.5
		elif difficulty == "hard":
			self.damagemodifier = 2
		else:
			self.damagemodifier = 1

		self.ship = ship
		self.maxvelocity = 8
		self.velx, self.vely, self.gametime, self.attackinterval, self.expcounter, self.score = 0, 0, 0, 0, 0, 0
		self.shoot, self.pausestate, self.bossstate = False, False, False
		self.shipstats = {
			"type": 1,
			"health": 100,
			"level": 1,
			"fireratemultiplier": 1,
			"damagemultiplier": 1,
		}
		self.enemylist = []
		self.enemybulletspeciallist = []
		self.enemybulletspreadlist = []
		self.expboundaries = [1,2,4,4,6,6]

		self.settings = ConfigParser()
		self.settings.read("settings.ini")

		# These are all for the purpose of performance optimisation
		self.forwardkey = self.settings["CONTROLS"]["Forward"].upper()
		self.backwardkey = self.settings["CONTROLS"]["Backward"].upper()
		self.leftkey = self.settings["CONTROLS"]["Left"].upper()
		self.rightkey = self.settings["CONTROLS"]["Right"].upper()
		self.shootkey = self.settings["CONTROLS"]["Shoot"].upper()
		self.pausekey = self.settings["CONTROLS"]["Pause"].upper()
		self.bosskey = self.settings["CONTROLS"]["Bosskey"].upper()
		self.bbox = canvas.bbox
		self.move = canvas.move
		self.createimage = canvas.create_image
		self.gettags = canvas.gettags
		self.delete = canvas.delete
		self.sqrt = math.sqrt
		self.circlesin = [0.0, 0.71, 1.0, 0.71, 0.0, -0.71, -1.0, -0.71]
		self.circlecos = [1.0, 0.71, 0.0, -0.71, -1.0, -0.71, -0.0, 0.71]


	# Start New or Saved Game
	def newgame(self):  # New Game

		canvas.delete("fg")

		self.hitbox = canvas.create_oval(windowlength / 2 - 11, windowheight + 116, windowlength / 2 + 12,
										 windowheight + 116 + 27, tags=("fg", "ship", "game"))

		canvas.create_image(windowlength / 2, windowheight, anchor=N, image=shipA[1],
							tags=("fg", "game", "ship", "shipbody", "gameimage"))

		# Neat little for loop here to have the ship enter the scene with a simple animation
		for x in range(40):
			time.sleep(0.01)
			self.move("ship", 0, -10)
			window.update()

		# UI Elements
		self.score_label = Label(window, text="Score: " + str(self.score).zfill(10), font=("Impact", 18))

		canvas.create_window(windowlength, 0, anchor=NE, window=self.score_label, tags=("fg", "game"))
		healthbarbg = canvas.create_line(0, self.windowheight - 10, self.windowlength, self.windowheight - 10,
										 fill="red", width=10, tags=("fg", "game"))
		self.healthbarfg = canvas.create_line(0, self.windowheight - 10, self.windowlength, self.windowheight - 10,
											  fill="green", width=10, tags=("fg", "game"))

		# Start game loop
		canvas.bind_all("<KeyPress>", self.key_press)
		canvas.bind_all("<KeyRelease>", self.key_release)
		self.game_loop()

	def loadgame(self):  # Load saved game, if no saved game available then starts a new game

		canvas.delete("fg")

		if os.path.getsize("savestate.txt") == 0:  # If no saved game then start new game

			Menu(self.windowlength, self.windowheight).createmenu("chooseship")

		else:

			file = open("savestate.txt", "r")

			savestateobjects = file.read().splitlines()
			information = savestateobjects[0].split("~")
			self.gametime = int(information[0])
			self.shipstats = json.loads(information[1])
			self.attackinterval = int(information[2])
			self.enemylist = json.loads(information[3])
			self.enemybulletspeciallist = json.loads(information[4])
			self.enemybulletspreadlist = json.loads(information[5])
			self.score = int(information[6])

			for object in savestateobjects[1:]:
				# This code is needed to interpret the savestate.txt, Effectively splits the text file into the necessary parts and then cleans each part until it is useable in create_image()
				object = object.split("~")

				coords = object[0].replace("[", "")
				coords = coords.replace("]", "")
				coords = coords.split(", ")

				config = object[1][1:-1].replace("'',", "")
				config = config.split("), ")

				anchor = config[1][34:-1]

				image = config[3][23:-1]

				tags = config[5][21:-2].split()
				tagstring = ""

				for tag in tags:
					tagstring += '"' + str(tag) + '", '

				tagstring = tagstring[0:-2]

				# creates the needed objects from the interpreted savestate.txt
				canvas.create_image(coords[0], coords[1], anchor=anchor, image=image, tags=(eval(tagstring)))

			shipx, shipy = canvas.coords("ship")
			self.hitbox = canvas.create_oval(shipx - 11, shipy + 116, shipx + 12, shipy + 116 + 27,
											 tags=("fg", "ship", "game"))

			# Due to having to recreate all the canvas items, the item handle written in self.enemylist is now incorrect and must be updated with the new handle.
			i = 0
			for enemy in canvas.find_withtag("enemy"):
				self.enemylist[i]["id"] = enemy
				i += 1

			# Same for the tracking bullets and spread bullets too
			i = 0
			for bullet in canvas.find_withtag("enemybulletspecial"):
				self.enemybulletspeciallist[i]["id"] = bullet
				i += 1

			i = 0
			for bullet in canvas.find_withtag("enemybulletspread"):
				self.enemybulletspreadlist[i]["id"] = bullet
				i += 1

			file.close()

			# UI Elements
			self.score_label = Label(window, text="Score: " + str(self.score).zfill(10), font=("Impact", 18))

			canvas.create_window(windowlength, 0, anchor=NE, window=self.score_label, tags=("fg", "game"))
			healthbarbg = canvas.create_line(0, self.windowheight - 10, self.windowlength, self.windowheight - 10,
											 fill="red", width=10, tags=("fg", "game"))
			self.healthbarfg = canvas.create_line(0, self.windowheight - 10, self.windowlength, self.windowheight - 10,
												  fill="green", width=10, tags=("fg", "game"))

			# Player Movement and shooting
			canvas.bind_all("<KeyPress>", self.key_press)
			canvas.bind_all("<KeyRelease>", self.key_release)

			# Start game loop
			self.game_loop()

	def key_press(self, event):
		"""Records key presses for controls"""

		# Movement
		if event.keysym.upper() == self.forwardkey and self.vely > -self.maxvelocity:
			self.vely -= self.maxvelocity
		elif event.keysym.upper() == self.backwardkey and self.vely < self.maxvelocity:
			self.vely += self.maxvelocity
		elif event.keysym.upper() == self.leftkey and self.velx > -self.maxvelocity:
			self.velx -= self.maxvelocity
		elif event.keysym.upper() == self.rightkey and self.velx < self.maxvelocity:
			self.velx += self.maxvelocity

		# Shooting
		elif event.keysym.upper() == self.shootkey:
			self.shoot = True

		# Pause
		elif event.keysym.upper() == self.pausekey:
			self.pausestate = True
		elif event.keysym.upper() == self.bosskey:
			self.bossstate = True

	def key_release(self, event):
		"""Records when a key is released for movement and shooting"""

		# Movement
		if event.keysym.upper() == self.forwardkey:
			self.vely += self.maxvelocity
		elif event.keysym.upper() == self.backwardkey:
			self.vely -= self.maxvelocity
		elif event.keysym.upper() == self.leftkey:
			self.velx += self.maxvelocity
		elif event.keysym.upper() == self.rightkey:
			self.velx -= self.maxvelocity

		# Shooting
		elif event.keysym.upper() == self.shootkey:
			self.shoot = False

	# Enemy spawn  
	def enemy_spawn(self, type, spawnx, spawny, movement=0, stopx=0, stopy=0, healthmultiplier=1):
		"""Spawn an enemy entity, different available types of enemy"""

		if type == 1:  # Regular enemy type, shoots two simple lasers
			enemy = self.createimage(spawnx, spawny, image=enemy1_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": 1,
				"health": 75*healthmultiplier,
				"movement": movement,
				"stopx": stopx,
				"stopy": stopy,
				"speed": 3,
				"damage": 10,
				"points": 1000
			}

		elif type == 2:  # Similar to type 1, but only moves horizontally and follows the player
			enemy = self.createimage(spawnx, spawny, image=enemy2_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": 2,
				"health": 200*healthmultiplier,
				"movement": "followx",
				"stopx": stopx,
				"stopy": stopy,
				"speed": 2,
				"damage": 10,
				"points": 1000
			}

		elif type == 3:  # Shoots a 3 shot burst
			enemy = self.createimage(spawnx, spawny, image=enemy3_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": 3,
				"health": 100*healthmultiplier,
				"movement": movement,
				"stopx": stopx,
				"stopy": stopy,
				"speed": 3,
				"damage": 10,
				"points": 1500
			}

		elif type == 4:  # Slow moving also only moves horizontally, shoots a high damage tracking bullet
			enemy = self.createimage(spawnx, spawny, image=enemy4_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": 4,
				"health": 150*healthmultiplier,
				"movement": movement,
				"stopx": stopx,
				"stopy": stopy,
				"speed": 1,
				"damage": 20,
				"points": 1500
			}

		elif type == 5:  # Elite type, shoots a single round bullet (cross) that itself shoots out a bunch of round bullets
			enemy = self.createimage(spawnx, spawny, image=enemy5_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": 5,
				"health": 500*healthmultiplier,
				"movement": movement,
				"stopx": stopx,
				"stopy": stopy,
				"speed": 1,
				"damage": 10,
				"points": 2500
			}

		elif type == "boss":  # Pretty self explanatory
			enemy = self.createimage(spawnx, spawny, image=boss1_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": "boss",
				"health": 5000,
				"movement": movement,
				"stopx": stopx,
				"stopy": stopy,
				"speed": 2,
				"damage": 10,
				"points": 100000
			}

		self.enemylist.append({"id": enemy, "stats": enemystats, "attackcounter": 0})

	def enemybullet(self, type, x, y, shipx=0, shipy=0):
		"""Spawn an enemy bullet, different types of bullets available"""

		if type == "simple":  # Straight laser

			self.createimage(x, y, anchor=N, image=enemylaserstraight_image,
							 tag=("fg", "enemybullet", "enemybulletstraight", "game", "gameimage"))

		elif type == "special":  # Round laser that is pointed towards given player position

			bullet = self.createimage(x, y, anchor=N, image=enemylaserround_image,
									  tag=("fg", "enemybullet", "enemybulletspecial", "game", "gameimage"))

			# Maths to work out which direction the bullet needs to move in to move towards the player position
			bulletx0, bullety0, bulletx1, bullety1 = self.bbox(bullet)
			bulletx = (bulletx0 + bulletx1) / 2
			bullety = (bullety0 + bullety1) / 2
			directDist = self.sqrt(((shipx - bulletx) ** 2) + ((shipy - bullety) ** 2))
			movex = (shipx - bulletx) / directDist
			movey = (shipy - bullety) / directDist

			# Need to keep track of which bullet is moving in what direction
			self.enemybulletspeciallist.append({"id": bullet, "x": round(movex * 5), "y": round(movey * 5)})

		elif type == "radiate":  # Round laser that radiates more round lasers

			bullet = self.createimage(x, y, anchor=N, image=enemylaserroundcross_image,
									  tag=("fg", "enemybullet", "enemybulletspread", "game", "gameimage"))

			spreadcounter = 0

			self.enemybulletspreadlist.append({"id": bullet, "counter": spreadcounter})

	# Game Saving
	def saveonclose(self):
		"""Saves the game state on window close"""
		self.savestate = open("savestate.txt", "w")
		self.savestate.write(" " + str(self.gametime) + "~" + json.dumps(self.shipstats) + "~" + str(
			self.attackinterval) + "~" + json.dumps(self.enemylist) + "~" + json.dumps(
			self.enemybulletspeciallist) + "~" + json.dumps(self.enemybulletspreadlist) + "~" + str(
			self.score) + "\n")

		for item in canvas.find_withtag(
				"gameimage"):  # Finds every canvas item with tag "game" and saves their coordinates and configuration

			self.savestate.write(str(canvas.coords(item)) + "~" + str(canvas.itemconfigure(item)) + "\n")

		self.savestate.close()
		window.destroy()

	def saveonreturn(self):
		"""Saves the game state when returning to main menu. Just closes the savestate.txt file, actually saving happens on pause"""
		window.protocol("WM_DELETE_WINDOW", window.destroy)
		Menu(self.windowlength, self.windowheight).createmenu()

	# The Actual Game
	def game_loop(self):
		"""This is the main game loop"""

		canvas.itemconfig("game", state="normal")
		self.delete("pausebutton")

		window.protocol("WM_DELETE_WINDOW", self.saveonclose)

		self.score_label.config(text="Score: " + str(self.score).zfill(10))
		canvas.coords(self.healthbarfg, 0, self.windowheight - 10, self.windowlength * (self.shipstats["health"] / 100),
					  self.windowheight - 10)  # Assuming max health is 100

		# Player Movement
		x, y = 0, 0

		x += self.velx
		y += self.vely

		x0, y0, x1, y1 = self.bbox("shipbody")

		# This set of if statements sets the bounds for the ship, if the ship reaches these bounds it will bounce off them.
		if x0 <= -100:
			x = self.maxvelocity
		if x1 >= 1000:
			x = -self.maxvelocity
		if y0 <= 0:
			y = self.maxvelocity
		if y1 >= 1100:
			y = -self.maxvelocity

		if x != 0 and y != 0:  # Normalise diagonal movement
			x = x * (self.sqrt(2) / 2)
			y = y * (self.sqrt(2) / 2)

		self.move("ship", round(x), round(y))


		# Player Shooting
		if self.shoot:

			shiplevel = self.shipstats["level"]

			#Ship levels 1 and 2 use similar sprites, levels 3-5 use similar sprites
			if shiplevel <= 2: #Levels 1 and 2

				if not(self.attackinterval % 10):  # % x indicates fire rate

					#Single side lasers
					self.createimage(x0 + 90, y0 + 180, image=playerlaserstraight_image,
									 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
					self.createimage(x1 - 90, y0 + 180, image=playerlaserstraight_image,
									 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))

					if shiplevel == 2:

						#Lasers are now doubled
						self.createimage(x0 + 90, y0 + 130, image=playerlaserstraight_image,
										 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
						self.createimage(x1 - 90, y0 + 130, image=playerlaserstraight_image,
										 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))


			elif shiplevel <= 5: #Levels 3-5

				if not(self.attackinterval % 10): #Level 3

					#Double side lasers
					self.createimage(x0 + 70, y0 + 160, image=playerlaserstraight_image,
									 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
					self.createimage(x0 + 70, y0 + 110, image=playerlaserstraight_image,
									 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
					self.createimage(x1 - 70, y0 + 160, image=playerlaserstraight_image,
									 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
					self.createimage(x1 - 70, y0 + 110, image=playerlaserstraight_image,
									 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))

					#Single middle laser
					self.createimage((x0+x1)/2, y0 + 90, image=playerlaserstraight_image,
									 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))

					if shiplevel == 5: #Level 5

							#Double side laser #2
							self.createimage(x0 + 45, y0 + 160, image=playerlaserstraight_image,
											 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
							self.createimage(x0 + 45, y0 + 110, image=playerlaserstraight_image,
											 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
							self.createimage(x1 - 45, y0 + 160, image=playerlaserstraight_image,
											 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))
							self.createimage(x1 - 45, y0 + 110, image=playerlaserstraight_image,
											 tag=("fg", "playerbulletstraight", "playerbullet", "game", "gameimage"))

				if shiplevel > 3: #Level 4

					if not(self.attackinterval % 30):

						#Single side round laser
						self.createimage((x0+x1)/2 + 30, y0 + 130, image=playerlaserround_image,
										 tag=("fg", "playerbulletround", "playerbullet", "game", "gameimage"))
						self.createimage((x0+x1)/2 - 30, y0 + 130, image=playerlaserround_image,
										 tag=("fg", "playerbulletround", "playerbullet", "game", "gameimage"))

			self.attackinterval += 1

		else:  # Can think of this as preloading a shot

			if (self.attackinterval % 30) != 0:
				self.attackinterval += 1

		self.move("playerbulletstraight", 0, -30)
		self.move("playerbulletround", 0 , -15)

		# Enemy
		for enemy in self.enemylist:

			enemystats = enemy["stats"]
			enemymovement = enemystats["movement"]
			enemyspeed = enemystats["speed"]
			enemytype = enemystats["type"]
			enemyid = enemy["id"]
			enemyattackcounter = enemy["attackcounter"]
			enemy["attackcounter"] += 1
			enemyx0, enemyy0, enemyx1, enemyy1 = self.bbox(enemyid)

			# Movement
			if enemymovement == "forward":
				self.move(enemyid, 0, enemyspeed/2)
			elif enemymovement == "right":
				self.move(enemyid, enemyspeed, 0)
			elif enemymovement == "left":
				self.move(enemyid, -enemyspeed, 0)
			elif enemymovement == "diagonalright":
				self.move(enemyid, enemyspeed * (self.sqrt(2) / 2), enemyspeed * (self.sqrt(2) / 2))
			elif enemymovement == "diagonalleft":
				self.move(enemyid, -enemyspeed * (self.sqrt(2) / 2), enemyspeed * (self.sqrt(2) / 2))
			elif enemymovement == "followx":  # Moves towards the x of the player ship
				shipx = (x0 + x1) / 2
				enemyx = (enemyx0 + enemyx1) / 2
				if enemyx < shipx - 2:
					self.move(enemyid, enemyspeed, 0)
				elif enemyx > shipx + 2:
					self.move(enemyid, -enemyspeed, 0)
			elif enemymovement == "stop":
				# Maths to work out which direction to move the enemy to reach stopx and stopy
				enemyx = (enemyx0 + enemyx1) / 2
				enemyy = (enemyy0 + enemyy1) / 2
				directDist = self.sqrt(((enemystats["stopx"] - enemyx) ** 2) + ((enemystats["stopy"] - enemyy) ** 2))
				if directDist > 5:
					movex = (enemystats["stopx"] - enemyx) / directDist
					movey = (enemystats["stopy"] - enemyy) / directDist
					self.move(enemyid, movex * enemyspeed * 2, movey * enemyspeed * 2)

			# Shooting
			if enemytype == 1:  # Types 1 and 2 shoot the same, simple two shot laser

				if not (enemyattackcounter % 70):
					self.enemybullet("simple", enemyx0 + 15, enemyy1)
					self.enemybullet("simple", enemyx1 - 15, enemyy1)

			elif enemytype == 2:

				if not (enemyattackcounter % 70):
					self.enemybullet("simple", enemyx0 + 45, enemyy1)
					self.enemybullet("simple", enemyx1 - 45, enemyy1)

			elif enemytype == 3:  # 3 round burst fire (Not true burst fire, just spawns three lasers)

				if not (enemyattackcounter % 70):
					self.enemybullet("simple", enemyx0 + 24, enemyy1)
					self.enemybullet("simple", enemyx0 + 24, enemyy1 + 42)
					self.enemybullet("simple", enemyx0 + 24, enemyy1 + 84)

			elif enemytype == 4:  # Round laser shot towards the player, a bit more complex compared to other bullet types

				if not (enemyattackcounter % 100):
					shipx = (x0 + x1) / 2
					shipy = (y0 + y1) / 2

					self.enemybullet("special", enemyx0 + 76, enemyy1, shipx, shipy)

			elif enemytype == 5:  # Special round bullet that radiates other round bullets

				if not (enemyattackcounter % 150):
					self.enemybullet("radiate", enemyx0 + 97, enemyy1)

			elif enemytype == "boss":  # A combination of the shooting types

				if not(enemyattackcounter % 300):
					self.enemybullet("simple", enemyx0 + 420, enemyy1)

				if not(enemyattackcounter % 200):
					self.enemybullet("radiate", enemyx0 + 100, enemyy1)
					self.enemybullet("radiate", enemyx1 - 100, enemyy1)

				if not(enemyattackcounter % 100):
					shipx = (x0 + x1) / 2
					shipy = (y0 + y1) / 2
					self.enemybullet("special", enemyx0 + 200, enemyy1, shipx, shipy)
					self.enemybullet("special", enemyx1 - 200, enemyy1, shipx, shipy)

			# Enemy Collisions and Damage
			for collision in canvas.find_overlapping(enemyx0, enemyy0, enemyx1, enemyy1):

				tags = self.gettags(collision)

				if "playerbullet" in tags:

					self.delete(collision)

					if "playerbulletround" in tags:

						enemystats["health"] -= 24 * self.shipstats["damagemultiplier"]

					else:

						enemystats["health"] -= 8 * self.shipstats["damagemultiplier"]

					if enemystats["health"] <= 0:

						try:
							self.delete(enemyid)
							self.enemylist.remove(enemy)
							self.score += enemystats["points"]

							#Level up mechanic
							if enemytype == 5:

								self.expcounter += 1

								if (self.shipstats["level"] < 5) and (self.expcounter == self.expboundaries[self.expcounter-1]) :

									self.shipstats["level"] += 1

									canvas.itemconfig("shipbody", image=shipA[self.shipstats["level"]])


						except ValueError:  # Catches the exception when two bullets both collide with an enemy and program tries to remove the enemy twice

							pass

		# Enemy Bullet Movement
		self.move("enemybulletstraight", 0, 8)

		self.move("enemybulletspread", 0, 5)
		for bullet in self.enemybulletspreadlist:  # Loop to spawn radiating bullets around spread type bullets
			bulletcounter = bullet["counter"]
			if not (bulletcounter % 50) and (bulletcounter != 0):

				bulletx0, bullety0, bulletx1, bullety1 = self.bbox(bullet["id"])
				bulletx = (bulletx0 + bulletx1) / 2
				bullety = (bullety0 + bullety1) / 2

				dist = 2  # Spawn distance fron the cross bullet

				append = self.enemybulletspeciallist.append

				for i in range(8):
					movex = self.circlesin[i]*dist
					movey = self.circlecos[i]*dist
					bulletcreate = self.createimage(bulletx + movex, bullety + movey, anchor=N,
													image=enemylaserround_image,
													tag=(
														"fg", "enemybullet", "enemybulletspecial", "game", "gameimage"))

					append({"id": bulletcreate, "x": movex, "y": movey})

			bullet["counter"] += 1

		for bullet in self.enemybulletspeciallist:  # For bullets that don't go straight down

			self.move(bullet["id"], bullet["x"], bullet["y"])

		# Player Collision and Damage
		hitboxx0, hitboxy0, hitboxx1, hitboxy1 = self.bbox(self.hitbox)
		possiblecollisions = canvas.find_overlapping(hitboxx0 + 12, hitboxy0 + 12, hitboxx1 - 12, hitboxy1 - 12)
		for collision in possiblecollisions:

			tags = self.gettags(collision)

			if "enemybullet" in tags:

				self.shipstats["health"] -= 10 * self.damagemodifier  # Damage calculation, implement variable base damage in the future

				# Need to make sure the bullet is also removed from the list
				remove = self.enemybulletspeciallist.remove
				for bullet2 in self.enemybulletspeciallist:
					if collision == bullet2["id"]:
						remove(bullet2)
						break

				remove = self.enemybulletspreadlist.remove
				for bullet2 in self.enemybulletspreadlist:
					if collision == bullet2["id"]:
						remove(bullet2)
						break

				self.delete(collision)

			elif "enemy" in tags: #Contact damage

				self.shipstats["health"] -= 0.5

			if self.shipstats["health"] <= 0:
				self.addtoleaderboard()
				return

		# Cleaning
		possibleitems = canvas.find_overlapping(0-200, 0-200, self.windowlength+200, self.windowheight)
		for item in canvas.find_withtag("game"):
			if item in possibleitems:
				pass
			else:
				remove = self.enemylist.remove
				for item2 in self.enemylist:
					if item == item2["id"]:
						remove(item2)
						break
				remove = self.enemybulletspeciallist.remove
				for item2 in self.enemybulletspeciallist:
					if item == item2["id"]:
						remove(item2)
						break
				remove = self.enemybulletspreadlist.remove
				for item2 in self.enemybulletspreadlist:
					if item == item2["id"]:
						remove(item2)
						break
				self.delete(item)

		# Pausing
		if self.pausestate or self.bossstate:

			# Game Save
			self.savestate = open("savestate.txt", "w")

			self.savestate.write(" " + str(self.gametime) + "~" + json.dumps(self.shipstats) + "~" + str(
				self.attackinterval) + "~" + json.dumps(self.enemylist) + "~" + json.dumps(
				self.enemybulletspeciallist) + "~" + json.dumps(self.enemybulletspreadlist) + "~" + str(
				self.score) + "\n")
			for item in canvas.find_withtag(
					"gameimage"):  # Finds every canvas item with tag "game" and saves their coordinates and configuration

				self.savestate.write(str(canvas.coords(item)) + "~" + str(canvas.itemconfigure(item)) + "\n")

			self.savestate.close()

			canvas.itemconfig("game", state="hidden")

			if self.pausestate:

				resume_button = Button(window, text="Resume", font=("Impact", 50), command=self.game_loop)
				mainmenu_button = Button(window, text="Main Menu", font=("Impact", 50), command=self.saveonreturn)

				canvas.create_window(self.windowlength / 2, 300, anchor=CENTER, window=resume_button,
									 tags=("fg", "pausebutton"))
				canvas.create_window(self.windowlength / 2, 500, anchor=CENTER, window=mainmenu_button,
									 tags=("fg", "pausebutton"))

			elif self.bossstate:

				resume_button = Button(window, text="Resume", font=("Impact", 15), command=self.game_loop)

				self.createimage(0, 0, anchor=NW, image=bosskey_image, tags=("fg", "pausebutton"))
				canvas.create_window(0, 1017, anchor=SW, window=resume_button, tags=("fg", "pausebutton"))

			self.pausestate = False
			self.bossstate = False

		else:
			self.gametime += 1
			# print(self.gametime) #For helping level design
			canvas.after(16, self.startstage)

	def addtoleaderboard(self):
		"""Shows current leaderboard and gives the player the option to add their score to the leaderboard"""
		canvas.delete("fg")

		window.protocol("WM_DELETE_WINDOW", window.destroy)

		self.score = self.score*self.damagemodifier #Higher difficulty gives more points

		yourscore_label = Label(window, text="Your Score: " + str(self.score).zfill(10), font=("Impact", 30))
		yourname_label = Label(window, text="Your Name: ", font=("Impact", 20))
		self.name_entry = Entry(window, font=("Impact", 20))
		nameadd_button = Button(window, text="Add", font=("Impact", 20), command= self.add)
		back_button = Button(window, text="Back", font=("Impact", 50), command=Menu(self.windowlength, self.windowheight).createmenu)

		file = open("leaderboard.txt", "r")
		leaderboard_read = file.read().split("\n")
		file.close()

		leaderboard_list = []
		for item in leaderboard_read[:-1]:
			leaderboard_list.append(json.loads(item))

		def getscore(x):

			return x["score"]

		leaderboard_list.sort(reverse=True, key=getscore)

		leaderboard_text = ""
		i = 0
		for item in leaderboard_list[:25]:
			i += 1
			leaderboard_text += (str(i) + ". " + item["name"] + ": " + str(item["score"]) + "\n")

		leaderboard_label = Label(window, text=leaderboard_text, font=("Impact", 15))

		canvas.create_window(self.windowlength/2, 0+100, window=yourscore_label, tags=("fg"))
		canvas.create_window((self.windowlength/2)-210, 0+175, window=yourname_label, tags=("fg"))
		canvas.create_window(self.windowlength/2, 0+175, window=self.name_entry, tags=("fg"))
		canvas.create_window((self.windowlength/2)+180, 0+175, window=nameadd_button, tags=("fg"))
		canvas.create_image(self.windowlength/2, 0+250, image=leaderboardTitle_image, tags=("fg"))
		canvas.create_window(self.windowlength/2, 0+300, anchor=N, window=leaderboard_label, tags=("fg"))

		canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")

	def add(self):
		"""Adds the name given and score to the leaderboard file"""
		name = self.name_entry.get()

		leaderboardentry = {"name": name, "score": self.score}

		file = open("leaderboard.txt", "a")
		file.write(json.dumps(leaderboardentry) + "\n")
		file.close()

		Menu(self.windowlength, self.windowheight).createmenu("leaderboard")

	def startstage(self):
		"""Spawns a set of enemies for the level dependent on gametime."""

		gametime = self.gametime
		enemy_spawn = self.enemy_spawn

		#A cleaner way of doing this may be to create a function which creates predetermined patterns.
		if gametime == 1: #Single type 1 on left and right 
			enemy_spawn(1, 450, -100, "stop", 225, 200, 0.5)
			enemy_spawn(1, 450, -100, "stop", 675, 200, 0.5)

		elif gametime == 500:	#2 type 1 stacked on either side

			enemy_spawn(1, 450, -100, "stop", 225, 200, 0.5)
			enemy_spawn(1, 450, -100, "stop", 675, 200, 0.5)
			enemy_spawn(1, 450, -100, "stop", 225, 400, 0.5)
			enemy_spawn(1, 450, -100, "stop", 675, 400, 0.5)

		elif gametime == 1000:	#2 type 1 stacked on either side

			enemy_spawn(1, 450, -100, "stop", 225, 200, 0.5)
			enemy_spawn(1, 450, -100, "stop", 675, 200, 0.5)
			enemy_spawn(1, 450, -100, "stop", 225, 400, 0.5)
			enemy_spawn(1, 450, -100, "stop", 675, 400, 0.5)

		elif gametime == 1500:	#2 type 1 in the middle, 1 type 1 on either side moving across screen

			enemy_spawn(1, 450, -100, "stop", 350, 300)
			enemy_spawn(1, 450, -100, "stop", 550, 300)
			enemy_spawn(1, -100, 100, "right")
			enemy_spawn(1, 1000, 150, "left")

		elif gametime == 2000: #2 type 2 entering from the sides, 1 type 1 on either side moving across screen

			enemy_spawn(2, -100, 200)
			enemy_spawn(2, 1000, 100)
			enemy_spawn(1, -100, 300, "right")
			enemy_spawn(1, 1000, 400, "left")

		elif (gametime >= 2100) and (gametime < 2700): #1 type 1 on either side moving across screen, 2 times

			if not(gametime % 100):
				enemy_spawn(1, -100, 300, "right")
				enemy_spawn(1, 1000, 400, "left")

		elif gametime == 2700: #Elite spawn

			enemy_spawn(5, 450, -100, "stop", 450, 250)

#-----------------------------------------------------------------------------------

		elif gametime == 3500: #2 type 1 in middle, type 3 on either side

			enemy_spawn(1, 450, -100, "stop", 350, 100)
			enemy_spawn(1, 450, -100, "stop", 550, 100)
			enemy_spawn(3, 225, -100, "stop", 225, 200)
			enemy_spawn(3, 675, -100, "stop", 675, 200)

		elif gametime == 4100: #Some additional type 1 into the middle

			enemy_spawn(1, 450, -100, "stop", 350, 200)
			enemy_spawn(1, 450, -100, "stop", 550, 200)

		elif gametime == 4500: #2 type 2 entering from the side, 2 stacked type 1 on either side

			enemy_spawn(2, -100, 200)
			enemy_spawn(2, 1000, 100)
			enemy_spawn(1, 450, -100, "stop", 225, 300)
			enemy_spawn(1, 450, -100, "stop", 675, 300)
			enemy_spawn(1, 450, -100, "stop", 225, 400)
			enemy_spawn(1, 450, -100, "stop", 675, 400)

		elif (gametime >= 4700) and (gametime < 5500): #Multiple type 1 coming down from the top right and top left

			if not(gametime % 100):
				enemy_spawn(1, -100, -100, "diagonalright")
				enemy_spawn(1, 1000, -100, "diagonalleft")

		elif gametime == 5500: #2 type 4 in middle, type 3 on either side

			enemy_spawn(3, 225, -100, "stop", 225, 350)
			enemy_spawn(3, 675, -100, "stop", 675, 350)
			enemy_spawn(4, 350, -100, "stop", 350, 350)
			enemy_spawn(4, 550, -100, "stop", 550, 350)

		elif (gametime >= 5500) and (gametime < 6100): #Multiple type 1 going right and left

			if not(gametime % 200):
				enemy_spawn(1, -100, 100, "right")
				enemy_spawn(1, 1000, 200, "left")

		elif gametime == 6500: #Elite 2, has 2 type 4 on each side

			enemy_spawn(5, 450, -100, "stop", 450, 250, 1.5)
			enemy_spawn(4, 350, -100, "stop", 225, 350)
			enemy_spawn(4, 550, -100, "stop", 675, 350)
			enemy_spawn(4, 350, -100, "stop", 225, 250)
			enemy_spawn(4, 550, -100, "stop", 675, 250)

#-----------------------------------------------------------------------------------

		elif gametime == 7500: #Type 2 entering from each side, type 3 going across diagonally, 2 type 1 going down the center.

			enemy_spawn(2, -100, 200, 0, 0, 0, 1.2)
			enemy_spawn(2, 1000, 100, 0, 0, 0, 1.2)
			enemy_spawn(3, -100, -100, "diagonalright", 0, 0, 1.2)
			enemy_spawn(3, 1000, -100, "diagonalleft", 0, 0, 1.2)
			enemy_spawn(1, 350, -100, "forward", 0, 0, 1.2)
			enemy_spawn(1, 550, -100, "forward", 0, 0, 1.2)

		elif gametime == 8000: #Diagonal pattern from center to right of type 1's, set of 4 type 4 on the left

			enemy_spawn(1, 450, -100, "stop", 450, 50, 1.2)
			enemy_spawn(1, 450, -100, "stop", 550, 100, 1.2)
			enemy_spawn(1, 450, -100, "stop", 650, 150, 1.2)
			enemy_spawn(1, 450, -100, "stop", 750, 200, 1.2)
			enemy_spawn(1, 450, -100, "stop", 850, 250, 1.2)
			enemy_spawn(4, 225, -100, "stop", 225, 200, 1.2)
			enemy_spawn(4, 225, -100, "stop", 225, 350, 1.2)
			enemy_spawn(4, 300, -100, "stop", 300, 200, 1.2)
			enemy_spawn(4, 300, -100, "stop", 300, 350, 1.2)

		elif gametime == 9000: #Diagonal pattern from center to right of type 1's, set of 4 type 4 on the left

			enemy_spawn(1, 450, -100, "stop", 450, 50, 1.2)
			enemy_spawn(1, 450, -100, "stop", 350, 100, 1.2)
			enemy_spawn(1, 450, -100, "stop", 250, 150, 1.2)
			enemy_spawn(1, 450, -100, "stop", 150, 200, 1.2)
			enemy_spawn(1, 450, -100, "stop", 50, 250, 1.2)
			enemy_spawn(4, 650, -100, "stop", 650, 200, 1.2)
			enemy_spawn(4, 650, -100, "stop", 650, 350, 1.2)
			enemy_spawn(4, 500, -100, "stop", 500, 200, 1.2)
			enemy_spawn(4, 500, -100, "stop", 500, 350, 1.2)

		elif gametime == 10000: #2 type 3 in the center

			enemy_spawn(3, 350, -100, "stop", 350, 300, 1.2)
			enemy_spawn(3, 550, -100, "stop", 550, 300, 1.2)

		elif gametime >= 10000 and gametime < 11500: #Type 4 going across the top from left to right, type 1 going down either side

			if not(gametime % 200):

				enemy_spawn(4, -100, 100, "right", 0, 0, 1.2)

			if not(gametime % 200):

				enemy_spawn(1, 225, -100, "forward", 0, 0, 1.2)
				enemy_spawn(1, 675, -100, "forward", 0, 0, 1.2)

		elif gametime == 12000: #Elite 3, 2 type 5 on either side

			enemy_spawn(5, 225, -100, "stop", 225, 250, 1.5)
			enemy_spawn(5, 625, -100, "stop", 625, 250, 1.5)

#-----------------------------------------------------------------------------------

		elif gametime >= 13500 and gametime <15500: #Series of type 4 going from top right to bottom left, periodic type 2 entering from left

			if not(gametime % 100):

				enemy_spawn(4, -100, -150, "diagonalright", 0, 0, 2)

			if not(gametime % 250):

				enemy_spawn(1, 450, -100, "stop", 450, 150, 1.5)
				enemy_spawn(2, 1000, 100, 0, 0, 0, 2)

		elif gametime == 16000: #Group of 4 type 1 on either side, 2 tanky type 4 in the middle

			enemy_spawn(1, 200, -150, "stop", 200, 100, 1.5)
			enemy_spawn(1, 200, -100, "stop", 200, 150, 1.5)
			enemy_spawn(1, 300, -150, "stop", 300, 100, 1.5)
			enemy_spawn(1, 300, -100, "stop", 300, 150, 1.5)
			enemy_spawn(1, 700, -150, "stop", 700, 100, 1.5)
			enemy_spawn(1, 700, -100, "stop", 700, 150, 1.5)
			enemy_spawn(1, 600, -150, "stop", 600, 100, 1.5)
			enemy_spawn(1, 600, -100, "stop", 600, 150, 1.5)

			enemy_spawn(4, 350, -100, "stop", 350, 150, 4)
			enemy_spawn(4, 550, -100, "stop", 550, 150, 4)

		elif gametime >= 16000 and gametime < 17000: #Periodic type 3 moving down the middle

			if not(gametime % 200):

				enemy_spawn(3, 450, -100, "forward", 0, 0, 2)

		elif gametime == 17000 and gametime < 18000: #Same as 13500

			if not(gametime % 100):

				enemy_spawn(4, 1000, -150, "diagonalleft", 0, 0, 2)

			if not(gametime % 250):

				enemy_spawn(1, 450, -100, "stop", 450, 150, 1.5)
				enemy_spawn(2, 100, 100, 0, 0, 0, 2)

		elif gametime == 18500: #Elite 4, 2 type 5 on either side

			enemy_spawn(5, 225, -100, "stop", 225, 250, 1.5)
			enemy_spawn(5, 625, -100, "stop", 625, 250, 1.5)

		elif gametime >= 18500 and gametime <= 20000 and self.enemylist == None: #Periodic type 4 in the center

			if not(gametime % 200):

				enemy_spawn(4, 350, -100, "stop", 350, 150, 4)
				enemy_spawn(4, 550, -100, "stop", 550, 150, 4)				

		self.game_loop()

window = Tk()
windowlength = 900
windowheight = 1017
window.geometry(str(windowlength) + "x" + str(windowheight))
window.title("Dong Space Odyssey")

canvas = Canvas(window, width=windowlength, height=windowheight, bg="blue")

background_image = PhotoImage(file="Assets/bkgd_0.png")
canvas.create_image(0, 0, anchor=NW, image=background_image, tag="bg")

canvas.pack()

# Menu Titles
title_image = PhotoImage(file="Assets/Title.png")
settingsTitle_image = PhotoImage(file="Assets/Settings.png")
howtoplayTitle_image = PhotoImage(file="Assets/howtoplaytitle.png")
aboutTitle_image = PhotoImage(file="Assets/About.png")
controlsTitle_image = PhotoImage(file="Assets/controls.png")
leaderboardTitle_image = PhotoImage(file="Assets/leaderboard.png")

# Content Images
howtoplay_image = PhotoImage(file="Assets/howtoplaytext.png")
about_image = PhotoImage(file="Assets/abouttext.png")
bosskey_image = PhotoImage(file="Assets/excel-data-1.png")

# Player Ship
shipA = {1: PhotoImage(file="Assets/aship1.png"), 
		2: PhotoImage(file="Assets/aship2.png"),
		3: PhotoImage(file="Assets/aship3.png"), 
		4: PhotoImage(file="Assets/aship4.png"),
		5: PhotoImage(file="Assets/aship5.png")}

# Player Bullets
playerlaserstraight_image = PhotoImage(file="Assets/playerlaserstraight.png")
playerlaserround_image = PhotoImage(file="Assets/playerlaserround.png")

# Enemies
enemy1_image = PhotoImage(file="Assets/enemy1.png")
enemy2_image = PhotoImage(file="Assets/enemy2.png")
enemy3_image = PhotoImage(file="Assets/enemy3.png")
enemy4_image = PhotoImage(file="Assets/enemy4.png")
enemy5_image = PhotoImage(file="Assets/enemy5.png")
boss1_image = PhotoImage(file="Assets/boss1.png")
# Enemy Bullets
enemylaserstraight_image = PhotoImage(file="Assets/enemylaserstraight.png")
enemylaserround_image = PhotoImage(file="Assets/enemylaserround.png")
enemylaserroundcross_image = PhotoImage(file="Assets/enemylaserroundcross.png")

Menu(windowlength, windowheight).createmenu()
window.mainloop()
