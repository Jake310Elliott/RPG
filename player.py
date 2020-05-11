import pygame
from entity import Entity
from weapon import Weapon
from toolbarHandler import ToolbarHandler
from box import Box
from pygame.rect import Rect
#from collections import namedtuple
#import weapon

WHITE = (255, 255, 255)
 
class Player(Entity):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
	
	def __init__(self,toolbar, health = 10, X = 125, Y = 125, spawnPosition = 'forward', cellSize = 100):
		# Call the parent class (Entity) constructor
		super().__init__("Plain_Sprite_Images/Left_Sprite.PNG", "Plain_Sprite_Images/Right_Sprite.PNG", "Plain_Sprite_Images/Forward_Sprite.PNG", 
		"Plain_Sprite_Images/Back_Sprite.PNG", cellSize, X, Y, spawnPosition)
		
		# Initialize toolbar
		self.toolbar = toolbar
		
		# Initialize health
		self.health = health
		self.maxHealth = health
		
		# Must be set by picking up a weapon
		self.grabWeaponAnimation_Left = ["no animation"]
		self.grabWeaponAnimation_Right = ["no animation"]
		self.grabWeaponAnimation_Forward = ["no animation"]
		self.grabWeaponAnimation_Back = ["no animation"]
		

		self.weaponToBeGrabbed = ("none", 0)
		# default weapon grabbing animation to forward (doesn't matter unless weapon is initialized on character before game starts)
		self.animation = self.grabWeaponAnimation_Forward
		
		# save presets to revert back to when item is gone
		self.Plain_Forward_Sprite = self.Forward_Sprite # movement sprites are set in moving_sprite with the init function
		self.Plain_Back_Sprite = self.Back_Sprite
		self.Plain_Left_Sprite = self.Left_Sprite
		self.Plain_Right_Sprite = self.Right_Sprite
		
		self.fists = Weapon("fists", 1,'fist')
		#self.equipedItems = {} # TODO: add more items to equip
		self.mainWeapon = self.fists
		self.sideWeapon = self.fists
		
		
		
		
		
		# initialize main weapon as the equiped weapon
		self.equipedWeapon = self.fists
		self.storedWeapons = set()
		
		# weapon toggle
		self.mainWeaponEquiped = True
				
		
		# variable used for storing position of weapon we're picking up
		self.weaponGrabPos = (0,0)
		
		# Cell that the player can attack
		self.attackBox = Box(self.frontRect)
		#print(self.attackBox.__repr__)   # This is used to make sure the object isn't creatign a memory leak by creating a new object and keeping the old one
		
		# animation flags
		self.grabbingWeapon = False
		self.attacking = False
		
		self.leftAttack = []
		self.rightAttack = []
		self.forwardAttack = []
		self.backAttack = []
		# This will be called in the animation
		self.attackPosition = self.forwardAttack
		
		# Initialize the fists as equiped weapon
		
		self.equipWeapon(self.equipedWeapon)
		
	
	def equipWeapon(self, item):
		'''
		Adds item's effects to player (item must be an equipable) (equipable has not been made a type yet)
		'''
		# If the item we're equiping was in our storage
		if item.name in self.storedWeapons:
			# delete it from storage and equip the item, also store equiped item
			self.equipedWeapon = item
			self.storedWeapons.remove(item.name)
			self.storedWeapons.append(self.equipedWeapon)
		# If the item we're equiping was from the floor
		else:
			# equip the item and add the weapon we're holding to storage
			self.equipedWeapon = item
			self.storedWeapons.add(self.equipedWeapon)
			
		# clear storage of duplicates DANGEROUS: COULD CAUSE LOSS OF ITEMS
		#self.storedWeapons = list(dict.fromkeys(self.storedWeapons))
		
		# Update grabbing animation
		self.grabWeaponAnimation_Left = item.grabWeaponAnimation_Left 
		self.grabWeaponAnimation_Right = item.grabWeaponAnimation_Right
		self.grabWeaponAnimation_Forward = item.grabWeaponAnimation_Forward
		self.grabWeaponAnimation_Back = item.grabWeaponAnimation_Back
		
		# update walking animations
		self.Forward_Sprite = item.Forward_Sprite
		self.Back_Sprite = item.Back_Sprite
		self.Left_Sprite = item.Left_Sprite
		self.Right_Sprite = item.Right_Sprite
		
		# update attack animations
		self.leftAttack = item.leftAttack
		self.rightAttack = item.rightAttack
		self.forwardAttack = item.forwardAttack
		self.backAttack = item.backAttack
		
	def revertSprite(self):
		'''
		Revert sprite back to having no items
		'''
		self.Forward_Sprite = self.Plain_Forward_Sprite
		self.Back_Sprite = self.Plain_item.Back_Sprite
		self.Left_Sprite = self.Plain_item.Left_Sprite
		self.Right_Sprite = self.Plain_item.Right_Sprite
		
	def switchWeapon(self):
		'''
		Toggle between main and side weapon
		'''
		# toggle boolean
		self.mainWeaponEquiped = not self.mainWeaponEquiped
		# equip designated weapon
		if self.mainWeaponEquiped:
			self.equipWeapon(self.mainWeapon)
		else:
			self.equipWeapon(self.sideWeapon)
	
	
	
	
	
	def getEquippedWeapon(self):
		return equipedWeapon
	
	def getStoredWeapon(self):
		return storedWeapons
		
	def storeWeapon(self,weapon):
		'''
		add weapon to storage
		'''
		self.storedWeapons.append(weapon)
	
	def attack(self,enemyList):
		'''
		perform attack functions and activate animation (with physical weapon)
		'''
		#print("player.attack()")
		i = 1
		for enemy in enemyList:
			#print("enemy {} is in attack box?: {}".format(i,pygame.sprite.collide_rect(enemy,self.attackBox)))
			#print("enemy rect: {}, player attckbox: {}".format(enemy,self.attackBox))
			# Determine attacked monster
			if pygame.sprite.collide_rect(enemy,self.attackBox):
				enemy.takeDamage(self.equipedWeapon)
				#print("enemy {} hit!".format(i))
			# Do this if the monster was not the attacked monster
			else:
				pass#print("enemy {} missed".format(i))
			i+=1
			self.attacking = True
	
	def updateAttackPosition(self):
		'''
		This is caled repeatedly to keep the attack animation up to date
		'''
		if self.position == self.FORWARD:
			self.attackPosition = self.forwardAttack
		if self.position == self.BACKWARD:
			self.attackPosition = self.backAttack
		if self.position == self.LEFT:
			self.attackPosition = self.leftAttack
		if self.position == self.RIGHT:
			self.attackPosition = self.rightAttack
	
	
	
	
	
	
	
	
	
	
	def pickUpWeapon(self, weapon):
		'''
		Set proper animation list and initiate animation
		'''
		self.grabbingWeapon = True
		self.weaponToBeGrabbed = weapon
		self.weaponGrabPos = (self.x, self.y)
		
		# Replace empty hand with weapon
		if self.mainWeapon == self.fists:
			self.mainWeapon = weapon
		elif self.sideWeapon == self.fists:
			self.sideWeapon = weapon
		
		# equip respective weapon depending on equiped weapon boolean
		if self.mainWeaponEquiped:
			self.equipWeapon(self.mainWeapon)
		else:
			self.equipWeapon(self.sideWeapon)
		
		
		
		# set animation list for current position                   		# TODO: choose animation based on weapon
		if self.position == self.FORWARD:
			#print("animation set to forward")
			self.animation = self.grabWeaponAnimation_Forward
		if self.position == self.BACKWARD:
			#print("animation set to backward")
			self.animation = self.grabWeaponAnimation_Back
		if self.position == self.LEFT:
			#print("animation set to Left")
			self.animation = self.grabWeaponAnimation_Left
		if self.position == self.RIGHT:
			#print("animation set to Right")
			self.animation = self.grabWeaponAnimation_Right
		
	def animatorWeaponGrab(self, i):
		'''
		Generate animation to be looped through (set for 20 frames per animation image or which there are 3 + initial position frame)
		i : animation clock tick that allows function to display one image per specified number of frames
		This function is repeatedly called when the grabbing weapon flag is active
		USE: Set a counter equal to this function with the same counter as the input. this function will increment that counter until the animation finishes then terminate the
		Grabbing weapon counter
		'''
		# Debugging prints
		#print("beginning of animator")
		#print("animation: ", self.animation)
		weapon = self.weaponToBeGrabbed

		#print("self.grabbingWeapon: {}".format(self.grabbingWeapon))
		#print("i // 20: ", i//20)
		if i // 20 > 3:
			# remove weapon from screen
			weapon.kill()
			
			# Reflect weapon attainment on toolbar (if possible)
			if self.toolbar.getWeaponAvailability().main:
				self.toolbar.setMainWeapon(weapon)
			elif self.toolbar.getWeaponAvailability().side:
				self.toolbar.setSideWeapon(weapon)
			
			# restore position to facing forward # TODO restore previous position
			self.image = pygame.image.load(self.animation[3]).convert_alpha()
			self.setPosition(self.animation[-1])
			# end animation loop
			self.grabbingWeapon = False
			return 0
			#print("self.grabbingWeapon: {}".format(self.grabbingWeapon))
		if i // 20 == 3:
			# presenting item image
			self.image = pygame.image.load(self.animation[2]).convert_alpha()
			# change item position cell to be above acharacter
			weapon.setXY(self.weaponGrabPos[0],self.weaponGrabPos[1]-100)
			# make weapon visable again
			weapon.setPosXY(self.posX,self.posY + 60)
		elif i // 20 == 2:
			# previous position image
			self.image = pygame.image.load(self.animation[1]).convert_alpha()
			# make item dissapear during this frame (by drawing the image off the sprite surface which is the size and position of current cell)
			weapon.setPosXY(-100,-100) # used instead of kill() so it can be easily restored after
		elif i // 20 == 1:
			# bending down image
			self.image = pygame.image.load(self.animation[0]).convert_alpha()
		# increment frame counter (controlled by main loop clock speed)
		return i + 1

		
	def animatorAttack(self, i):
		#print(i,i//10)
		if i // 1 == 1:
			#print("fisrst")
			self.image = pygame.image.load(self.attackPosition[0]).convert_alpha()
		elif i // 1 == 1:
			#print("Second")
			self.image = pygame.image.load(self.attackPosition[1]).convert_alpha()
		elif i // 5 == 1:
			#print("thirdw")
			self.image = pygame.image.load(self.attackPosition[2]).convert_alpha()
		elif i // 6 == 1:
			#print("Fourth")
			self.image = pygame.image.load(self.attackPosition[3]).convert_alpha()
		elif i // 7 == 1:
			#print("Fifth")
			self.image = pygame.image.load(self.attackPosition[4]).convert_alpha()
		elif i // 8 == 1:
			#print("done")
			self.attacking = False
			self.image = pygame.image.load(self.attackPosition[5]).convert_alpha()
			return 0
		
		return i + 1
	
	
	
	def update(self, surface = None):
		'''
		this method is called every time the draw function is called
		'''
		self.attackBox = Box(self.frontRect)
		#print(self.attackBox.__repr__)
		self.updateAttackPosition()

	
	
	
	
	
	
	
	
	

        
