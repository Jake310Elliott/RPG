import pygame
from pygame.rect import Rect

class AnimationHandler():
	def __init__(self, player, enemyList, droppedItemList,):
		# this will keep track of the animations which must be played
		self.animationQueue = []
		self.animationDict = {}  # Key: event name  value: animation function
		self.frameCount = 0
		
		self.player = player
		self.enemyList = enemyList
		self.droppedItemList = droppedItemList
		self.totalEnemies = set()
	
	def handleAnimations(self):
		'''
		Stand alone function to automatically check and execute the proper animations given their cues.
		Should have access to the:
		- cue to check for each animation
		- animation function
		- animation boolean
		'''
		print(self.animationQueue)
		
		# Account for error: Enemy sprites will be kill()ed before this class can reference them and delete their animation from the queue
		for enemy in self.enemyList:  # This enemy list contains living enemies
			self.totalEnemies.add(enemy)   # This enemy list contains all enemies faced this session

		# Check animation cues
			# if event (cue) detected and event not already queued up (inside animation list), 
				#queue the animation associated with the event (add it to animation list)
				
				
		# ANIMATION EVENT DETECTOR
				
		# If self.player is picking up a weapon
		if self.player.grabbingWeapon == True and self.player.animatorWeaponGrab not in self.animationQueue:
			# queue the weapon grabbing animation function
			self.animationQueue.append(self.player.animatorWeaponGrab)
		# If the animation has finished
		elif self.player.grabbingWeapon == False and self.player.animatorWeaponGrab in self.animationQueue:
			# Delete it from the queue
			del self.animationQueue[0]
		
		
		# cycle through enemies to check their flags individually
		print(self.enemyList)
		for sprite in self.enemyList:
			# if the sprite's dying flag is up
			if sprite.dying == True and sprite.animatorDying not in self.animationQueue:
				# add animation to queue
				self.animationQueue.append(sprite.animatorDying)
		for sprite in self.totalEnemies:
			if sprite.dying == False and sprite.animatorDying in self.animationQueue:
				del self.animationQueue[0]

				
		# Check for self.player attacking flag to be raised
		if self.player.attacking == True and self.player.animatorAttack not in self.animationQueue:
			# queue animation
			self.animationQueue.append(self.player.animatorAttack)
		elif self.player.attacking == False and self.player.animatorAttack in self.animationQueue:
			# remove animation from queue
			del self.animationQueue[0]
		
		# ANIMATION EVENT HANDLER

		# if there is an animation to play
		if len(self.animationQueue) > 0:
			# play the animation that is queued
			self.frameCount = self.animationQueue[0](self.frameCount)
	
	
	
			
			
			
			
			

		
		
		
		
		