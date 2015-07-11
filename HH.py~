# Ryan M. Salerno
# January 2015
#
# Holocene Hero
#
# A 2D video game created using Pygame

#--------------------- General Setup ---------------------#

# Import statements
import pygame
import sys
import random
import webbrowser

# Import Sanctuary.py
from Sanctuary import Animal

# Initialize pygame
pygame.init()

# Initialize the fonts
try:
    pygame.font.init()
except:
    print "Fonts unavailable"
    sys.exit()

# Create a clock
gameClock = pygame.time.Clock()

# Create a state variable
state = "StartScreen"

size = width, height = 550, 900

# Create a screen (width, height)
screen = pygame.display.set_mode( size )

# Import the background
background = pygame.image.load( "background.png" ).convert_alpha()
background1 = pygame.image.load( "background1.png" ).convert_alpha()
background2 = pygame.image.load( "background2.png" ).convert_alpha()
icon = pygame.image.load( "icon.png" ).convert_alpha()

# Mute Button
muteButton = pygame.image.load( "volmute.png" ).convert_alpha()
volOnButton = pygame.image.load( "volon.png" ).convert_alpha()

# Music option
musicOn = True

# Load and play music
pygame.mixer.music.load( "theme1.wav" )
pygame.mixer.music.play( -1 )

# Sex of the hero
sex = ""

# Import the test tubes
sOne = pygame.image.load( "salmon_testtube.png" ).convert_alpha()
sTwo = pygame.image.load( "purple_testtube.png" ).convert_alpha()
sThree = pygame.image.load( "orange_testtube.png" ).convert_alpha()
sFour = pygame.image.load( "green_testtube.png" ).convert_alpha()
sFive = pygame.image.load( "gray_testtube.png" ).convert_alpha()
sSix = pygame.image.load( "gold_testtube.png" ).convert_alpha()
sSeven = pygame.image.load( "cyan_testtube.png" ).convert_alpha()
sEight = pygame.image.load( "brown_testtube.png" ).convert_alpha()
sNine = pygame.image.load( "blue_testtube.png" ).convert_alpha()
sTen = pygame.image.load( "black_testtube.png" ).convert_alpha()

# Level completion setup
oneCompleted = False
twoCompleted = False
threeCompleted = False
fourCompleted = False
fiveCompleted = False

# Bio boo's
oneBio = False
twoBio = False
threeBio = False
fourBio = False
fiveBio = False
sixBio = False
sevenBio = False
eightBio = False
nineBio = False
tenBio = False

#------------------- End General Setup ------------------#


#------------------- StartScreen Setup ------------------#
startButton = pygame.image.load( "Start_Game.png" ).convert_alpha()
creditsButton = pygame.image.load( "creditsButton.png" ).convert_alpha()
getInvolvedButton = pygame.image.load( "Get_Involved.png" ).convert_alpha()
quitButton = pygame.image.load( "Quit.png" ).convert_alpha()
#----------------- End StartScreen Setup ----------------#


#------------------- GetInvolved Setup ------------------#
# Create new fonts
dfont = pygame.font.SysFont( "Helvetica", 28, bold=False )
#----------------- End GetInvolved Setup ----------------#


#----------------- DifficultyScreen Setup ---------------#
# Difficulty field

difficulty = 0

# Create new font
ffont = pygame.font.SysFont( "Magnum", 40, bold=False )
#--------------- End DifficultyScreen Setup -------------#


#------------------- ReadyScreen Setup ------------------#
# Start a counter
readyTick = 0

# Create the new font
gfont = pygame.font.SysFont( "full Pack 2025", 60, bold=False )
#------------------ End ReadyScreen Setup ---------------#

#--------------------- Context Setup --------------------#
contextImage = pygame.image.load( "Instructions_Screen.png" ).convert_alpha()
contextTimer = pygame.image.load( "timerContext.png" ).convert_alpha()
contextNeeded = pygame.image.load( "amountContext.png" ).convert_alpha()

congrats = pygame.image.load( "congratulations.png" ).convert_alpha()
#-------------------- End Context Setup -----------------#


#--------------------- Credits Setup --------------------#
creditList = pygame.image.load( "credits.png" ).convert_alpha()
#-------------------- End Credits Setup -----------------#

#--------------------- Sanctuary Setup --------------------#
map1 = pygame.image.load( "map1.png" ).convert_alpha()
map2 = pygame.image.load( "map2.png" ).convert_alpha()
map3 = pygame.image.load( "map3.png" ).convert_alpha()
map4 = pygame.image.load( "map4.png" ).convert_alpha()
map5 = pygame.image.load( "map5.png" ).convert_alpha()

bioOne = pygame.image.load( "hawksbillturtlebio.png" ).convert_alpha()
bioTwo = pygame.image.load( "carribeanmonksealbio.png" ).convert_alpha()
bioThree = pygame.image.load( "giantayeayebio.png" ).convert_alpha()
bioFour = pygame.image.load( "pacificsalmonbio.png" ).convert_alpha()
bioFive = pygame.image.load( "blackrhinobio.png" ).convert_alpha()
bioSix = pygame.image.load( "woolymammothbio.png" ).convert_alpha()
bioSeven = pygame.image.load( "quaggabio.png" ).convert_alpha()
bioEight = pygame.image.load( "saolabio.png" ).convert_alpha()
bioNine = pygame.image.load( "dodobio.png" ).convert_alpha()
bioTen = pygame.image.load( "frogbio.png" ).convert_alpha()
#-------------------- End Sanctuary Setup -----------------#


#------------------- MainPlay Content -------------------#
#
# SETUP
#

# Image imports

lastPos = 0

mspider = pygame.image.load( "MaleSpider.png" ).convert_alpha()
mspider2 = pygame.image.load( "MaleSpider2.png" ).convert_alpha()
mspider3 = pygame.image.load( "MaleSpider3.png" ).convert_alpha()

fspider = pygame.image.load( "FemaleSpider.png" ).convert_alpha()
fspider2 = pygame.image.load( "FemaleSpider2.png" ).convert_alpha()
fspider3 = pygame.image.load( "FemaleSpider2.png" ).convert_alpha()

failureImage = pygame.image.load( "failure.png" ).convert_alpha()

sancBackFemale = pygame.image.load( "sancBackFemale.png" ).convert_alpha()
sancBackMale = pygame.image.load( "sancBackMale.png" ).convert_alpha()

spiderRect = fspider.get_rect()
spiderRect.move_ip( 160, 30 )

dot = pygame.image.load( "dot.png" ).convert_alpha()

# Level One Objects
neededL1 = pygame.image.load( "needed1.png" ).convert_alpha()
neededL2 = pygame.image.load( "needed2.png" ).convert_alpha()
neededL3 = pygame.image.load( "needed3.png" ).convert_alpha()
neededL4 = pygame.image.load( "needed4.png" ).convert_alpha()
neededL5 = pygame.image.load( "needed5.png" ).convert_alpha()

# Enemy Objects
enemy = pygame.image.load( "EnemySpider.png" ).convert_alpha()

# Set the speed
speed = [0, 0]

# Sound effects
testTubeSound = pygame.mixer.Sound( "collecttesttube.wav" )

# Countdown setup
levelCountdownTicks = 0
levelCountdown = 0

#
# ENEMY SETUP
#

# Maximum number of enemies and their minimum spawn time

maxEnemies = 10
minSpawnTime = 120

# Store a list of active enemies
activeEnemies = []

# Record the ticks since last spawn
ticksSinceSpawn = 0

# Enemy speed
eSpeed = [0, -1]

#
# SPECIES SETUP
#

# Maximum number of species and their minimum spawn time
maxSpecies = 1
minSpeciesOneSpawnTime = 0
minSpeciesTwoSpawnTime = 0

# Store a list of active species
activeOneSpecies = []
activeTwoSpecies = []

# Record the ticks since last species spawn
ticksSinceSpeciesOneSpawn = 0
ticksSinceSpeciesTwoSpawn = 0

# Species speed
sSpeed = [0, -1]

# Acquired setup
oneAcq = False
twoAcq = False

# Keep track of the number of each acquired
numOneAcq = 0
numTwoAcq = 0

# Level setup
level = ""

#------------------ End MainPlay Setup -----------------#

#------------------- Main Event Loop -------------------#
	
