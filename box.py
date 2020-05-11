import pygame
from pygame.rect import Rect

class Box():
	def __init__(self, rect):
		self.rect = Rect(rect)
	
	
	def __str__(self):
		return str(self.rect)
	