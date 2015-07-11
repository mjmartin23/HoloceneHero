# Charles Macaulay
# January 2015
#
# Sanctuary gamestate
#
#


####################### Setup #########################
# useful imports
import sys
import random
import math

# import pygame
import pygame


# initialize pygame
pygame.init()

# initialize the fonts
try:
    pygame.font.init()
except:
    print "Fonts unavailable"
    sys.exit()

# create a game clock
gameClock = pygame.time.Clock()


# create a screen (width, height)
screen = pygame.display.set_mode( (550 , 900) )

################## Animal Base Class ###################

class Animal(object):
    def __init__(self, img, bio, location ):
        self.img = pygame.image.load( img )
        self.bio = pygame.image.load( bio )
        self.location = location

    def drawAnimal(self):
		img_rect = self.img.get_rect()
		img_rect.move_ip( self.location )
		screen.blit(self.img, img_rect)

    def drawBio(self):
        img_rect_bio = pygame.Rect( (self.location), self.bio.get_rect().width, self.bio.get_rect().height )
        screen.blit(self.bio, img_rect_bio)



################## Content ###########################

#### The animal thumbnails (which ones get drawn
# depends on performance on levels). They are stored in a list.


# black_rhino = Animal( "Black_Rhino.png", "blackrhinobio.png", (0,0) )
# caribbean_monk = Animal( "Caribbean_Monk_Seal.png", "carribeanmonksealbio.png", (0,1) )
# dodo_bird = Animal( "dodo_bird.png", "dodobio.png", (0,2) )
# giant_aye = Animal( "giant_aye_aye.png", "giantayeayebio.png", (0,3) )
# gold_frog = Animal( "Golden_Frog.png", "goldenfrogbio.png", (0,4) )
# pac_salm = Animal ( "pacific_salmon.png", "pacificsalmonbio.png", (1,0))
# quagga = Animal( "Quagga.png", "quaggabio.png", (1,1) )
# saola = Animal( "Saola.png", "saolabio.png", (1,2) )
# turtle = Animal( "turtle.png", "hawsbillturtlebio.png", (1,3))
# wool_mammoth = Animal( "Wooly_Mammoth.png", "woolymammothbio.png", (1, 4) )

back_sound = pygame.mixer.Sound( "sanctuary.wav" )




