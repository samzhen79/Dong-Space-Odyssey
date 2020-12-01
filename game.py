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

			ship = canvas.create_image(self.windowlength / 2, 440, image=ship_image, tags="fg")

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

		elif menutype == "about":

			about_label = Label(window, image=about_image)
			about_canvaswindow = canvas.create_window(self.windowlength / 2, 800, anchor=CENTER, window=about_label,
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

			leaderboard_list = leaderboard_list[:24] #Only get the top 25 items

			leaderboard_text = ""
			i = 0
			for item in leaderboard_list:
				i += 1
				leaderboard_text += (str(i) + ". " + item["name"] + ": " + str(item["score"]) + "\n")

			leaderboard_label = Label(window, text=leaderboard_text, font=("Impact", 20))

			canvas.create_image(self.windowlength/2, 0+100, image=leaderboardTitle_image, tags=("fg"))
			canvas.create_window(self.windowlength/2, 0+250, window=leaderboard_label, tags=("fg"))

			canvas.create_window(0, self.windowheight, anchor=SW, window=back_button, tags="fg")


		else:  # This is the default menutype i.e. the main menu

			title_label = Label(window, image=title_image)
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

			canvas.create_window(self.windowlength / 2, 100, anchor=CENTER, window=title_label, tags="fg")
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
		self.difficulty = difficulty
		self.ship = ship
		self.maxvelocity = 8
		self.velx, self.vely, self.gametime, self.attackinterval, self.score = 0, 0, 0, 0, 0
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

		self.settings = ConfigParser()
		self.settings.read("settings.ini")

		# These are all for the purpose of performance
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
		self.sin = math.sin
		self.cos = math.cos
		self.pi = math.pi

	# Start New or Saved Game
	def newgame(self):  # New Game

		canvas.delete("fg")

		self.hitbox = canvas.create_oval(windowlength / 2 - 11, windowheight + 116, windowlength / 2 + 12,
										 windowheight + 116 + 27, tags=("fg", "ship", "game"))
		canvas.create_image(windowlength / 2, windowheight, anchor=N, image=ship_image,
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

		print(os.path.getsize("savestate.txt"))

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
				self.enemylist[i][0] = enemy
				i += 1

			# Same for the tracking bullets and spread bullets too
			i = 0
			for bullet in canvas.find_withtag("enemybulletspecial"):
				self.enemybulletspeciallist[i]["id"] = bullet
				i += 1

			i = 0
			for bullet in canvas.find_withtag("enemybulletspread"):
				self.enemybulletspreadlist[i][0] = bullet
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
	def enemy_spawn(self, type, spawnx, spawny, movement, stopx=0, stopy=0):
		"""Spawn an enemy entity, different available types of enemy"""

		if type == 1:  # Regular enemy type, shoots two simple lasers
			enemy = self.createimage(spawnx, spawny, image=enemy1_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": 1,
				"health": 100,
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
				"health": 50,
				"movement": "followx",
				"stopx": stopx,
				"stopy": stopy,
				"speed": 4,
				"damage": 10,
				"points": 1000
			}

		elif type == 3:  # Shoots a 3 shot burst
			enemy = self.createimage(spawnx, spawny, image=enemy3_image, tag=("fg", "enemy", "game", "gameimage"))
			enemystats = {
				"type": 3,
				"health": 150,
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
				"health": 100,
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
				"health": 350,
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

		self.enemylist.append({"id": enemy, "stats": enemystats})

	def enemybullet(self, type, x, y, shipx=0, shipy=0):
		"""Spawn an enemy bullet, different types of bullets available"""

		if type == "simple":  # Straight laser

			self.createimage(x, y, anchor=N, image=enemylaserstraight_image,
							 tag=("fg", "enemybullet", "enemybulletstraight", "game", "gameimage"))

		elif type == "special":  # Round laser that is pointed towards given player position

			bullet = self.createimage(x, y, anchor=N, image=enemylaserround_image,
									  tag=("fg", "enemybullet", "enemybulletspecial", "game", "gameimage"))

			# Maths to work out which direction the bullet needs to move in to move towards the player position
			bulletx0, bullety0, bulletx1, bullety1 = self.bbox(bullet["id"])
			bulletx = (bulletx0 + bulletx1) / 2
			bullety = (bullety0 + bullety1) / 2
			directDist = self.sqrt(((shipx - bulletx) ** 2) + ((shipy - bullety) ** 2))
			movex = (shipx - bulletx) / directDist
			movey = (shipy - bullety) / directDist

			# Need to keep track of which bullet is moving in what direction
			self.enemybulletspeciallist.append({"id": bullet, "x": round(movex * 10, 2), "y": round(movey * 10, 2)})

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

			if not (self.attackinterval % 10):  # % x indicates fire rate

				self.createimage(x0 + 90, y0 + 180, image=playerlaserstraight_image,
								 tag=("fg", "playerbullet", "game", "gameimage"))
				self.createimage(x1 - 90, y0 + 180, image=playerlaserstraight_image,
								 tag=("fg", "playerbullet", "game", "gameimage"))

			self.attackinterval += 1

		else:  # Can think of this as preloading a shot

			if (self.attackinterval % 10) != 0:
				self.attackinterval += 1

		# For creating round bullets on higher ship levels
		# 	createimage(x1,y1, image = playerlaserround_image, tag = ("fg","playerbullet"))

		self.move("playerbullet", 0, -30)
		# move("round", 0 , -150)

		# Enemy
		for enemy in self.enemylist:

			enemystats = enemy["stats"]
			enemymovement = enemystats["movement"]
			enemyspeed = enemystats["speed"]
			enemytype = enemystats["type"]
			enemyid = enemy["id"]
			enemyx0, enemyy0, enemyx1, enemyy1 = self.bbox(enemyid)
			# Movement
			if enemymovement == "forward":
				self.move(enemyid, 0, enemyspeed)
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
				if directDist > 1:
					movex = (enemystats["stopx"] - enemyx) / directDist
					movey = (enemystats["stopy"] - enemyy) / directDist
					self.move(enemyid, movex * enemyspeed, movey * enemyspeed)

			# Shooting
			if enemytype == 1:  # Types 1 and 2 shoot the same, simple two shot laser

				if not (self.gametime % 70):
					self.enemybullet("simple", enemyx0 + 15, enemyy1)
					self.enemybullet("simple", enemyx1 - 15, enemyy1)

			elif enemytype == 2:

				if not (self.gametime % 70):
					self.enemybullet("simple", enemyx0 + 45, enemyy1)
					self.enemybullet("simple", enemyx1 - 45, enemyy1)

			elif enemytype == 3:  # 3 round burst fire (Not true burst fire, just spawns three lasers)

				if not (self.gametime % 70):
					self.enemybullet("simple", enemyx0 + 24, enemyy1)
					self.enemybullet("simple", enemyx0 + 24, enemyy1 + 42)
					self.enemybullet("simple", enemyx0 + 24, enemyy1 + 84)

			elif enemytype == 4:  # Round laser shot towards the player, a bit more complex compared to other bullet types

				if not (self.gametime % 100):
					shipx = (x0 + x1) / 2
					shipy = (y0 + y1) / 2

					self.enemybullet("special", enemyx0 + 76, enemyy1, shipx, shipy)

			elif enemytype == 5:  # Special round bullet that radiates other round bullets

				if not (self.gametime % 150):
					self.enemybullet("radiate", enemyx0 + 97, enemyy1)

			elif enemytype == "boss":  # A combination of the shooting types

				if not (self.gametime % 150):  # Cross Bullet

					self.enemybullet("radiate", enemyx0 + 97, enemyy1)

			# Enemy Collisions and Damage
			for collision in canvas.find_overlapping(enemyx0, enemyy0, enemyx1, enemyy1):

				if "playerbullet" in self.gettags(collision):

					self.delete(collision)

					enemystats["health"] -= 10 * self.shipstats["damagemultiplier"]

					if enemystats["health"] <= 0:

						try:
							self.delete(enemyid)
							self.enemylist.remove(enemy)
							self.score += enemystats["points"]

						except ValueError:  # Catches the exception when two bullets both collide with an enemy and program tries to remove the enemy twice

							pass

		# Enemy Bullet Movement
		self.move("enemybulletstraight", 0, 10)

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
					movex = dist * self.sin(self.pi * (i / 4))
					movey = dist * self.cos(self.pi * (i / 4))
					bulletcreate = self.createimage(bulletx + movex, bullety + movey, anchor=N,
													image=enemylaserround_image,
													tag=(
														"fg", "enemybullet", "enemybulletspecial", "game", "gameimage"))

					append({"id": bulletcreate, "x": round(movex, 2), "y": round(movey, 2)})

			bullet["counter"] += 1

		for bullet in self.enemybulletspeciallist:  # For bullets that don't go straight down

			self.move(bullet["id"], bullet["x"], bullet["y"])

		# Player Collision and Damage
		hitboxx0, hitboxy0, hitboxx1, hitboxy1 = self.bbox(self.hitbox)
		possiblecollisions = canvas.find_overlapping(hitboxx0 + 12, hitboxy0 + 12, hitboxx1 - 12, hitboxy1 - 12)
		for collision in possiblecollisions:

			if "enemybullet" in self.gettags(collision):

				self.shipstats["health"] -= 5  # Damage calculation, implement variable base damage in the future

				# Need to make sure the bullet is also removed from the list
				remove = self.enemybulletspeciallist.remove
				for bullet2 in self.enemybulletspeciallist:
					if collision == bullet2["id"]:
						remove(bullet2)

				remove = self.enemybulletspreadlist.remove
				for bullet2 in self.enemybulletspreadlist:
					if collision == bullet2["id"]:
						remove(bullet2)

				self.delete(collision)

				if self.shipstats["health"] <= 0:
					self.addtoleaderboard()
					return

		# Cleaning
		possibleitems = canvas.find_overlapping(0, 0, self.windowlength, self.windowheight)
		for item in canvas.find_withtag("game"):
			if item in possibleitems:
				pass
			else:
				remove = self.enemylist.remove
				for item2 in self.enemylist:
					if item == item2["id"]:
						remove(item2)
				remove = self.enemybulletspeciallist.remove
				for item2 in self.enemybulletspeciallist:
					if item == item2["id"]:
						remove(item2)
				remove = self.enemybulletspreadlist.remove
				for item2 in self.enemybulletspreadlist:
					if item == item2["id"]:
						remove(item2)
				self.delete(item)

		# Stages
		if self.gametime == 20:
			self.enemy_spawn(5, 225, 200, "stop", 225, 200)
			self.enemy_spawn(3, 275, 200, "stop", 275, 200)
			self.enemy_spawn(3, 325, 200, "stop", 325, 200)
			self.enemy_spawn(3, 375, 200, "stop", 375, 200)
			self.enemy_spawn(3, 425, 200, "stop", 425, 200)
			self.enemy_spawn(3, 475, 200, "stop", 475, 200)
			self.enemy_spawn(3, 525, 200, "stop", 525, 200)
			self.enemy_spawn(3, 575, 200, "stop", 575, 200)
			self.enemy_spawn(3, 625, 200, "stop", 625, 200)
			self.enemy_spawn(3, 675, 200, "stop", 675, 200)
			self.enemy_spawn(3, 725, 200, "stop", 725, 200)
		# self.enemylist.append(enemy_spawn(1, 625, 0, "forward"))

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
			canvas.after(16, self.game_loop)

	def addtoleaderboard(self):
		"""Shows current leaderboard and gives the player the option to add their score to the leaderboard"""
		canvas.delete("fg")

		window.protocol("WM_DELETE_WINDOW", window.destroy)

		yourscore_label = Label(window, text="Your Score: " + str(self.score).zfill(10), font=("Impact", 30))
		yourname_label = Label(window, text="Your Name: ", font=("Impact", 20))
		self.name_entry = Entry(window, font=("Impact", 20))
		nameadd_button = Button(window, text="Add", font=("Impact", 20), command= self.add)

		file = open("leaderboard.txt", "r")
		leaderboard_read = file.read().split("\n")
		file.close()

		leaderboard_list = []
		for item in leaderboard_read:
			leaderboard_list.append(json.loads(item))

		def getscore(x):

			return x["score"]

		leaderboard_list.sort(reverse=True, key=getscore)

		leaderboard_list = leaderboard_list[:24] #Only get the top 25 items

		leaderboard_text = ""
		i = 0
		for item in leaderboard_list:
			i += 1
			leaderboard_text += (str(i) + ". " + item["name"] + ": " + str(item["score"]) + "\n")

		leaderboard_label = Label(window, text=leaderboard_text, font=("Impact", 20))

		canvas.create_window(self.windowlength/2, 0+100, window=yourscore_label, tags=("fg"))
		canvas.create_window((self.windowlength/2)-210, 0+175, window=yourname_label, tags=("fg"))
		canvas.create_window(self.windowlength/2, 0+175, window=self.name_entry, tags=("fg"))
		canvas.create_window((self.windowlength/2)+180, 0+175, window=nameadd_button, tags=("fg"))
		canvas.create_image(self.windowlength/2, 0+225, image=leaderboardTitle_image, tags=("fg"))
		canvas.create_window(self.windowlength/2, 0+300, window=leaderboard_label, tags=("fg"))

	def add(self):
		"""Adds the name given and score to the leaderboard file"""
		name = self.name_entry.get()

		leaderboardentry = {"name": name, "score": self.score}

		file = open("leaderboard.txt", "a")
		file.write(json.dumps(leaderboardentry) + "\n")
		file.close()

		Menu(self.windowlength, self.windowheight).createmenu("leaderboard")

window = Tk()
windowlength = 900
windowheight = 1017
window.geometry(str(windowlength) + "x" + str(windowheight))

canvas = Canvas(window, width=windowlength, height=windowheight, bg="blue")

background_image = PhotoImage(file="Assets/bkgd_0.png")
canvas.create_image(0, 0, anchor=NW, image=background_image, tag="bg")

canvas.pack()

# Menu Titles
title_image = PhotoImage(file="Assets/placeholder.png")
settingsTitle_image = PhotoImage(file="Assets/settings.png")
controlsTitle_image = PhotoImage(file="Assets/controls.png")
leaderboardTitle_image = PhotoImage(file="Assets/leaderboard.png")

# Content Images
about_image = PhotoImage(file="Assets/placeholder.png")
bosskey_image = PhotoImage(file="Assets/excel-data-1.png")

# Player Ship
ship_image = PhotoImage(file="Assets/aship1.png")
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