while 1:

	#####################
	# STARTSCREEN STATE #
	#####################
	
	if state == "StartScreen":
		# Draw the start screen background
		screen.blit( background2, ( 0, 0 ) )
		
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on start button
				if startRect.collidepoint(pos):
					# Go to the MainPlay state
					state = "Context"
				elif getInvolvedRect.collidepoint(pos):
					# Go to the GetInvolved state
					state = "GetInvolved"
				elif creditsRect.collidepoint(pos):
					# Go to the Credits state
					state = "Credits"
				# Click on the mute button
				elif muteRect.collidepoint(pos):
					# Mute/Turn on the volume
					if musicOn == True:
						pygame.mixer.music.pause()
						musicOn = False
					elif musicOn == False:
						pygame.mixer.music.unpause()
						musicOn = True
				# Click on quit button
				elif quitRect.collidepoint(pos):
					# Quit the game
					sys.exit()
		
		# # Create the start button
		# startRect = startButton.get_rect()
		# startRect.move_ip( 60, 225 )
		# screen.blit( startButton, startRect )
		
		startRect = startButton.get_rect()
		startRect.move_ip( 182, 300 )
		creditsRect = creditsButton.get_rect()
		creditsRect.move_ip( 210, 400 )
		getInvolvedRect = getInvolvedButton.get_rect()
		getInvolvedRect.move_ip( 171, 500 )
		quitRect = quitButton.get_rect()
		quitRect.move_ip( 235, 600 )
		
		screen.blit( startButton, startRect )
		screen.blit( getInvolvedButton, getInvolvedRect )
		screen.blit( creditsButton, creditsRect )
		screen.blit( quitButton, quitRect )
		
		
		# Create the mute button
		muteRect = muteButton.get_rect()
		muteRect.move_ip( 475, 825 )
		if musicOn == True:
			screen.blit( muteButton, muteRect )
		elif musicOn == False:
			screen.blit( volOnButton, muteRect )
		
		# Refresh the screen
		screen.blit( icon, (80, 20) )
		pygame.display.flip()
		
	###################
	# MAINPLAY STATES #
	###################
	
	elif state == "LevelOne":
		
		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Check to see if the character is moving laterally
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					speed[0] -= 1.5
				if event.key == pygame.K_RIGHT:
					speed[0] += 1.5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					speed[0] = 0
				if event.key == pygame.K_RIGHT:
					speed[0] = 0
		
		# Check to see if we should add an enemy
		if len( activeEnemies ) < maxEnemies and ticksSinceSpawn > minSpawnTime:
			# 10% chance of new spawn
			if random.random() < difficulty and levelCountdown > 3:
				tempX = random.randint( 0, 359 )
				tempE = enemy.get_rect()
				tempE.move_ip( tempX, 900 )
				lastPos = tempX
				activeEnemies.append( tempE )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpawn = 0
				
		# Increment the ticksSinceSpawn
		ticksSinceSpawn += 1
				
		# Check to see if we should add a species
		if len( activeOneSpecies ) < maxSpecies and ticksSinceSpeciesOneSpawn > minSpeciesOneSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempSX = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempSX > tOne and tempSX < tTwo:
					tempSX = random.randint( 0, 386 )
				tempS = sOne.get_rect()
				tempS.move_ip( tempSX, 900 )
				activeOneSpecies.append( tempS )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesOneSpawn = 0
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesOneSpawn += 1
		
		# Check to see if we should add a species
		if len( activeTwoSpecies ) < maxSpecies and ticksSinceSpeciesTwoSpawn > minSpeciesTwoSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempS2X = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempS2X > tOne and tempS2X < tTwo:
					tempS2X = random.randint( 0, 386 )
				tempS2 = sTwo.get_rect()
				tempS2.move_ip( tempS2X, 900 )
				activeTwoSpecies.append( tempS2 )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesTwoSpawn = 2000
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesTwoSpawn += 1
		
		# Move the hero
		spiderRect = spiderRect.move( speed )
		
		# Move & draw the enemies
		tempList = []
		for item in activeEnemies:
			screen.blit( enemy, item )
			tempList.append( item.move( eSpeed ) )
			activeEnemies = tempList
			
		# Move & draw the first species
		tempSList = []
		for item in activeOneSpecies:
			screen.blit( sFour, item )
			tempSList.append( item.move( sSpeed ) )
			activeOneSpecies = tempSList
			
		# Move & draw the second species
		tempS2List = []
		for item in activeTwoSpecies:
			screen.blit( sFive, item )
			tempS2List.append( item.move( sSpeed ) )
			activeTwoSpecies = tempS2List
			
		# Check to see if any enemies need to be deleted
		tempAct = []
		for item in activeEnemies:
			spiderCollisionBox = spiderRect
			enemyCollisionBox = item
			# If there is a collision
			if enemyCollisionBox.colliderect( spiderCollisionBox ):
				# Lose a random vial
				randInt = random.randint(0,1)
				if randInt == 0:
					if numOneAcq > 0:
						numOneAcq -= 1
					elif numTwoAcq > 0:
						numTwoAcq -= 1
				elif randInt == 1:
					if numTwoAcq > 0:
						numTwoAcq -= 1
					elif numOneAcq > 0:
						numOneAcq -= 1

			# If the enemy goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempAct.append( item )
		activeEnemies = tempAct
		
		# Check to see if any species need to be deleted
		tempSAct = []
		for item in activeOneSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				oneAcq = True
				numOneAcq += 1
				if numOneAcq >= 1 and numTwoAcq >= 1:
					# Check to see if the hero has enough
					pygame.mixer.music.fadeout( 2000 )
					state = "LandingScreen"
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempSAct.append( item )
		activeOneSpecies = tempSAct
		
		# Check to see if any species need to be deleted
		tempS2Act = []
		for item in activeTwoSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				twoAcq = True
				numTwoAcq += 1
				if numOneAcq >= 1 and numTwoAcq >= 1:
					# Check to see if the hero has enough
					state = "LandingScreen"
					pygame.mixer.music.fadeout( 2000 )
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempS2Act.append( item )
		activeTwoSpecies = tempS2Act
		
		# Check to see if the hero has hit the boundaries
		if spiderRect.left == 0 or spiderRect.right == ( width - 100 ):
			speed[0] = 0
		if spiderRect.left < 0 or spiderRect.right > ( width - 100 ):
			speed[0] = -speed[0]
			
		# Countdown setup
		levelCountdownTicks += 1
		# Check to see if the ticks have reached one second
		if levelCountdownTicks == 400:
			levelCountdown -= 1
			levelCountdownTicks = 0
		# Check to see if the countdown has reached 002
		if levelCountdown == 0:
			# Change the state to the landing screen
			state = "LandingScreen"
		# Create the button to blit
		countDownButton = dfont.render( str( levelCountdown ), True, (0, 0, 0 ) )
		countDownRect = countDownButton.get_rect()
		countDownRect.move_ip( 485, 20 )
		
		# Blit the countdown onto the screen
		screen.blit( countDownButton, countDownRect )
	
		if sex == "Male":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( mspider, spiderRect )
			elif randImg == 1:
				screen.blit( mspider2, spiderRect )
			elif randImg == 2:
				screen.blit( mspider3, spiderRect )
		elif sex == "Female":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( fspider, spiderRect )
			elif randImg == 1:
				screen.blit( fspider2, spiderRect )
			elif randImg == 2:
				screen.blit( fspider3, spiderRect )
				
		# Draw species one if one has been captured
		if numOneAcq > 0:
			screen.blit( sFour, ( 468, 600 ) )
			
		# Draw the number of species one captured
		if numOneAcq == 1:
			screen.blit( dot, (472, 576) )
		elif numOneAcq == 2:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
		elif numOneAcq > 2:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			
		# Draw species two if one has been captured
		if numTwoAcq > 0:
			screen.blit( sFive, (468, 800) )
		
		# Draw the number of species two captured
		if numTwoAcq == 1:
			screen.blit( dot, (472, 776) )
		elif numTwoAcq == 2:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
		elif numTwoAcq > 2:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
			screen.blit( dot, (512, 776) )
			
		# Refresh the display
		screen.blit( neededL1, ( 460, 190 ) )
		pygame.display.flip()
	
	elif state == "LevelTwo":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Check to see if the character is moving laterally
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					speed[0] -= 1.5
				if event.key == pygame.K_RIGHT:
					speed[0] += 1.5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					speed[0] = 0
				if event.key == pygame.K_RIGHT:
					speed[0] = 0
		
		# Check to see if we should add an enemy
		if len( activeEnemies ) < maxEnemies and ticksSinceSpawn > minSpawnTime:
			# 10% chance of new spawn
			if random.random() < difficulty and levelCountdown > 3:
				tempX = random.randint( 0, 359 )
				tempE = enemy.get_rect()
				tempE.move_ip( tempX, 900 )
				lastPos = tempX
				activeEnemies.append( tempE )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpawn = 0
				
		# Increment the ticksSinceSpawn
		ticksSinceSpawn += 1
				
		# Check to see if we should add a species
		if len( activeOneSpecies ) < maxSpecies and ticksSinceSpeciesOneSpawn > minSpeciesOneSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempSX = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempSX > tOne and tempSX < tTwo:
					tempSX = random.randint( 0, 386 )
				tempS = sOne.get_rect()
				tempS.move_ip( tempSX, 900 )
				activeOneSpecies.append( tempS )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesOneSpawn = 0
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesOneSpawn += 1
		
		# Check to see if we should add a species
		if len( activeTwoSpecies ) < maxSpecies and ticksSinceSpeciesTwoSpawn > minSpeciesTwoSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempS2X = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempS2X > tOne and tempS2X < tTwo:
					tempS2X = random.randint( 0, 386 )
				tempS2 = sTwo.get_rect()
				tempS2.move_ip( tempS2X, 900 )
				activeTwoSpecies.append( tempS2 )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesTwoSpawn = 2000
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesTwoSpawn += 1
		
		# Move the hero
		spiderRect = spiderRect.move( speed )
		
		# Move & draw the enemies
		tempList = []
		for item in activeEnemies:
			screen.blit( enemy, item )
			tempList.append( item.move( eSpeed ) )
			activeEnemies = tempList
			
		# Move & draw the first species
		tempSList = []
		for item in activeOneSpecies:
			screen.blit( sOne, item )
			tempSList.append( item.move( sSpeed ) )
			activeOneSpecies = tempSList
			
		# Move & draw the second species
		tempS2List = []
		for item in activeTwoSpecies:
			screen.blit( sNine, item )
			tempS2List.append( item.move( sSpeed ) )
			activeTwoSpecies = tempS2List
			
		# Check to see if any enemies need to be deleted
		tempAct = []
		for item in activeEnemies:
			spiderCollisionBox = spiderRect
			enemyCollisionBox = item
			# If there is a collision
			if enemyCollisionBox.colliderect( spiderCollisionBox ):
				# Lose a random vial
				randInt = random.randint(0,1)
				if randInt == 0:
					if numOneAcq > 0:
						numOneAcq -= 1
					elif numTwoAcq > 0:
						numTwoAcq -= 1
				elif randInt == 1:
					if numTwoAcq > 0:
						numTwoAcq -= 1
					elif numOneAcq > 0:
						numOneAcq -= 1

			# If the enemy goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempAct.append( item )
		activeEnemies = tempAct
		
		# Check to see if any species need to be deleted
		tempSAct = []
		for item in activeOneSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				oneAcq = True
				numOneAcq += 1
				if numOneAcq >= 2 and numTwoAcq >= 2:
					# Check to see if the hero has enough
					pygame.mixer.music.fadeout( 2000 )
					state = "LandingScreen"
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempSAct.append( item )
		activeOneSpecies = tempSAct
		
		# Check to see if any species need to be deleted
		tempS2Act = []
		for item in activeTwoSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				twoAcq = True
				numTwoAcq += 1
				if numOneAcq >= 2 and numTwoAcq >= 2:
					# Check to see if the hero has enough
					state = "LandingScreen"
					pygame.mixer.music.fadeout( 2000 )
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempS2Act.append( item )
		activeTwoSpecies = tempS2Act
		
		# Check to see if the hero has hit the boundaries
		if spiderRect.left == 0 or spiderRect.right == ( width - 100 ):
			speed[0] = 0
		if spiderRect.left < 0 or spiderRect.right > ( width - 100 ):
			speed[0] = -speed[0]
			
		# Countdown setup
		levelCountdownTicks += 1
		# Check to see if the ticks have reached one second
		if levelCountdownTicks == 550:
			levelCountdown -= 1
			levelCountdownTicks = 0
		# Check to see if the countdown has reached 002
		if levelCountdown == 0:
			# Change the state to the landing screen
			state = "LandingScreen"
		# Create the button to blit
		countDownButton = dfont.render( str( levelCountdown ), True, (0, 0, 0 ) )
		countDownRect = countDownButton.get_rect()
		countDownRect.move_ip( 485, 20 )
		
		# Blit the countdown onto the screen
		screen.blit( countDownButton, countDownRect )
	
		if sex == "Male":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( mspider, spiderRect )
			elif randImg == 1:
				screen.blit( mspider2, spiderRect )
			elif randImg == 2:
				screen.blit( mspider3, spiderRect )
		elif sex == "Female":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( fspider, spiderRect )
			elif randImg == 1:
				screen.blit( fspider2, spiderRect )
			elif randImg == 2:
				screen.blit( fspider3, spiderRect )
				
		# Draw species one if one has been captured
		if numOneAcq > 0:
			screen.blit( sOne, ( 468, 600 ) )
			
		# Draw the number of species one captured
		if numOneAcq == 1:
			screen.blit( dot, (472, 576) )
		elif numOneAcq == 2:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
		elif numOneAcq > 2:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			
		# Draw species two if one has been captured
		if numTwoAcq > 0:
			screen.blit( sNine, (468, 800) )
		
		# Draw the number of species two captured
		if numTwoAcq == 1:
			screen.blit( dot, (472, 776) )
		elif numTwoAcq == 2:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
		elif numTwoAcq > 2:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
			screen.blit( dot, (512, 776) )
			
		# Refresh the display
		screen.blit( neededL2, ( 460, 190 ) )
		pygame.display.flip()

	elif state == "LevelThree":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Check to see if the character is moving laterally
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					speed[0] -= 1.5
				if event.key == pygame.K_RIGHT:
					speed[0] += 1.5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					speed[0] = 0
				if event.key == pygame.K_RIGHT:
					speed[0] = 0
		
		# Check to see if we should add an enemy
		if len( activeEnemies ) < maxEnemies and ticksSinceSpawn > minSpawnTime:
			# 10% chance of new spawn
			if random.random() < difficulty and levelCountdown > 3:
				tempX = random.randint( 0, 359 )
				tempE = enemy.get_rect()
				tempE.move_ip( tempX, 900 )
				lastPos = tempX
				activeEnemies.append( tempE )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpawn = 0
				
		# Increment the ticksSinceSpawn
		ticksSinceSpawn += 1
				
		# Check to see if we should add a species
		if len( activeOneSpecies ) < maxSpecies and ticksSinceSpeciesOneSpawn > minSpeciesOneSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempSX = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempSX > tOne and tempSX < tTwo:
					tempSX = random.randint( 0, 386 )
				tempS = sOne.get_rect()
				tempS.move_ip( tempSX, 900 )
				activeOneSpecies.append( tempS )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesOneSpawn = 0
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesOneSpawn += 1
		
		# Check to see if we should add a species
		if len( activeTwoSpecies ) < maxSpecies and ticksSinceSpeciesTwoSpawn > minSpeciesTwoSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempS2X = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempS2X > tOne and tempS2X < tTwo:
					tempS2X = random.randint( 0, 386 )
				tempS2 = sTwo.get_rect()
				tempS2.move_ip( tempS2X, 900 )
				activeTwoSpecies.append( tempS2 )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesTwoSpawn = 2000
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesTwoSpawn += 1
		
		# Move the hero
		spiderRect = spiderRect.move( speed )
		
		# Move & draw the enemies
		tempList = []
		for item in activeEnemies:
			screen.blit( enemy, item )
			tempList.append( item.move( eSpeed ) )
			activeEnemies = tempList
			
		# Move & draw the first species
		tempSList = []
		for item in activeOneSpecies:
			screen.blit( sTwo, item )
			tempSList.append( item.move( sSpeed ) )
			activeOneSpecies = tempSList
			
		# Move & draw the second species
		tempS2List = []
		for item in activeTwoSpecies:
			screen.blit( sEight, item )
			tempS2List.append( item.move( sSpeed ) )
			activeTwoSpecies = tempS2List
			
		# Check to see if any enemies need to be deleted
		tempAct = []
		for item in activeEnemies:
			spiderCollisionBox = spiderRect
			enemyCollisionBox = item
			# If there is a collision
			if enemyCollisionBox.colliderect( spiderCollisionBox ):
				# Lose a random vial
				randInt = random.randint(0,1)
				if randInt == 0:
					if numOneAcq > 0:
						numOneAcq -= 1
					elif numTwoAcq > 0:
						numTwoAcq -= 1
				elif randInt == 1:
					if numTwoAcq > 0:
						numTwoAcq -= 1
					elif numOneAcq > 0:
						numOneAcq -= 1

			# If the enemy goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempAct.append( item )
		activeEnemies = tempAct
		
		# Check to see if any species need to be deleted
		tempSAct = []
		for item in activeOneSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				oneAcq = True
				numOneAcq += 1
				if numOneAcq >= 3 and numTwoAcq >= 3:
					# Check to see if the hero has enough
					pygame.mixer.music.fadeout( 2000 )
					state = "LandingScreen"
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempSAct.append( item )
		activeOneSpecies = tempSAct
		
		# Check to see if any species need to be deleted
		tempS2Act = []
		for item in activeTwoSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				twoAcq = True
				numTwoAcq += 1
				if numOneAcq >= 3 and numTwoAcq >= 3:
					# Check to see if the hero has enough
					state = "LandingScreen"
					pygame.mixer.music.fadeout( 2000 )
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempS2Act.append( item )
		activeTwoSpecies = tempS2Act
		
		# Check to see if the hero has hit the boundaries
		if spiderRect.left == 0 or spiderRect.right == ( width - 100 ):
			speed[0] = 0
		if spiderRect.left < 0 or spiderRect.right > ( width - 100 ):
			speed[0] = -speed[0]
			
		# Countdown setup
		levelCountdownTicks += 1
		# Check to see if the ticks have reached one second
		if levelCountdownTicks == 550:
			levelCountdown -= 1
			levelCountdownTicks = 0
		# Check to see if the countdown has reached 002
		if levelCountdown == 0:
			# Change the state to the landing screen
			state = "LandingScreen"
		# Create the button to blit
		countDownButton = dfont.render( str( levelCountdown ), True, (0, 0, 0 ) )
		countDownRect = countDownButton.get_rect()
		countDownRect.move_ip( 485, 20 )
		
		# Blit the countdown onto the screen
		screen.blit( countDownButton, countDownRect )
	
		if sex == "Male":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( mspider, spiderRect )
			elif randImg == 1:
				screen.blit( mspider2, spiderRect )
			elif randImg == 2:
				screen.blit( mspider3, spiderRect )
		elif sex == "Female":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( fspider, spiderRect )
			elif randImg == 1:
				screen.blit( fspider2, spiderRect )
			elif randImg == 2:
				screen.blit( fspider3, spiderRect )
				
		# Draw species one if one has been captured
		if numOneAcq > 0:
			screen.blit( sTwo, ( 468, 600 ) )
			
		# Draw the number of species one captured
		if numOneAcq == 1:
			screen.blit( dot, (472, 576) )
		elif numOneAcq == 2:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
		elif numOneAcq == 3:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
		elif numOneAcq == 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
		elif numOneAcq > 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
			screen.blit( dot, (502, 556) )
			
		# Draw species two if one has been captured
		if numTwoAcq > 0:
			screen.blit( sEight, (468, 800) )
		
		# Draw the number of species two captured
		if numTwoAcq == 1:
			screen.blit( dot, (472, 776) )
		elif numTwoAcq == 2:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
		elif numTwoAcq == 3:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
			screen.blit( dot, (512, 776) )
		elif numTwoAcq == 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
		elif numTwoAcq > 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
			screen.blit( dot, (502, 556) )
			
		# Refresh the display
		screen.blit( neededL3, ( 460, 190 ) )
		pygame.display.flip()
	
	elif state == "LevelFour":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Check to see if the character is moving laterally
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					speed[0] -= 1.5
				if event.key == pygame.K_RIGHT:
					speed[0] += 1.5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					speed[0] = 0
				if event.key == pygame.K_RIGHT:
					speed[0] = 0
		
		# Check to see if we should add an enemy
		if len( activeEnemies ) < maxEnemies and ticksSinceSpawn > minSpawnTime:
			# 10% chance of new spawn
			if random.random() < difficulty and levelCountdown > 3:
				tempX = random.randint( 0, 359 )
				tempE = enemy.get_rect()
				tempE.move_ip( tempX, 900 )
				lastPos = tempX
				activeEnemies.append( tempE )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpawn = 0
				
		# Increment the ticksSinceSpawn
		ticksSinceSpawn += 1
				
		# Check to see if we should add a species
		if len( activeOneSpecies ) < maxSpecies and ticksSinceSpeciesOneSpawn > minSpeciesOneSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempSX = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempSX > tOne and tempSX < tTwo:
					tempSX = random.randint( 0, 386 )
				tempS = sOne.get_rect()
				tempS.move_ip( tempSX, 900 )
				activeOneSpecies.append( tempS )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesOneSpawn = 0
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesOneSpawn += 1
		
		# Check to see if we should add a species
		if len( activeTwoSpecies ) < maxSpecies and ticksSinceSpeciesTwoSpawn > minSpeciesTwoSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempS2X = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempS2X > tOne and tempS2X < tTwo:
					tempS2X = random.randint( 0, 386 )
				tempS2 = sTwo.get_rect()
				tempS2.move_ip( tempS2X, 900 )
				activeTwoSpecies.append( tempS2 )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesTwoSpawn = 2000
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesTwoSpawn += 1
		
		# Move the hero
		spiderRect = spiderRect.move( speed )
		
		# Move & draw the enemies
		tempList = []
		for item in activeEnemies:
			screen.blit( enemy, item )
			tempList.append( item.move( eSpeed ) )
			activeEnemies = tempList
			
		# Move & draw the first species
		tempSList = []
		for item in activeOneSpecies:
			screen.blit( sThree, item )
			tempSList.append( item.move( sSpeed ) )
			activeOneSpecies = tempSList
			
		# Move & draw the second species
		tempS2List = []
		for item in activeTwoSpecies:
			screen.blit( sTen, item )
			tempS2List.append( item.move( sSpeed ) )
			activeTwoSpecies = tempS2List
			
		# Check to see if any enemies need to be deleted
		tempAct = []
		for item in activeEnemies:
			spiderCollisionBox = spiderRect
			enemyCollisionBox = item
			# If there is a collision
			if enemyCollisionBox.colliderect( spiderCollisionBox ):
				# Lose a random vial
				randInt = random.randint(0,1)
				if randInt == 0:
					if numOneAcq > 0:
						numOneAcq -= 1
					elif numTwoAcq > 0:
						numTwoAcq -= 1
				elif randInt == 1:
					if numTwoAcq > 0:
						numTwoAcq -= 1
					elif numOneAcq > 0:
						numOneAcq -= 1

			# If the enemy goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempAct.append( item )
		activeEnemies = tempAct
		
		# Check to see if any species need to be deleted
		tempSAct = []
		for item in activeOneSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				oneAcq = True
				numOneAcq += 1
				if numOneAcq >= 4 and numTwoAcq >= 4:
					# Check to see if the hero has enough
					pygame.mixer.music.fadeout( 2000 )
					state = "LandingScreen"
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempSAct.append( item )
		activeOneSpecies = tempSAct
		
		# Check to see if any species need to be deleted
		tempS2Act = []
		for item in activeTwoSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				twoAcq = True
				numTwoAcq += 1
				if numOneAcq >= 4 and numTwoAcq >= 4:
					# Check to see if the hero has enough
					state = "LandingScreen"
					pygame.mixer.music.fadeout( 2000 )
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempS2Act.append( item )
		activeTwoSpecies = tempS2Act
		
		# Check to see if the hero has hit the boundaries
		if spiderRect.left == 0 or spiderRect.right == ( width - 100 ):
			speed[0] = 0
		if spiderRect.left < 0 or spiderRect.right > ( width - 100 ):
			speed[0] = -speed[0]
			
		# Countdown setup
		levelCountdownTicks += 1
		# Check to see if the ticks have reached one second
		if levelCountdownTicks == 550:
			levelCountdown -= 1
			levelCountdownTicks = 0
		# Check to see if the countdown has reached 002
		if levelCountdown == 0:
			# Change the state to the landing screen
			state = "LandingScreen"
		# Create the button to blit
		countDownButton = dfont.render( str( levelCountdown ), True, (0, 0, 0 ) )
		countDownRect = countDownButton.get_rect()
		countDownRect.move_ip( 485, 20 )
		
		# Blit the countdown onto the screen
		screen.blit( countDownButton, countDownRect )
	
		if sex == "Male":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( mspider, spiderRect )
			elif randImg == 1:
				screen.blit( mspider2, spiderRect )
			elif randImg == 2:
				screen.blit( mspider3, spiderRect )
		elif sex == "Female":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( fspider, spiderRect )
			elif randImg == 1:
				screen.blit( fspider2, spiderRect )
			elif randImg == 2:
				screen.blit( fspider3, spiderRect )
				
		# Draw species one if one has been captured
		if numOneAcq > 0:
			screen.blit( sThree, ( 468, 600 ) )
			
		# Draw the number of species one captured
		if numOneAcq == 1:
			screen.blit( dot, (472, 576) )
		elif numOneAcq == 2:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
		elif numOneAcq == 3:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
		elif numOneAcq == 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
		elif numOneAcq > 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
			screen.blit( dot, (502, 556) )
			
		# Draw species two if one has been captured
		if numTwoAcq > 0:
			screen.blit( sTen, (468, 800) )
		
		# Draw the number of species two captured
		if numTwoAcq == 1:
			screen.blit( dot, (472, 776) )
		elif numTwoAcq == 2:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
		elif numTwoAcq == 3:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
			screen.blit( dot, (512, 776) )
		elif numTwoAcq == 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
		elif numTwoAcq > 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
			screen.blit( dot, (502, 556) )
			
		# Refresh the display
		screen.blit( neededL4, ( 460, 190 ) )
		pygame.display.flip()

	elif state == "LevelFive":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Check to see if the character is moving laterally
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					speed[0] -= 1.5
				if event.key == pygame.K_RIGHT:
					speed[0] += 1.5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					speed[0] = 0
				if event.key == pygame.K_RIGHT:
					speed[0] = 0
		
		# Check to see if we should add an enemy
		if len( activeEnemies ) < maxEnemies and ticksSinceSpawn > minSpawnTime:
			# 10% chance of new spawn
			if random.random() < difficulty and levelCountdown > 3:
				tempX = random.randint( 0, 359 )
				tempE = enemy.get_rect()
				tempE.move_ip( tempX, 900 )
				lastPos = tempX
				activeEnemies.append( tempE )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpawn = 0
				
		# Increment the ticksSinceSpawn
		ticksSinceSpawn += 1
				
		# Check to see if we should add a species
		if len( activeOneSpecies ) < maxSpecies and ticksSinceSpeciesOneSpawn > minSpeciesOneSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempSX = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempSX > tOne and tempSX < tTwo:
					tempSX = random.randint( 0, 386 )
				tempS = sOne.get_rect()
				tempS.move_ip( tempSX, 900 )
				activeOneSpecies.append( tempS )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesOneSpawn = 0
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesOneSpawn += 1
		
		# Check to see if we should add a species
		if len( activeTwoSpecies ) < maxSpecies and ticksSinceSpeciesTwoSpawn > minSpeciesTwoSpawnTime:
			# Spawn a species if there is still time
			if levelCountdown > 2:
				tempS2X = random.randint( 0, 386 )
				tOne = lastPos - 30
				tTwo = lastPos + 30
				while tempS2X > tOne and tempS2X < tTwo:
					tempS2X = random.randint( 0, 386 )
				tempS2 = sTwo.get_rect()
				tempS2.move_ip( tempS2X, 900 )
				activeTwoSpecies.append( tempS2 )
				
				# Reset the ticksSinceSpawn
				ticksSinceSpeciesTwoSpawn = 2000
			
		# Increment the ticksSinceSpeciesSpawn
		ticksSinceSpeciesTwoSpawn += 1
		
		# Move the hero
		spiderRect = spiderRect.move( speed )
		
		# Move & draw the enemies
		tempList = []
		for item in activeEnemies:
			screen.blit( enemy, item )
			tempList.append( item.move( eSpeed ) )
			activeEnemies = tempList
			
		# Move & draw the first species
		tempSList = []
		for item in activeOneSpecies:
			screen.blit( sSix, item )
			tempSList.append( item.move( sSpeed ) )
			activeOneSpecies = tempSList
			
		# Move & draw the second species
		tempS2List = []
		for item in activeTwoSpecies:
			screen.blit( sSeven, item )
			tempS2List.append( item.move( sSpeed ) )
			activeTwoSpecies = tempS2List
			
		# Check to see if any enemies need to be deleted
		tempAct = []
		for item in activeEnemies:
			spiderCollisionBox = spiderRect
			enemyCollisionBox = item
			# If there is a collision
			if enemyCollisionBox.colliderect( spiderCollisionBox ):
				# Lose a random vial
				randInt = random.randint(0,1)
				if randInt == 0:
					if numOneAcq > 0:
						numOneAcq -= 1
					elif numTwoAcq > 0:
						numTwoAcq -= 1
				elif randInt == 1:
					if numTwoAcq > 0:
						numTwoAcq -= 1
					elif numOneAcq > 0:
						numOneAcq -= 1

			# If the enemy goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempAct.append( item )
		activeEnemies = tempAct
		
		# Check to see if any species need to be deleted
		tempSAct = []
		for item in activeOneSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				oneAcq = True
				numOneAcq += 1
				if numOneAcq >= 5 and numTwoAcq >= 5:
					# Check to see if the hero has enough
					pygame.mixer.music.fadeout( 2000 )
					state = "LandingScreen"
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempSAct.append( item )
		activeOneSpecies = tempSAct
		
		# Check to see if any species need to be deleted
		tempS2Act = []
		for item in activeTwoSpecies:
			spiderCollisionBox = spiderRect
			speciesCollisionBox = item
			# If there is a collision
			if speciesCollisionBox.colliderect( spiderCollisionBox ):
				# Make which species were acquired
				twoAcq = True
				numTwoAcq += 1
				if numOneAcq >= 5 and numTwoAcq >= 5:
					# Check to see if the hero has enough
					state = "LandingScreen"
					pygame.mixer.music.fadeout( 2000 )
				if musicOn == True:
					testTubeSound.play()
			# If the species goes off of the screen, play the "miss" sound
			elif item.bottom < 0:
				pass
			else:
				tempS2Act.append( item )
		activeTwoSpecies = tempS2Act
		
		# Check to see if the hero has hit the boundaries
		if spiderRect.left == 0 or spiderRect.right == ( width - 100 ):
			speed[0] = 0
		if spiderRect.left < 0 or spiderRect.right > ( width - 100 ):
			speed[0] = -speed[0]
			
		# Countdown setup
		levelCountdownTicks += 1
		# Check to see if the ticks have reached one second
		if levelCountdownTicks == 550:
			levelCountdown -= 1
			levelCountdownTicks = 0
		# Check to see if the countdown has reached 002
		if levelCountdown == 0:
			# Change the state to the landing screen
			state = "LandingScreen"
		# Create the button to blit
		countDownButton = dfont.render( str( levelCountdown ), True, (0, 0, 0 ) )
		countDownRect = countDownButton.get_rect()
		countDownRect.move_ip( 485, 20 )
		
		# Blit the countdown onto the screen
		screen.blit( countDownButton, countDownRect )
	
		if sex == "Male":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( mspider, spiderRect )
			elif randImg == 1:
				screen.blit( mspider2, spiderRect )
			elif randImg == 2:
				screen.blit( mspider3, spiderRect )
		elif sex == "Female":
			randImg = random.randint(0,2)
			if randImg == 0:
				screen.blit( fspider, spiderRect )
			elif randImg == 1:
				screen.blit( fspider2, spiderRect )
			elif randImg == 2:
				screen.blit( fspider3, spiderRect )
				
		# Draw species one if one has been captured
		if numOneAcq > 0:
			screen.blit( sSix, ( 468, 600 ) )
			
		# Draw the number of species one captured
		if numOneAcq == 1:
			screen.blit( dot, (472, 576) )
		elif numOneAcq == 2:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
		elif numOneAcq == 3:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
		elif numOneAcq == 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
		elif numOneAcq > 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
			screen.blit( dot, (502, 556) )
			
		# Draw species two if one has been captured
		if numTwoAcq > 0:
			screen.blit( sSeven, (468, 800) )
		
		# Draw the number of species two captured
		if numTwoAcq == 1:
			screen.blit( dot, (472, 776) )
		elif numTwoAcq == 2:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
		elif numTwoAcq == 3:
			screen.blit( dot, (472, 776) )
			screen.blit( dot, (492, 776) )
			screen.blit( dot, (512, 776) )
		elif numTwoAcq == 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
		elif numTwoAcq > 4:
			screen.blit( dot, (472, 576) )
			screen.blit( dot, (492, 576) )
			screen.blit( dot, (512, 576) )
			screen.blit( dot, (482, 556) )
			screen.blit( dot, (502, 556) )
			
		# Refresh the display
		screen.blit( neededL5, ( 460, 190 ) )
		pygame.display.flip()
		
	#####################
	# GETINVOLVED STATE #
	#####################
	
	elif state == "GetInvolved":
		# Draw the start screen background
		screen.blit( background2, ( 0, 0 ) )
	
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "StartScreen"
				elif endSpeRect.collidepoint(pos):
					# Go to WWF site
					webbrowser.open('https://www.worldwildlife.org/initiatives/protecting-species')
				elif wwfRect.collidepoint(pos):
					# Go to WWF site
					webbrowser.open('https://www.worldwildlife.org/about')
				elif donateRect.collidepoint(pos):
					# Go to WWF site
					webbrowser.open('www.worldwildlife.org/Donate')
		
		# Create the button texts
		titleButton = dfont.render( "Get Involved!", True, (0, 0, 0 ) )
		warningButton = dfont.render( "(warning: external links)", True, (0, 0, 0 ) )
		backButton = dfont.render( "Back to Main Screen", True, (0, 0, 0 ) )
		endSpeButton = dfont.render( "What are endangered species?", True, (0, 0, 50 ) )
		wwfButton = dfont.render( "What is the WWF?", True, (0, 0, 50 ) )
		donateButton = dfont.render( "Donate", True, (0, 0, 50 ) )
		
		# Create the title heading
		titleRect = titleButton.get_rect()
		titleRect.move_ip( 205, 225 )
		screen.blit( titleButton, titleRect )
		
		# Create the warning heading
		warningRect = warningButton.get_rect()
		warningRect.move_ip( 148, 250 )
		screen.blit( warningButton, warningRect )
		
		# Create the endangered species button
		endSpeRect = endSpeButton.get_rect()
		endSpeRect.move_ip( 105, 350 )
		screen.blit( endSpeButton, endSpeRect )
		
		# Create the WWF button
		wwfRect = wwfButton.get_rect()
		wwfRect.move_ip( 175, 425)
		screen.blit( wwfButton, wwfRect )
		
		# Create the Donate button
		donateRect = donateButton.get_rect()
		donateRect.move_ip( 230, 500 )
		screen.blit( donateButton, donateRect )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Refresh the screen
		screen.blit( icon, (80, 20) )
		pygame.display.flip()
	
	#################
	# CONTEXT STATE #
	#################
	
	elif state == "Context":
	
		# Draw the start screen background
		screen.blit( background, ( 0, 0 ) )
	
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if nextRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "CharacterSelection"
		
		# Create the button texts
		backButton = dfont.render( "Back to Main Screen", True, (0, 0, 0 ) )
		nextButton = dfont.render( "Next", True, (0, 0, 0 ) )
		
		# Create the back button
		#backRect = backButton.get_rect()
		#backRect.move_ip( 10, 860 )
		#screen.blit( backButton, backRect )
		
		# Create the next button
		nextRect = nextButton.get_rect()
		nextRect.move_ip( 450, 840 )
		
		# Blit the context image onto the screen
		screen.blit( contextImage, (0,0) )
		screen.blit( nextButton, nextRect )
		#screen.blit( contextTimer, (450, -80) )
		
		# Create the countdown button to blit
		countDownButton = dfont.render( "47", True, (0, 0, 0 ) )
		countDownRect = countDownButton.get_rect()
		countDownRect.move_ip( 485, 20 )
		
		# Blit the displays onto the screen
		screen.blit( countDownButton, countDownRect )
		
		screen.blit( sFour, ( 468, 450 ) )
		screen.blit( dot, (472, 426) )
		screen.blit( dot, (492, 426) )
		#screen.blit( neededL1, ( 460, 190 ) )
		#screen.blit( contextNeeded, (350, 110) )
		
		# Refresh the screen
		#screen.blit( icon, (30, 20) )
		pygame.display.flip()

	############################
	# CHARACTERSELECTION STATE #
	############################
	
	elif state == "CharacterSelection":
	
		# Draw the start screen background
		screen.blit( background2, ( 0, 0 ) )
	
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "StartScreen"
				# If the male or female button is hit
				elif maleRect.collidepoint(pos):
					sex = "Male"
					if oneCompleted == False:
						difficulty = 0.001
						activeEnemies = []
						activeOneSpecies = []
						activeTwoSpecies = []
						minSpeciesOneSpawnTime = 5000
						minSpeciesTwoSpawnTime = 7000
						level = "One"
						eSpeed = [0,-1]
						levelCountdownTicks = 0
						levelCountdown = 60
						state = "ReadyScreen"
					else:
						state = "ReadyScreen"
				elif femaleRect.collidepoint(pos):
					sex = "Female"
					if oneCompleted == False:
						difficulty = 0.001
						activeEnemies = []
						activeSpecies = []
						minSpeciesOneSpawnTime = 5000
						minSpeciesTwoSpawnTime = 7000
						level = "One"
						eSpeed = [0,-1]
						levelCountdownTicks = 0
						levelCountdown = 60
						state = "ReadyScreen"
					else:
						state = "ReadyScreen"
		
		# Create the button texts
		backButton = dfont.render( "Back", True, (0, 0, 0 ) )
		maleButton = dfont.render( "Bruce", True, (0, 0, 0 ) )
		femaleButton = dfont.render( "Stephanie", True, (0, 0, 0 ) )
		titleButton = dfont.render( "Choose your character!", True, (0, 0, 0 ) )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Create the title label
		titleRect = titleButton.get_rect()
		titleRect.move_ip( 150, 300 )
		screen.blit( titleButton, titleRect )
		
		# Create the male button
		maleRect = maleButton.get_rect()
		maleRect.move_ip( 234, 375 )
		screen.blit( maleButton, maleRect )
		
		# Create the female button
		femaleRect = femaleButton.get_rect()
		femaleRect.move_ip( 213, 445 )
		screen.blit( femaleButton, femaleRect )
		
		# Refresh the screen
		screen.blit( icon, (80, 20) )
		pygame.display.flip()
		
	##########################
	# DIFFICULTYSCREEN STATE #
	##########################
	
	elif state == "DifficultyScreen":

		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Reset all of the global variables
		oneAcq = False
		twoAcq = False
		
		numOneAcq = 0
		numTwoAcq = 0
		
		speed = [0,0]
	
		activeOneSpecies = []
		activeTwoSpecies = []
		activeEnemies = []
	
		ticksSinceSpawn = 0
		ticksSinceSpeciesOneSpawn = 0
		ticksSinceSpeciesTwoSpawn = 0

		levelCountdownTicks = 0
		levelCountdown = 60
		
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on start button
				if oneRect.collidepoint(pos):
					# Go to the MainPlay state
					difficulty = 0.001
					activeEnemies = []
					activeOneSpecies = []
					activeTwoSpecies = []
					minSpeciesOneSpawnTime = 5000
					minSpeciesTwoSpawnTime = 7000
					level = "One"
					eSpeed = [0,-1]
					state = "ReadyScreen"
				elif twoRect.collidepoint(pos):
					# Go to the MainPlay state
					difficulty = 0.004
					activeEnemies = []
					activeOneSpecies = []
					activeTwoSpecies = []
					level = "Two"
					eSpeed = [0,-1]
					state = "ReadyScreen"
				elif threeRect.collidepoint(pos):
					# Go to the MainPlay state
					difficulty = 0.007
					activeEnemies = []
					activeOneSpecies = []
					activeTwoSpecies = []
					level = "Three"
					eSpeed = [0,-1]
					state = "ReadyScreen"
				elif fourRect.collidepoint(pos):
					# Go to the MainPlay state
					difficulty = 0.01
					activeEnemies = []
					activeOneSpecies = []
					activeTwoSpecies = []
					level = "Four"
					eSpeed = [0,-1.2]
					state = "ReadyScreen"
				elif fiveRect.collidepoint(pos):
					# Go to the MainPlay state
					difficulty = 0.014
					activeEnemies = []
					activeOneSpecies = []
					activeTwoSpecies = []
					level = "Five"
					eSpeed = [0,-1.5]
					state = "ReadyScreen"
				elif backRect.collidepoint(pos):
					# Return to the main screen
					state = "StartScreen"
					
		# Create the button texts
		diffTitle = ffont.render( "Select Level:", True, (0, 0, 0) )
		oneButton = bfont.render( "1", True, (0, 0, 0 ) )
		twoButton = bfont.render( "2", True, (0, 0, 0 ) )
		threeButton = bfont.render( "3", True, (0, 0, 0 ) )
		fourButton = bfont.render( "4", True, (0, 0, 0 ) )
		fiveButton = bfont.render( "5", True, (0, 0, 0 ) )
		backButton = dfont.render( "Back to Main Screen", True, (0, 0, 0 ) )
		
		# Create the title label
		diffRect = diffTitle.get_rect()
		diffRect.move_ip( 120, 225 )
		screen.blit( diffTitle, diffRect )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Create the number buttons
		oneRect = oneButton.get_rect()
		twoRect = twoButton.get_rect()
		threeRect = threeButton.get_rect()
		fourRect = fourButton.get_rect()
		fiveRect = fiveButton.get_rect()
		
		oneRect.move_ip( 210, 295 )
		twoRect.move_ip( 210, 355 )
		threeRect.move_ip( 210, 415 )
		fourRect.move_ip( 210, 475 )
		fiveRect.move_ip( 210, 535 )
		
		screen.blit( oneButton, oneRect )
		screen.blit( twoButton, twoRect )
		screen.blit( threeButton, threeRect )
		screen.blit( fourButton, fourRect )
		screen.blit( fiveButton, fiveRect )
		
		# Refresh the screen
		screen.blit( icon, (30, 20) )
		pygame.display.flip()

	###############
	# ABOUT STATE #
	###############
	
	elif state == "About":
		# Draw the start screen background
		screen.blit( background, ( 0, 0 ) )
	
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "StartScreen"
				elif rulesRect.collidepoint(pos):
					# Go to the rules page
					state = "Rules"
		
		# Create the button texts
		backButton = dfont.render( "Back to Main Screen", True, (0, 0, 0 ) )
		rulesButton = dfont.render( "Rules", True, (0, 0, 0 ) )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Create the rules button
		rulesRect = rulesButton.get_rect()
		rulesRect.move_ip( 10, 820 )
		screen.blit( rulesButton, rulesRect )
		
		# Refresh the screen
		screen.blit( icon, (30, 20) )
		pygame.display.flip()
	
	###############
	# RULES STATE #
	###############
	
	elif state == "Rules":
	
		# Draw the start screen background
		screen.blit( background, ( 0, 0 ) )
	
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "StartScreen"
				elif aboutRect.collidepoint(pos):
					# Go to the rules page
					state = "About"
		
		# Create the button texts
		backButton = dfont.render( "Back to Main Screen", True, (0, 0, 0 ) )
		aboutButton = dfont.render( "About", True, (0, 0, 0 ) )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Create the rules button
		aboutRect = aboutButton.get_rect()
		aboutRect.move_ip( 10, 820 )
		screen.blit( aboutButton, aboutRect )
		
		# Refresh the screen
		screen.blit( icon, (30, 20) )
		pygame.display.flip()
		
	################
	# CREDIT STATE #
	################
	
	elif state == "Credits":
	
		# Draw the start screen background
		screen.blit( background2, ( 0, 0 ) )
		
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "StartScreen"
				
		# Create the button text
		backButton = dfont.render( "Back to Main Screen", True, (0, 0, 0 ) )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Draw the credits image
		screen.blit( creditList, (50, 225) )
	
		# Refresh the screen
		screen.blit( icon, (80, 20) )
		pygame.display.flip()
	
	#####################
	# READYSCREEN STATE #
	#####################
	
	elif state == "ReadyScreen":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Reset all of the global variables
		oneAcq = False
		twoAcq = False
		
		numOneAcq = 0
		numTwoAcq = 0
		
		speed = [0,0]
	
		activeOneSpecies = []
		activeTwoSpecies = []
		activeEnemies = []
	
		ticksSinceSpawn = 0
		ticksSinceSpeciesOneSpawn = 0
		ticksSinceSpeciesTwoSpawn = 0

		levelCountdownTicks = 0
		levelCountdown = 60
		
		# Set up the spiderRect
		spiderRect = fspider.get_rect()
		spiderRect = spiderRect.inflate ( 0 , -30)
		
		spiderRect.move_ip( 160, 30 )
		if sex == "Male":
			screen.blit( mspider, spiderRect )
		elif sex == "Female":
			screen.blit( fspider, spiderRect )
		
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
				
		# Create the button texts
		threeButton = dfont.render( "3", True, (0, 0, 0 ) )
		twoButton = dfont.render( "2", True, (0, 0, 0 ) )
		oneButton = dfont.render( "1", True, (0, 0, 0 ) )
		
		# Create the buttons
		threeRect = threeButton.get_rect()
		twoRect = twoButton.get_rect()
		oneRect = oneButton.get_rect()
		
		threeRect.move_ip( 210, 400 )
		twoRect.move_ip( 210, 400 )
		oneRect.move_ip( 210, 400 )
		
		# Create the countdown button to blit
		countDownButton = dfont.render( "60", True, (0, 0, 0 ) )
		countDownRect = countDownButton.get_rect()
		countDownRect.move_ip( 485, 20 )
		
		# Blit the countdown onto the screen
		screen.blit( countDownButton, countDownRect )
		
		# Count down
		if readyTick < 600:
			screen.blit( threeButton, threeRect )
			readyTick += 1
			if musicOn == True:
				pygame.mixer.music.fadeout( 2000 )
		elif readyTick >= 600 and readyTick < 1200:
			screen.blit( twoButton, twoRect )
			readyTick += 1
		elif readyTick >= 1200 and readyTick < 1800:
			screen.blit( oneButton, oneRect )
			readyTick += 1
		elif readyTick >= 1800:
			# Change to the MainPlay
			if musicOn == True:
				pygame.mixer.music.load( "gameplay.mp3" )
				pygame.mixer.music.play( -1 )
			if level == "One":
				difficulty = 0.001
				minSpawnTime = 340
				state = "LevelOne"
			elif level == "Two":
				difficulty = 0.003
				minSpawnTime = 340
				state = "LevelTwo"
			elif level == "Three":
				difficulty = 0.006
				minSpawnTime = 340
				state = "LevelThree"
			elif level == "Four":
				difficulty = 0.009
				minSpawnTime = 340
				state = "LevelFour"
			elif level == "Five":
				difficulty = 0.012
				minSpawnTime = 280
				state = "LevelFive"
			readyTick = 0
			
			
		# Add the needed information
		if level == "One":
			screen.blit( neededL1, ( 460, 190 ) )
		elif level == "Two":
			screen.blit( neededL2, ( 460, 190 ) )
		elif level == "Three":
			screen.blit( neededL3, ( 460, 190 ) )
		elif level == "Four":
			screen.blit( neededL4, ( 460, 190 ) )
		elif level == "Five":
			screen.blit( neededL5, ( 460, 190 ) )

		# Refresh the screen
		pygame.display.flip()
	
	#######################
	# LANDINGSCREEN STATE #
	#######################
	
	elif state == "LandingScreen":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		if sex == "Male":
			screen.blit( mspider, spiderRect )
		elif sex == "Female":
			screen.blit( fspider, spiderRect )
			
		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		# Set the hero to fall
		speed[0] = 0
		speed[1] = 1
		
		# Move the hero
		spiderRect = spiderRect.move( speed )
		
		# Check to see if we should change the screen
		if spiderRect.bottom >= 1200:
			# If they were on the first level
			if level == "One":
				# If the collected the necessary species
				if numOneAcq >= 1 and numTwoAcq >= 1:
					if musicOn == True:
						pygame.mixer.music.fadeout( 2000 )
						pygame.mixer.music.load( "sanctuary.wav" )
						pygame.mixer.music.play( -1 )
					level = "Two"
					oneCompleted = True
					state = "Sanctuary"
				else:
					if musicOn == True:
						pygame.mixer.music.play( -1 )
					state = "Failure"
			elif level == "Two":
				# If the collected the necessary species
				if numOneAcq >= 2 and numTwoAcq >= 2:
					if musicOn == True:
						pygame.mixer.music.fadeout( 2000 )
						pygame.mixer.music.load( "sanctuary.wav" )
						pygame.mixer.music.play( -1 )
					level = "Three"
					twoCompleted = True
					state = "Sanctuary"
				else:
					if musicOn == True:
						pygame.mixer.music.play( -1 )
					state = "Failure"
			elif level == "Three":
				# If the collected the necessary species
				if numOneAcq >= 3 and numTwoAcq >= 3:
					if musicOn == True:
						pygame.mixer.music.fadeout( 2000 )
						pygame.mixer.music.load( "sanctuary.wav" )
						pygame.mixer.music.play( -1 )
					level = "Four"
					threeCompleted = True
					state = "Sanctuary"
				else:
					if musicOn == True:
						pygame.mixer.music.play( -1 )
					state = "Failure"
			elif level == "Four":
				# If the collected the necessary species
				if numOneAcq >= 4 and numTwoAcq >= 4:
					if musicOn == True:
						pygame.mixer.music.fadeout( 2000 )
						pygame.mixer.music.load( "sanctuary.wav" )
						pygame.mixer.music.play( -1 )
					level = "Five"
					fourCompleted = True
					state = "Sanctuary"
				else:
					if musicOn == True:
						pygame.mixer.music.play( -1 )
					state = "Failure"
			elif level == "Five":
				# If the collected the necessary species
				if numOneAcq >= 5 and numTwoAcq >= 5:
					if musicOn == True:
						pygame.mixer.music.fadeout( 2000 )
						pygame.mixer.music.load( "sanctuary.wav" )
						pygame.mixer.music.play( -1 )
					level = "Five"
					fiveCompleted = True
					state = "Sanctuary"
				else:
					if musicOn == True:
						pygame.mixer.music.play( -1 )
					state = "Failure"
		
		# Update the display
		pygame.display.flip()
	
	###################
	# SANCTUARY STATE #
	###################
	
	elif state == "Sanctuary":
	
		# Blit the maps
		if sex == "Male":
			screen.blit( sancBackMale, (0,0) )
		elif sex == "Female":
			screen.blit( sancBackFemale, (0,0) )
		
		# Check for events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					if musicOn == True:
						pygame.mixer.music.load( "theme.wav" )
						pygame.mixer.music.play( -1 )
					state = "StartScreen"
				elif continueRect.collidepoint(pos):
					# Go to the ReadyScreen
					if fiveCompleted == True:
						oneCompleted = False
						twoCompleted = False
						threeCompleted = False
						fourCompleted = False
						fiveCompleted = False
						level = "One"
						state = "GameWin"
					state = "ReadyScreen"
				elif turtleRect.collidepoint(pos):
					oneBio = True
					state = "Biography"
				elif monkRect.collidepoint(pos):
					twoBio = True
					state = "Biography"
				elif ayeRect.collidepoint(pos):
					threeBio = True
					state = "Biography"
				elif salmonRect.collidepoint(pos):
					fourBio = True
					state = "Biography"
				elif rhinoRect.collidepoint(pos):
					fiveBio = True
					state = "Biography"
				elif mammothRect.collidepoint(pos):
					sixBio = True
					state = "Biography"
				elif quaggaRect.collidepoint(pos):
					sevenBio = True
					state = "Biography"
				elif saolaRect.collidepoint(pos):
					eightBio = True
					state = "Biography"
				elif dodoRect.collidepoint(pos):
					nineBio = True
					state = "Biography"
				elif frogRect.collidepoint(pos):
					tenBio = True
					state = "Biography"
				
		# Setup the buttons
		backButton = dfont.render( "Back to Main Screen", True, (180, 180, 180 ) )
		continueButton = dfont.render( "Continue", True, (180, 180, 180 ) )
		#savedButton = dfont.render( "The animals that you have saved will appear", True, (180, 180, 180 ) )
		#saved2Button = dfont.render( "here... click on their icons to learn more!", True, (180, 180, 180 ) )
		
		# # Create the saved button
		# savedRect = savedButton.get_rect()
		# savedRect.move_ip( 10, 500 )
		# if twoCompleted != True:
			# screen.blit( savedButton, savedRect )
		
		# # Create the saved2 button
		# saved2Rect = saved2Button.get_rect()
		# saved2Rect.move_ip( 10, 530 )
		# if twoCompleted != True:
			# screen.blit( saved2Button, saved2Rect )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Create the continue button
		continueRect = continueButton.get_rect()
		continueRect.move_ip( 10, 820 )
		screen.blit( continueButton, continueRect )
		
		# Set up the animals
		# Level one
		hawksbill_turtle = Animal( "turtle.png", "hawksbillturtlebio.png", (40, 670 ) )
		if oneCompleted == True:
			hawksbill_turtle.drawAnimal()
		turtleRect = hawksbill_turtle.img.get_rect()
		turtleRect.move_ip( hawksbill_turtle.location )
		
		monk_seal = Animal( "Caribbean_Monk_Seal.png", "carribeanmonksealbio.png", (130,670) )
		if oneCompleted == True:
			monk_seal.drawAnimal()
		monkRect = monk_seal.img.get_rect()
		monkRect.move_ip( monk_seal.location )
		
		# Level two
		aye_aye = Animal( "giant_aye_aye.png", "giantayeayebio.png", (220,670) )
		if twoCompleted == True:
			aye_aye.drawAnimal()
		ayeRect = aye_aye.img.get_rect()
		ayeRect.move_ip( aye_aye.location )
		
		salmon = Animal( "pacific_salmon.png", "pacificsalmonbio.png", (310,670) )
		if twoCompleted == True: 
			salmon.drawAnimal()
		salmonRect = salmon.img.get_rect()
		salmonRect.move_ip( salmon.location )
		
		# Level three
		black_rhino = Animal( "Black_Rhino.png", "blackrhinobio.png", (400, 670) )
		if threeCompleted == True:
			black_rhino.drawAnimal()
		rhinoRect = black_rhino.img.get_rect()
		rhinoRect.move_ip( black_rhino.location )
		
		mammoth = Animal( "Wooly_Mammoth.png", "woolymammothbio.png", (40, 760) )
		if threeCompleted == True:
			mammoth.drawAnimal()
		mammothRect = mammoth.img.get_rect()
		mammothRect.move_ip( mammoth.location )
		
		# Level four
		quagga = Animal( "Quagga.png", "quaggabio.png", (130, 760) )
		if fourCompleted == True:
			quagga.drawAnimal()
		quaggaRect = quagga.img.get_rect()
		quaggaRect.move_ip( quagga.location )
		
		saola = Animal( "Saola.png", "saolabio.png", (220, 760) )
		if fourCompleted == True:
			saola.drawAnimal()
		saolaRect = saola.img.get_rect()
		saolaRect.move_ip( saola.location )
		
		# Level five
		dodo = Animal( "dodo_bird.png", "dodobio.png", (310, 760) )
		if fiveCompleted == True:
			dodo.drawAnimal()
		dodoRect = dodo.img.get_rect()
		dodoRect.move_ip( dodo.location )
		
		frog = Animal( "Golden_Frog.png", "frogbio.png", (400, 760) )
		if fiveCompleted == True:
			frog.drawAnimal()
		frogRect = frog.img.get_rect()
		frogRect.move_ip( frog.location )
		
		# Update the display
		pygame.display.flip()
	
	###################
	# BIOGRAPHY STATE #
	###################
	
	elif state == "Biography":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		screen.blit( icon, (30, 20) )
		
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					oneBio = False
					twoBio = False
					threeBio = False
					fourBio = False
					fiveBio = False
					sixBio = False
					sevenBio = False
					eightBio = False
					nineBio = False
					tenBio = False
					state = "Sanctuary"
		
		# Blit the bio images onto the screen
		if oneBio == True:
			screen.blit( bioOne, (35,300) )
		elif twoBio == True:
			screen.blit( bioTwo, (35,300) )
		elif threeBio == True:
			screen.blit( bioThree, (35,300) )
		elif fourBio == True:
			screen.blit( bioFour, (35,300) )
		elif fiveBio == True:
			screen.blit( bioFive, (35,300) )
		elif sixBio == True:
			screen.blit( bioSix, (35,300) )
		elif sevenBio == True:
			screen.blit( bioSeven, (35,300) )
		elif eightBio == True:
			screen.blit( bioEight, (35,300) )
		elif nineBio == True:
			screen.blit( bioNine, (35,300) )
		elif tenBio == True:
			screen.blit( bioTen, (35,300) )
					
		# Set up the back button
		backButton = dfont.render( "Back to the Sanctuary", True, (0, 0, 0 ) )
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
					
		# Refresh the screen
		pygame.display.flip()
	
	#################
	# GAMEWIN STATE #
	#################
	
	elif state == "GameWin":
	
		# Draw the start screen background
		screen.blit( background2, ( 0, 0 ) )
		
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if continueRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "StartScreen"
				elif learnRect.collidepoint(pos):
					# Go to the learn more webpage
					webbrowser.open('https://www.worldwildlife.org/species')
		
		# Blit the congratulations message onto the screen
		screen.blit( congrats, (0,240) )
		
		# Create the learn more button
		learnButton = dfont.render( "LEARN MORE", True, (0, 0, 50 ) )
		learnRect = learnButton.get_rect()
		learnRect.move_ip( 195, 470 )
		screen.blit( learnButton, learnRect )

		# Create the button text
		continueButton = dfont.render( "Main Screen", True, (0, 0, 0 ) )
		
		# Create the back button
		continueRect = continueButton.get_rect()
		continueRect.move_ip( 10, 860 )
		screen.blit( continueButton, continueRect )
					
		# Refresh the screen
		screen.blit( icon, (80, 20) )
		pygame.display.flip()
	
	#################
	# FAILURE STATE #
	#################
	
	elif state == "Failure":
	
		# Redraw the background
		screen.blit( background, (0,0) )
		
		# Check for events
		for event in pygame.event.get():
			# If the user quits
			if event.type == pygame.QUIT:
				sys.exit()
			# If there was a mouse click
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# Get the mouse position
				pos = pygame.mouse.get_pos()
				# Click on back button
				if backRect.collidepoint(pos):
					# Go to the StartScreen state
					state = "StartScreen"
				elif replayRect.collidepoint(pos):
					state = "ReadyScreen"
					# speed = [0,0]
					# difficulty = 0.001
					# activeEnemies = []
					# activeOneSpecies = []
					# activeTwoSpecies = []
					# minSpeciesOneSpawnTime = 5000
					# minSpeciesTwoSpawnTime = 7000
					# level = "One"
					# eSpeed = [0,-1]
					# levelCountdownTicks = 0
					# levelCountdown = 60
					# state = "ReadyScreen"
				
		# Create the button texts
		backButton = dfont.render( "Return to Start", True, (0, 0, 0 ) )
		replayButton = dfont.render( "Retry", True, (0, 0, 0 ) )
		
		# Create the back button
		backRect = backButton.get_rect()
		backRect.move_ip( 10, 860 )
		screen.blit( backButton, backRect )
		
		# Create the replay button
		replayRect = replayButton.get_rect()
		replayRect.move_ip( 350, 860 )
		screen.blit( replayButton, replayRect )
		
		# Display the failure message
		screen.blit( failureImage, ( 0, 200 ) )
		
		# Refresh the screen
		pygame.display.flip()