import pygame
from moving_sprite import MovingSprite

WHITE = (255, 255, 255)
 
class Entity(MovingSprite):
	'''
	A moving, breathing thing in the game
	'''
	
	
	def __init__(self, LeftSprite, RightSprite, ForwardSprite, BackSprite, cellSize, X = 125, Y = 125, spawnPosition = 'forward'):
		super().__init__(LeftSprite, RightSprite, ForwardSprite, BackSprite, cellSize, X, Y, spawnPosition)
	
