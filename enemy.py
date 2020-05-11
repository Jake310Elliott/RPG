import pygame
from entity import Entity
from weapon import Weapon
from toolbarHandler import ToolbarHandler
from box import Box
from pygame.rect import Rect

# colors 
GREEN = (97,173,64)#(20, 255, 140)
DARK_GREEN = (31,92,0)
#GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (200, 0, 100)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
GREY = (136,151,165)

class Enemy(Entity):
	def __init__(self, toolbar, type, name, health = 10, X = 125, Y = 125, spawnPosition = 'forward', cellSize = 100):
		defaultSprite = "Enemy Sprites/Slimes/Enemy_Slime_Blue.png"
		super().__init__(defaultSprite, defaultSprite, defaultSprite, 
		defaultSprite, cellSize, X, Y, spawnPosition)
		
		
		self.SLIME = 'slime'
		self.NONE = 'none'
		self.validTypes = [self.SLIME]
		
		self.name = name
		
		self.toolbar = toolbar
		self.type = type
		self.health = health
		self.maxHealth = health
		
		self.paintSprite(self.type)

		# animation lists
		self.dyingAnimation = [
		"Enemy Sprites/Slimes/Slime_Blue_Dying1.png",
		"Enemy Sprites/Slimes/Slime_Blue_Dying2.png",
		"Enemy Sprites/Slimes/Slime_Blue_Dying3.png",
		"Enemy Sprites/Slimes/Slime_Blue_Bubbly.png",
		"Enemy Sprites/Slimes/Slime_Blue_Bubble.png",
		"Enemy Sprites/Slimes/Squished_Slime_Blue.png"]
		
		
		# animation flags
		self.dying = False
		self.attacking = False

		
	def paintSprite(self, type):

		# set paint prefix
		self.type = type
		
		if self.type == self.SLIME:
			self.Left_Sprite = "Enemy Sprites/Slimes/Enemy_Slime_Blue.png"
			self.Right_Sprite = "Enemy Sprites/Slimes/Enemy_Slime_Blue.png"
			self.Forward_Sprite = "Enemy Sprites/Slimes/Enemy_Slime_Blue.png"
			self.Back_Sprite = "Enemy Sprites/Slimes/Enemy_Slime_Blue.png"
			
			self.posX = 0
			self.posY = 35
		
		if self.type == self.NONE:
			self.setXY(-100,-100)
			
	def __str__(self):
		return str(self.rect)
		
	def takeDamage(self, weapon):
		'''
		called whenever this enemy is attacked by a weapon
		'''
		
		self.health -= weapon.damage
	
	def dead(self):
		'''
		Returns true when this enemy is dead
		'''
		return self.health <=0
	
	def die(self):
		'''
		Initiate dying animation
		'''
		
		self.dying == True
		
	
	def checkFlags(self):
		'''
		use this to keep flag checking out of the main loop
		'''
		
	
	def animatorDying(self, i):
		'''
		This plays the slime dying animation
		'''

		#print(self.posX, self.posY)
		#print("dying animation")
		# For the first second
		if i // 4 == 0:
			pass
		elif i // 22 == 0:
			# cycle through the first three images
			self.setPosXY(0,0)
			self.image = pygame.image.load(self.dyingAnimation[i % 3]).convert_alpha()            # This plays the exploding animation
		elif i // 25 == 0:
			self.setPosXY(0,50)
			self.image = pygame.image.load(self.dyingAnimation[3]).convert_alpha()
		elif i // 27 == 0:
			self.image = pygame.image.load(self.dyingAnimation[4]).convert_alpha()
		elif i // 37 == 0:
			self.image = pygame.image.load(self.dyingAnimation[5]).convert_alpha()
		else:
			self.kill()
			self.dying = False
			return 0
		
		
		return i+1
		
	
	def updateHealthBar(self):
		# rect(left,top,width, height)
		
		# Define the health bar
		if 80 * (self.health / self.maxHealth) >= 0:
			length = 80 * (self.health / self.maxHealth)
		else:
			length = 0
		self.healthBar = Rect(10,10,length,10)
		self.healthOutline = Rect(10,10,80,10)
		print(self.health / self.maxHealth)
		# draw health bar on cell
		pygame.draw.rect(self.cellSurface, RED, self.healthBar)
		pygame.draw.rect(self.cellSurface, RED, self.healthOutline, 1)
		
		
		
	def update(self, surface = None):
		'''
		this method is called every time the draw function is called
		'''
		if surface != None:
			# Draw stuff
			pass
		self.updateHealthBar()
		
		
		
		
		
		
		
		
		
		
		