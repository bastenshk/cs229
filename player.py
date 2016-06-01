import pygame
from pygame.locals import *
from snake import Snake
import random

def play():
	game = Snake()
	# game.player_play()
	game.AI_control()
play()