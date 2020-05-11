import pygame
#from collections import namedtuple
from pygame.rect import Rect

# colors 
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

class Weapon(pygame.sprite.Sprite):

	def __init__(self, name, damage, type, X = 0 , Y = 0, cellSize = 100):
	
		super().__init__()
		
		
		# Define attributes
		self.damage = damage
		self.name = name
		self.type = type

		# Weapon types
		self.SWORD = 'sword'
		self.KNIFE = 'knife'
		self.STAFF = 'staff'
		self.BOW = 'bow'
		self.FIST = 'fist'
		self.NONE = 'none'
		
		# acceptable types
		self.validTypes = [self.FIST,self.SWORD, self.KNIFE,self.STAFF,self.BOW, self.NONE]
		
				
		# check for valid weapon type (might not work)
		self.checkForValidType(self.type)
		
		
		# Default picture
		self.picture = 'Sword_Images/Sword.PNG'
		
		# paint default image for weapon to avoid errors
		self.paintWeapon(self.type)
		

		
		# position on grid
		self.x = X
		self.y = Y
		
		# position in box
		self.posX = 40
		self.posY = 40
		
		# size of each cell on the game plane
		self.cellSize = cellSize
		
		
		
		# Default final position of animation is with sword
		self.grabWeaponAnimation_Left = ['Plain_Sprite_Images/Clothed_Sprite_Grabbing_Weapon_Left.PNG','Plain_Sprite_Images/Left_Sprite.PNG','Plain_Sprite_Images/Clothed_Sprite_Presenting_Weapon.PNG','Sword_Images/Sprite_With_Sword_Left.PNG','left']
		self.grabWeaponAnimation_Right = ['Plain_Sprite_Images/Clothed_Sprite_Grabbing_Weapon_Right.PNG','Plain_Sprite_Images/Right_Sprite.PNG','Plain_Sprite_Images/Clothed_Sprite_Presenting_Weapon.PNG','Sword_Images/Sprite_With_Sword_Right.PNG','right']
		self.grabWeaponAnimation_Forward = ['Plain_Sprite_Images/Clothed_Sprite_Grabbing_Weapon_Forward.PNG','Plain_Sprite_Images/Forward_Sprite.PNG','Plain_Sprite_Images/Clothed_Sprite_Presenting_Weapon.PNG','Sword_Images/Sprite_With_Sword_Forward.PNG','forward']
		self.grabWeaponAnimation_Back = ['Plain_Sprite_Images/Clothed_Sprite_Grabbing_Weapon_Back.PNG','Plain_Sprite_Images/Back_Sprite.PNG','Plain_Sprite_Images/Clothed_Sprite_Presenting_Weapon.PNG','Sword_Images/Sprite_With_Sword_Back.PNG','back']		

		self.leftAttack = []
		self.rightAttack = []
		self.forwardAttack = []
		self.backAttack = []

		# paint default image for weapon to avoid errors
		self.paintWeapon(self.type)


		
		# Create surface for the rect (the size of a box)
		self.cellSurface = pygame.Surface([cellSize, cellSize*2])   # make the surface a 1x2 tall box so that animations can lower the item below the cell border
		self.cellSurface.set_colorkey(WHITE)
		self.cellSurface.fill(WHITE)
		
		# create hit box for the box (because the item will interact with the player's hit box)
		hitBoxOffset = 10
		self.rect = Rect(self.x + .1 * cellSize,self.y + 0.1 * cellSize ,0.8 * cellSize,0.8 * cellSize) # This will be changed to be used for collision checking
		self.hitBox = Rect(0,0,cellSize,cellSize) # This will be the visual representation of the hitbox
		self.hitWidth = self.rect[2]
		self.hitHeight = self.rect[3]
		
		# add weapon image to surface
		self.cellSurface.blit(self.image,(0 + self.posX,0 + self.posY)) # draw image on the box in the position determined by pos
		pygame.draw.rect(self.cellSurface, RED, self.hitBox,1)
		
		
		
		
		
		
	# draw the image on the screen
	
	# TODO: fix this to draw image directly on surface and have cell surface be the surface containing the red / blue outline
	
	def draw(self, surface): #draw to the surface/screen
		self.cellSurface.fill(WHITE) # Allows for changes in pos to be seen (without this, the previous blit of the image and cell surface would remain visable)
		self.cellSurface.blit(self.image,(0 + self.posX,0 + self.posY)) # draw image on the box in the position determined by pos
		pygame.draw.rect(self.cellSurface, RED, self.hitBox,1) # draw red outline for this sprite's cell
		surface.blit(self.cellSurface, (self.x, self.y)) # Draw this sprite's surface on the screen's display-surface
	
	def getStats(self):
		'''
		Returns a named tuple of desired stats
		'''
		return (self.stats.name,self.stats.damage)
	# TODO add input functionality to either choose the stats to recieve or between basic and all stats (after more stats are introduced)
		return statsGroup(self.name, self.damage)
		
		
	def getWeaponSprites(self):
		'''
		return all player sprite images for holding the weapon
		'''
		return (forwardSprite, backwardSprite,leftSprite, rightSprite)
	
	def paintWeapon(self, weaponType):
		'''
		weapon types supported: sword, fists
		Sets walking animation images, grabbing 
		'''
		if weaponType == self.SWORD:

			
			self.Forward_Sprite = 'Sword_Images/Sprite_With_Sword_Forward.PNG'
			self.Back_Sprite = 'Sword_Images/Sprite_With_Sword_Back.PNG'
			self.Left_Sprite = 'Sword_Images/Sprite_With_Sword_Left.PNG'
			self.Right_Sprite = 'Sword_Images/Sprite_With_Sword_Right.PNG'
			
			self.leftAttack = ["Sword_Images/Player_Sword_Attack_Left1.png",
			"Sword_Images/Player_Sword_Attack_Left2.png",
			"Sword_Images/Player_Sword_Attack_Left3.png",
			"Sword_Images/Player_Sword_Attack_Left4.png",
			"Sword_Images/Player_Sword_Attack_Left5.png",
			"Plain_Sprite_Images/Left_Sprite.PNG"]
			self.rightAttack = ["Sword_Images/Player_Sword_Attack_Right1.png",
			"Sword_Images/Player_Sword_Attack_Right2.png",
			"Sword_Images/Player_Sword_Attack_Right3.png",
			"Sword_Images/Player_Sword_Attack_Right4.png",
			"Sword_Images/Player_Sword_Attack_Right5.png",
			"Plain_Sprite_Images/Right_Sprite.PNG"]
			self.forwardAttack = ["Sword_Images/Player_Sword_Attack_Forward1.png",
			"Sword_Images/Player_Sword_Attack_Forward2.png",
			"Sword_Images/Player_Sword_Attack_Forward3.png",
			"Sword_Images/Player_Sword_Attack_Forward4.png",
			"Sword_Images/Player_Sword_Attack_Forward5.png",
			"Plain_Sprite_Images/Forward_Sprite.PNG"]
			self.backAttack = ["Sword_Images/Player_Sword_Attack_back1.png",
			"Sword_Images/Player_Sword_Attack_back2.png",
			"Sword_Images/Player_Sword_Attack_back3.png",
			"Sword_Images/Player_Sword_Attack_back4.png",
			"Sword_Images/Player_Sword_Attack_back5.png",
			"Plain_Sprite_Images/Back_Sprite.PNG"]
			
			self.picture = 'Sword_Images/Sword.PNG'
			
			
		if weaponType == self.FIST:
			self.Forward_Sprite = "Plain_Sprite_Images/Forward_Sprite.PNG"
			self.Back_Sprite = "Plain_Sprite_Images/Back_Sprite.PNG"
			self.Left_Sprite = "Plain_Sprite_Images/Left_Sprite.PNG"
			self.Right_Sprite = "Plain_Sprite_Images/Right_Sprite.PNG"
			
			# Attack animations
			self.leftAttack = ["Sword_Images/Player_Sword_Attack_Left1.png",
			"Sword_Images/Player_Sword_Attack_Left2.png",
			"Sword_Images/Player_Sword_Attack_Left3.png",
			"Sword_Images/Player_Sword_Attack_Left4.png",
			"Sword_Images/Player_Sword_Attack_Left5.png",
			"Plain_Sprite_Images/Left_Sprite.PNG"]
			self.rightAttack = ["Sword_Images/Player_Sword_Attack_Right1.png",
			"Sword_Images/Player_Sword_Attack_Right2.png",
			"Sword_Images/Player_Sword_Attack_Right3.png",
			"Sword_Images/Player_Sword_Attack_Right4.png",
			"Sword_Images/Player_Sword_Attack_Right5.png",
			"Plain_Sprite_Images/Right_Sprite.PNG"]
			self.forwardAttack = ["Sword_Images/Player_Sword_Attack_Forward1.png",
			"Sword_Images/Player_Sword_Attack_Forward2.png",
			"Sword_Images/Player_Sword_Attack_Forward3.png",
			"Sword_Images/Player_Sword_Attack_Forward4.png",
			"Sword_Images/Player_Sword_Attack_Forward5.png",
			"Plain_Sprite_Images/Forward_Sprite.PNG"]
			self.backAttack = ["Sword_Images/Player_Sword_Attack_back1.png",
			"Sword_Images/Player_Sword_Attack_back2.png",
			"Sword_Images/Player_Sword_Attack_back3.png",
			"Sword_Images/Player_Sword_Attack_back4.png",
			"Sword_Images/Player_Sword_Attack_back5.png",
			"Plain_Sprite_Images/Back_Sprite.PNG"]
			
			# place holder image because fists have no image
			self.picture = 'Sword_Images/Sword.PNG'
		
		# define image for weapon
		self.image = pygame.image.load(self.picture).convert_alpha()
	
	def restoreRect(self):
		'''
		Set rect to the inner blue box used to determine collision
		'''
		self.rect = Rect(self.x + 10,self.y + 10 ,0.8 * cellSize,0.8 * cellSize)
	
	def deleteRect(self):
		'''
		Set rect to a null rectangle so it can't coolide with anything
		'''
		self.rect = Rect(0,0,0,0)
		
	def adjustXY(self, movex, movey):
		'''
		Used fo relative positioning on plane
		'''
		self.x += movex
		self.y += movey

	def setXY(self, movex, movey):
		'''
		Hard set the x and y coordinate on the plane
		'''
		self.x = movex
		self.y = movey		
	
	def adjustPosXY(self, movex, movey):
		'''
		Used for relative positioning within the cell this weapon exists in (will disappear if moved beyond the cell)
		'''
		self.posX += movex
		self.posY += movey

	def setPosXY(self, movex, movey):
		'''
		Used to hard set the position of this weapon within its cell (will disappear if moved beyond the cell)
		'''
		self.posX = movex
		self.posY = movey
	
	def checkForValidType(self,type):
		'''
		Print error message if the wrong type is used
		'''
		if type not in self.validTypes:
			print("invalid weapon type detected, error may follow")
	
	def attackAnimations(self):
		'''
		returns animation lists for attacking
		'''
		
		return self.forwardAttack, self.backAttack, self.leftAttack, self.rightAttack
	
	
	
	
	
	
	
	