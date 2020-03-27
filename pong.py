from tkinter import *
from random import randrange
def init_pong():
	#declaration
	global game
	global gamearea
	global game_running
	global x_speed
	global y_speed
	global home
	global away
	global home_score
	global away_score
	global home_text
	global away_text
	global pauseLabel

	#setup the scoreboard
	game = Tk()
	game.title('Game')
	home_score = IntVar()
	away_score = IntVar()
	home_score.set(0)
	away_score.set(0)
	home_text = StringVar()
	away_text = StringVar()
	home_text.set('Home-Team \n'+ str(home_score.get()))
	away_text.set('Away-Team \n'+ str(away_score.get()))
	home = Label(game, text=home_text.get())
	home.grid(row=0,column=0,sticky=W)
	away = Label(game, text=away_text.get())
	away.grid(row=0,column=1, sticky=E)

	#setup the gamearea
	game_running = False
	gamearea = Canvas(game, width=1000, height=500)
	gamearea.grid(row=2,column=0, columnspan=2)
	gamearea.grid_propagate(False)
	lower_border = gamearea.create_line(5,500,995,500)
	upper_border = gamearea.create_line(5,2,995,2)
	homegoal = gamearea.create_line(10,500,10,0,width=10,fill="blue")
	awaygoal = gamearea.create_line(990,0,990,500,width=10,fill="red")
	homekeeper = gamearea.create_line(20,300,20,200,width=5,tags="homekeeper")
	awaykeeper = gamearea.create_line(980,300,980,200,width=5,tags="awaykeeper")
	ball = gamearea.create_oval(490,220,510,240,fill="black",tags="ball")
	pauseLabel = Label(game,text="Press SPACE to start the Game. \nPress Esc to quit the Game.")
	pauseLabel.grid()
	reset_movement()
	#gamearea.bind('<B1-Motion>',move_home)
	game.bind('w',move_home)
	game.bind('s',move_home)
	game.bind('<Up>',move_away)
	game.bind('<Down>',move_away)
	game.bind('<space>',pauseUnpause)
	game.bind('<Escape>',quit_game)
	game.bind('<Key>',showKey)

def showKey(event):
	print(event.keysym)

def reset_movement():
	#ball speed
	global x_speed
	global y_speed

	x_speed = randrange(-36,37,5)*0.02
	y_speed = randrange(-36,37,5)*0.02

	#movehome
def move_home(event):
	global gamearea
	if event.keysym == "w" or event.keysym == "s":
		if event.keysym =="w":
			ay = -5
		if event.keysym =="s":
			ay = 5
		itemtag = "homekeeper"
		if gamearea.coords(itemtag)[1] >= 103.0 and gamearea.coords(itemtag)[1] <= 500.0:
	 		gamearea.move(itemtag,0,ay)
		if gamearea.coords(itemtag)[1] > 500.0:
			gamearea.coords(itemtag,20,500,20,400)
		elif gamearea.coords(itemtag)[1] < 103.0:
			gamearea.coords(itemtag,20,103,20,3)

	#moveaway
def move_away(event):
	global gamearea
	if event.keysym == "Up" or event.keysym == "Down":
		if event.keysym =="Up":
			ay = -5
		if event.keysym =="Down":
			ay = 5
		itemtag = "awaykeeper"
		if gamearea.coords(itemtag)[1] >= 103.0 and gamearea.coords(itemtag)[1] <= 500.0:
	 		gamearea.move(itemtag,0,ay)
		if gamearea.coords(itemtag)[1] > 500.0:
			gamearea.coords(itemtag,20,500,20,400)
		elif gamearea.coords(itemtag)[1] < 103.0:
			gamearea.coords(itemtag,20,103,20,3)
	#pauseUnpause
def pauseUnpause(event):
	global game
	global game_running
	global pauseLabel
	if game_running == False:
		game_running = True
		start_game()
		try:
			pauseLabel.grid_remove()  #causes much traffic cause old messages wont be deleted from the RAM
		except NameError:
			print('No Pause Label defined')
	elif game_running == True:
		game_running = False
		pauseLabel = Label(game,text="Game is paused. \nPress SPACE to continue. \nPress Esc to quit the Game.")
		pauseLabel.grid()

def scoring(team):
	global home_score
	global away_score
	global gamearea
	global game_running
	global home_text
	global away_text
	global home
	global away

	if game_running == True:
		game_running = False
		if team == "Home":
			home_score.set(home_score.get()+1)
			home_text.set("Home-Team \n" + str(home_score.get()))
			home.config(text=home_text.get())
		else:
			away_score.set(away_score.get()+1)
			away_text.set("Away-Team \n" + str(away_score.get()))
			away.config(text=away_text.get())
		gamearea.coords("ball",490,220,510,240)
		reset_movement()


def start_game():
	#ball game
	global x_speed
	global y_speed
	global gamearea
	global game_running

	if game_running == True:
		if gamearea.coords("ball")[1] <= 2: #upper border
			y_speed = abs(y_speed)
		elif gamearea.coords("ball")[3] >= 500: #lower border
			y_speed = -y_speed
		elif gamearea.coords("ball")[2] >= 980 and \
			(gamearea.coords("ball")[1] < gamearea.coords("awaykeeper")[1] and \
			 gamearea.coords("ball")[3] > gamearea.coords("awaykeeper")[3]): #away side
			x_speed = -x_speed
		elif gamearea.coords("ball")[0] <= 20 and \
			(gamearea.coords("ball")[1] < gamearea.coords("homekeeper")[1] and \
			 gamearea.coords("ball")[3] > gamearea.coords("homekeeper")[3]): #home side
			x_speed = abs(x_speed)
			x_speed = x_speed + (x_speed*0.3)
			y_speed = y_speed + (y_speed*0.3)
		elif gamearea.coords("ball")[0] <= 10:	#this is a score for the awayteam
			scoring("Away")
		elif gamearea.coords("ball")[2] >= 990:	#this is a score for the hometeam
			scoring("Home")
		gamearea.move("ball", x_speed, y_speed)
		root.after(1,start_game)
def quit_game(event):
	global game
	global game_running

	if game_running == False:
		game.quit()

#mainwindow and setup
root = Tk()
root.title('Pong')
#first info to read for the user
#choose if 1 or 2 players / mouse or keyboard
message = Label(root,text='This is the game Pong.')
message.grid(row=0)
#Button to start Game
start_btn = Button(root, text='Start Game', width=20,command=init_pong)
start_btn.grid(row=1, sticky=W)

#environment for TKinter
root.mainloop()
