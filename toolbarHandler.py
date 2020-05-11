import pygame
from weapon import Weapon
from collections import namedtuple
# colors 
GREEN = (97,173,64)#(20, 255, 140)
DARK_GREEN = (31,92,0)
#GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (167, 102, 242)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
GREY = (136,151,165)


class ToolbarHandler():
	def __init__(self, length, position, cellSize):
		
		# size of box cell in pixels
		self.cellSize = cellSize
		# Length in cells
		self.width = length * self.cellSize
		self.height = self.cellSize
		self.pos = position * cellSize
		
		
		
		# null value for weapon slots
		self.NONE = pygame.Surface([0, 0])
		
		# create toolbar surface
		self.toolbar = pygame.Surface([self.width, self.height])
		self.toolbar.fill(WHITE)
		self.toolbar.set_colorkey(WHITE)
 
		# Draw Toolbar
		self.toolbarBackground =[0, 0, self.width, self.height]
		
		# Define weapon boxes
		# outer
		self.outerLeft = [15, 15, self.cellSize - 30, self.height - 30]
		self. outerRight = [self.cellSize + 15, 15, self.cellSize - 30, self.height - 30]
		# inner
		self. innerLeft = [20, 20, self.cellSize - 40, self.height - 40]
		self.innerRight = [self.cellSize + 20, 20, self.cellSize - 40, self.height - 40]
		
		# Seletion box
		self.selectionBox = [17, 17, self.cellSize - 34, self.height - 34]
		
		# weapon toggle
		self.mainBox = True # Left box is main
		
		
		
		
		
		
		
		# Weapon Displays
		self.mainWeapon = self.NONE
		self.sideWeapon = self.NONE
		
		
		
		
		
		
	def draw(self,surface):
		'''
		Draw this toolbar on the bottom of the game plane
		'''
		self.toolbar.fill(WHITE) # Allows for changes in pos to be seen (without this, the previous blit of the toolbar and cell surface would remain visable)
		# Draw background
		pygame.draw.rect(self.toolbar, PURPLE, self.toolbarBackground)
		# Draw outer
		pygame.draw.rect(self.toolbar, GREY, self.outerLeft, 3)
		pygame.draw.rect(self.toolbar, GREY, self. outerRight, 3)
		# Draw Inner
		pygame.draw.rect(self.toolbar, GREY, self. innerLeft, 3)
		pygame.draw.rect(self.toolbar, GREY, self.innerRight, 3)
		# Draw selectionBox
		pygame.draw.rect(self.toolbar, YELLOW, self.selectionBox, 3)
		# draw weapon images
		self.toolbar.blit(self.mainWeapon,(21,21))
		self.toolbar.blit(self.sideWeapon,(self.cellSize + 21,21))

		
		
		# Draw Toolbar
		surface.blit(self.toolbar, (0, self.pos)) # Draw this sprite's surface on the screen's display-surface
	
	def toggleWeapon(self):
		'''
		Visually changes active weapon display. Functionality must be done in player object
		'''
		self.mainBox = not self.mainBox
		if self.mainBox:
			self.selectionBox = [17, 17, self.cellSize - 34, self.height - 34]
		else:
			self.selectionBox = [self.cellSize + 17, 17, self.cellSize - 34, self.height - 34]
	
	def setMainWeapon(self, weapon):
		'''
		Set image to be shown in the main weapon slot
		'''
		self.mainWeapon = weapon.image
	
	def setSideWeapon(self, weapon):
		'''
		Set image to be shown in the main weapon slot
		'''
		self.sideWeapon = weapon.image
	
	def getWeaponAvailability(self):
		'''
		Return named tuple of booleans: True for available, False for taken
		'''
		if self.mainWeapon != self.NONE:
			slot1 = False
		else:
			slot1 = True
		if self.sideWeapon != self.NONE:
			slot2 = False
		else:
			slot2 = True
		availability = namedtuple("availability", ["main","side"])
		
		return availability(slot1,slot2)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		