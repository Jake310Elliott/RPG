import pygame

class Item():
	def __init__(self):
		self.weapon = namedtuple('weapon',['name','damage'])
		# define returnable weapon tuple
		self.statsGroup = namedtuple('weapon', ['name', 'damage'])
		self.stats = self.statsGroup('Sword', 5)