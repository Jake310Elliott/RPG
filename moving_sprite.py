import pygame
from pygame.rect import Rect
#import importlib
#importlib.reload(pygame.sprite)
GREEN = (97,173,64)#(20, 255, 140)
DARK_GREEN = (31,92,0)
#GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
GREY = (136,151,165)
class MovingSprite(pygame.sprite.Sprite):

	def __init__(self, LeftSprite, RightSprite, ForwardSprite, BackSprite, cellSize = 100, X = 125, Y = 125, spawnPosition = 'forward'):
		# TODO: put box number definition in the move functions
		'''
		A subclass of sprite which contains movement functions that can be easily called to move around within a grid
		'''
		# Call the parent class (Sprite) constructor
		super().__init__()
        
		self.FORWARD = 'forward'
		self.BACKWARD = 'backward'
		self.LEFT = 'left'
		self.RIGHT = 'right'

		# position of sprite box on grid
		self.x = X
		self.y = Y
		
		# position of sprite in box
		self.posX = 35
		self.posY = 35
		
		# the length of one side of a box on the playing grid
		self.cellSize = cellSize
		
		
		# sprite animation images
		self.Left_Sprite = LeftSprite
		self.Right_Sprite = RightSprite
		self.Forward_Sprite = ForwardSprite
		self.Back_Sprite = BackSprite
		
		# health bar
		self.healthBar = Rect(0,0,0,0)
		self.healthOutline = Rect(0,0,0,0)
		
		
		# Default spawn position
		self.position = spawnPosition
		
		# use spawn position
		if spawnPosition == self.FORWARD:
			self.image = pygame.image.load(self.Forward_Sprite).convert_alpha()
		if spawnPosition == self.BACKWARD:
			self.image = pygame.image.load(self.Back_Sprite).convert_alpha()
		if spawnPosition == self.LEFT:
			self.image = pygame.image.load(self.Left_Sprite).convert_alpha()
		if spawnPosition == self.RIGHT:
			self.image = pygame.image.load(self.Right_Sprite).convert_alpha()
			
			
			
			
		# variables relative to the moving sprite
		# This variable is 1 when the front of the moving sprite is to the right
		self.frontX = 0
		# This variable is 1 when the front of the moving sprite is down
		self.frontY = -1
		# This variable is 1 when the box to the right of the moving sprite is to the right
		self.rightX = 1
		# This variable is 1 when the box to the right of the moving sprite is down
		self.rightY = 0
	
	
		self.updateSurroundingBoxes()
		
		
		
		# so that adjacent rects do not register as colliding
		self.hitBoxOffset = 10

		# hitbox rectangle
		self.rect = Rect(self.x + self.hitBoxOffset, self.y + self.hitBoxOffset, 0.8 * self.cellSize, 0.8 * self.cellSize)
		print("initial set: ", self.rect)
		
		# visual representation of hit box
		self.hitBox = Rect(0, 0, cellSize, cellSize)

		
		# Create surface for the rect
		self.cellSurface = pygame.Surface([cellSize, cellSize])
		self.cellSurface.set_colorkey(WHITE)
		self.cellSurface.fill(WHITE)
		
		# draw hit box around moving sprite (represents the collision rect box)
		pygame.draw.rect(self.cellSurface, RED, self.hitBox, 1 )



	def repaintSprite(self, forward, backward, left, right):
		'''
		Changes sprite animation images
		'''
		self.Forward_Sprite = forward
		self.Back_Sprite = backward
		self.Left_Sprite = left
		self.Right_Sprite = right
		
	# move around board
	def moveRight(self):
		self.image = pygame.image.load(self.Right_Sprite).convert_alpha()
		self.switchPosition(self.RIGHT)
 
	def moveLeft(self):
		self.image = pygame.image.load(self.Left_Sprite).convert_alpha()
		self.switchPosition(self.LEFT)
	
	def moveForward(self):
		self.image = pygame.image.load(self.Forward_Sprite).convert_alpha()
		self.switchPosition(self.FORWARD)
 
	def moveBackward(self):
		self.image = pygame.image.load(self.Back_Sprite).convert_alpha()
		self.switchPosition(self.BACKWARD)

	# Turn in place
	def turnRight(self):
		self.image = pygame.image.load(self.Right_Sprite).convert_alpha()
		self.setPosition(self.RIGHT)
 
	def turnLeft(self):
		self.image = pygame.image.load(self.Left_Sprite).convert_alpha()
		self.setPosition(self.LEFT)
	
	def turnForward(self):
		self.image = pygame.image.load(self.Forward_Sprite).convert_alpha()
		self.setPosition(self.FORWARD)
 
	def turnBackward(self):
		self.image = pygame.image.load(self.Back_Sprite).convert_alpha()
		self.setPosition(self.BACKWARD)		
		
		
		
		
		
		
		
		
		
		
		
		
		
	def draw(self, surface): #draw to the surface/screen
		'''
		This method is called every frame
		Used to update things	
		'''
		self.cellSurface.fill(WHITE)
		self.cellSurface.set_colorkey(WHITE)
		
		self.update(surface)
		
				
				
		
		#self.cellSurface.fill(WHITE)
		surface.blit(self.cellSurface, (self.x, self.y))       # Print the cell surface (which contains the red box outlining the box)
		surface.blit(self.image, ((self.posX + self.x), (self.posY + self.y)))        # print the image in the cell and position described by the coordinates	
		
		# draw collision rect (the one that represents the collision rect)
		pygame.draw.rect(surface, BLUE, self.rect ,1)
		
		
		# Attack boxes
		
		#pygame.draw.rect(surface, RED, self.frontRect, 3)
		#pygame.draw.rect(surface, RED, self.backRect, 3)
		#pygame.draw.rect(surface, RED, self.rightRect, 3)
		#pygame.draw.rect(surface, RED, self.leftRect, 3)
		
		#pygame.draw.rect(surface, RED, self.frontRightRect, 3)
		#pygame.draw.rect(surface, RED, self.backRightRect, 3)
		#pygame.draw.rect(surface, RED, self.frontLeftRect, 3)
		#pygame.draw.rect(surface, RED, self.backLeftRect, 3)



		
	def adjustPosXY(self,xmove,ymove):
		'''
		adds adjustment to sprite location in it's box
		'''
		self.posY += ymove
		self.posX += xmove
		
	def setPosXY(self,xmove,ymove):
		'''
		sets sprite location in it's box
		'''
		self.posY = ymove
		self.posX = xmove
		
		# update collision rect
		self.rect = Rect(self.x + self.hitBoxOffset, self.y + self.hitBoxOffset, 0.8 * self.cellSize, 0.8 * self.cellSize)
		
	def adjustXY(self,xmove,ymove):
		'''
		adds adjustment to sprite position on field
		'''
		self.y += ymove
		self.x += xmove
		
	def setXY(self,xmove,ymove):
		'''
		sets sprite position on field
		'''
		self.y = ymove
		self.x = xmove
		
		# update collision rect
		self.rect = Rect(self.x + self.hitBoxOffset, self.y + self.hitBoxOffset, 0.8 * self.cellSize, 0.8 * self.cellSize)
	
	def switchPosition(self, newPosition):
		'''
		Move to another cell and change sprite image accordingly
		'''
		RIGHT = self.RIGHT
		LEFT = self.LEFT
		FORWARD = self.FORWARD
		BACKWARD = self.BACKWARD
		cellSize = self.cellSize
		

		# Determine the new position of the moving sprite
		if newPosition == FORWARD:
			self.posX = 35
			self.posY = 35
			self.y -= 1 * cellSize
		if newPosition == BACKWARD:
			self.posX = 35
			self.posY = -15
			self.y += 1 * cellSize
		if newPosition == LEFT:
			self.posX = 60
			self.posY = 20
			self.x -= 1 * cellSize
		if newPosition == RIGHT:
			self.posX = 10
			self.posY = 20
			self.x += 1 * cellSize
		
		self.position = newPosition
		
		self.updateSurroundingBoxes()
		
		# update collision rect
		self.rect = Rect(self.x + self.hitBoxOffset, self.y + self.hitBoxOffset, 0.8 * cellSize, 0.8 * cellSize)

	def setPosition(self, newPosition):
		'''
		Change position of sprite without moving cells
		'''
		RIGHT = self.RIGHT
		LEFT = self.LEFT
		FORWARD = self.FORWARD
		BACKWARD = self.BACKWARD
		cellSize = self.cellSize
		

		# Determine the new position of the moving sprite
		if newPosition == FORWARD:
			self.posX = 35
			self.posY = 35
		if newPosition == BACKWARD:
			self.posX = 35
			self.posY = -15
		if newPosition == LEFT:
			self.posX = 60
			self.posY = 20
		if newPosition == RIGHT:
			self.posX = 10
			self.posY = 20
		
		self.position = newPosition
		
		self.updateSurroundingBoxes()
		
		
		# update collision rect
		#self.rect = Rect(self.x + self.hitBoxOffset, self.y + self.hitBoxOffset, 0.8 * cellSize, 0.8 * cellSize)
		
	def updateSurroundingBoxes(self):
	
		RIGHT = self.RIGHT
		LEFT = self.LEFT
		FORWARD = self.FORWARD
		BACKWARD = self.BACKWARD
		
		if self.position == FORWARD:
			self.frontX,self.frontY = 0,-1
			self.rightX,self.rightY = 1, 0
		if self.position == BACKWARD:
			self.frontX,self.frontY = 0,1
			self.rightX,self.rightY = -1, 0
		if self.position == LEFT:
			self.frontX,self.frontY = -1,0
			self.rightX,self.rightY = 0, -1
		if self.position == RIGHT:
			self.frontX,self.frontY = 1,0
			self.rightX,self.rightY = 0, 1
			
		self.frontRect = Rect(self.x + self.frontX * self.cellSize     , self.y + self.frontY * self.cellSize     , self.cellSize, self.cellSize)
		self.backRect  = Rect(self.x + self.frontX * self.cellSize * -1, self.y + self.frontY * self.cellSize * -1, self.cellSize, self.cellSize)
		self.rightRect = Rect(self.x + self.rightX * self.cellSize     , self.y + self.rightY * self.cellSize     , self.cellSize, self.cellSize)
		self.leftRect  = Rect(self.x + self.rightX * self.cellSize * -1, self.y + self.rightY * self.cellSize * -1, self.cellSize, self.cellSize)
		
		
		self.frontRightRect = Rect(self.x + (self.rightX+ self.frontX) * self.cellSize,
		self.y + (self.frontY + self.rightY) * self.cellSize,
		self.cellSize, self.cellSize)
		
		self.backRightRect  = Rect(self.x + (self.rightX+ self.frontX) * self.cellSize * (-1 + 2 * abs(self.frontY)),
		self.y + (self.frontY + self.rightY) * self.cellSize * (-1 + 2 * abs(self.rightY)),
		self.cellSize, self.cellSize)
		
		self.frontLeftRect  = Rect(self.x + (self.rightX + self.frontX) * self.cellSize * (-1 + 2 * abs(self.rightY)),
		self.y + (self.frontY + self.rightY) * self.cellSize * (-1 + 2 * abs(self.frontY)),
		self.cellSize, self.cellSize)
		
		self.backLeftRect   = Rect(self.x + (self.rightX+ self.frontX) * self.cellSize * -1,
		self.y + (self.frontY + self.rightY) * self.cellSize * -1,
		self.cellSize, self.cellSize)
		

	def update(self, surface = None):
		'''
		This function should be overloaded by a child class
		'''
			
			
			
			
			
			
			
			
			
		

 