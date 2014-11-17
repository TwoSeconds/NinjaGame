#1/usr/bin/python3

########################################################################
# File Name: NinjaGame.py
# Authors: Nicole Lewey and Jacob Lundgren
# Date: 12/08/2014
# Class: CS360 - Open Source
# Assignment: Ninja Game - Create Open Source Project
# Purpose: Main for the Ninja Game
########################################################################

import pygame
from Wall import *
from WallGroup import *
from pygame.locals import *

SCREEN_LENGTH = 900
SCREEN_WIDTH = 600

def main():
	pygame.init()
	screen = pygame.display.set_mode ((SCREEN_LENGTH, SCREEN_WIDTH))	
	walls = WallGroup(screen)
	walls.draw (screen)
	pygame.display.update()
	
	while True:
		if pygame.event.poll().type is QUIT:
			break

# invoke main()
if __name__=="__main__" :
	main()
