import pygame
from player import Player
from weapon import Weapon
from pygame.rect import Rect
from toolbarHandler import ToolbarHandler
from enemy import Enemy
from animationHandler import AnimationHandler

#from moving_sprite import MovingSprite
pygame.init()

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

# Open a new window
SCREENX = 1000
SCREENY = 800

# The size of each cell in pixels	
CELL_SIZE = 100

PLANEX = SCREENX / 100
PLANEY = SCREENY / 100


# Initialize the screen
size = (SCREENX, SCREENY + CELL_SIZE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame RPG")

# Initialize toolbarHandler
toolbar = ToolbarHandler(PLANEX,PLANEY, CELL_SIZE)



# Create player sprite AFTER setting screen mode (to avoid image loading errors)
player = Player(toolbar,10,100,100)
# create weapon sprites
sword = Weapon('sword', 5,'sword', 300, 300)
dagger = Weapon('dagger', 2,'sword',400, 200)

# Animation Counters
weaponAnimationCounter = 0
dyingAnimationCounter = 0
playerAttackingCounter = 0






# Create enemies
slime1 = Enemy(toolbar, 'slime', 'slime1',10, 300,200)
slime2 = Enemy(toolbar, 'slime', 'slime2', 10,400,300)

placeHolder = Enemy(toolbar, 'none', 'PlaceHolder enemy', 10,0,0)

# Sprite groups

# player and enemies, npcs ect.
friendlySprites = pygame.sprite.Group()
friendlySprites.add(player)

# items
droppedItems = pygame.sprite.Group()
droppedItems.add(sword)
droppedItems.add(dagger)

# Enemies
enemies = pygame.sprite.Group()
enemies.add(slime1)
enemies.add(slime2)
enemies.add(placeHolder)
# Custom events
#grab_item_event_inProgress = False
#grab_item_event = pygame.USEREVENT + 1

# Animation event handler
Animator = AnimationHandler(player,enemies,droppedItems)

def playerInBounds(condition):
	if condition == 'left':
		return player.x - CELL_SIZE >= 0
	elif condition == 'right':
		return player.x + CELL_SIZE < SCREENX
	elif condition == 'up':
		return player.y - CELL_SIZE >= 0 
	elif condition == 'down':
		return player.y + CELL_SIZE < PLANEY * CELL_SIZE

def printGameBoard():
    # First, clear the screen to white. 
	screen.fill(WHITE)
	# Print a grid of 100 x 100 squares that fits the screen
	for i in range(int(SCREENX/100)):
		for j in range(int(SCREENY/100)):
			if (i + j)%2  == 0:
				pygame.draw.rect(screen, GREEN, [0+100*i,0+100*j,100,100],0)
			else:
				pygame.draw.rect(screen, DARK_GREEN, [0+100*i,0+100*j,100,100],0)

def playerMovement(event):
	if event.mod == 0:
		# Arrow keys feature
		if event.key==pygame.K_LEFT and playerInBounds('left'):
			player.moveLeft()
		elif event.key==pygame.K_RIGHT and playerInBounds('right'):
			player.moveRight()
		elif event.key==pygame.K_UP and playerInBounds('up'):
			player.moveForward()
		elif event.key==pygame.K_DOWN and playerInBounds('down'):
			player.moveBackward()
			
		# WASD feature
		if event.key==pygame.K_a and playerInBounds('left'):
			player.moveLeft()
		elif event.key==pygame.K_d and playerInBounds('right'):
			player.moveRight()
		elif event.key==pygame.K_w and playerInBounds('up'):
			player.moveForward()
		elif event.key==pygame.K_s and playerInBounds('down'):
			player.moveBackward()

	elif event.mod == 1:		
		# Arrow keys feature
		if event.key==pygame.K_LEFT:
			player.turnLeft()
		elif event.key==pygame.K_RIGHT:
			player.turnRight()
		elif event.key==pygame.K_UP:
			player.turnForward()
		elif event.key==pygame.K_DOWN:
			player.turnBackward()
			
		# WASD feature
		if event.key==pygame.K_a:
			player.turnLeft()
		elif event.key==pygame.K_d:
			player.turnRight()
		elif event.key==pygame.K_w:
			player.turnForward()
		elif event.key==pygame.K_s:
			player.turnBackward()

def playerKeys(event):
	if event.key==pygame.K_q:
		player.switchWeapon()
		toolbar.toggleWeapon()
	if event.key == pygame.K_SPACE:
		player.attack(enemies)


def actionHandler():
	# Check for collisions between player and items on the floor
	items_found_list = pygame.sprite.spritecollide(player,droppedItems,False)
	for item in items_found_list:
		# Run initialization method for the grabbing animation
		player.pickUpWeapon(item)
		# Turn the rect object that the spritecollide function uses to determine collision into a 0,0 rect (so that this only runs once)
		item.deleteRect()
	

carryOn = True
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
	# Display equipment information
	#print("Stored Weapons: ",', '.join(i.name for i in player.storedWeapons), "Equiped Weapon: ", player.equipedWeapon.name,player.equipedWeapon.damage,
	#"   MAIN: "+ player.mainWeapon.name, "   SIDE: "+ player.sideWeapon.name)

    # --- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			carryOn = False # Flag that we are done so we exit this loop
		
		# Game Termination key
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_x: #Pressing the x Key will quit the game
				carryOn=False
			# check events for player movement interaction
			playerMovement(event)
			playerKeys(event)
				
	
	
	
	
	
	# Collision Detector
		
	
	
	# collision handler
	
# WEAPON GRABBING ANIMATION
		
	
	
	
	

			
	# player attacking animation handler

	
	


				
				

				
				
				
     # --- Game logic should go here
 
	# Handle actions performed between game elements
	actionHandler()
	# Handle animation attatched to those actions
	Animator.handleAnimations()
 
 
 
 
 
 
 
 
 
     # --- Drawing code should go here
	 
	 
	# GAME BOARD
	 
	 
	# Print the green tile background
	printGameBoard()

				
				
				
				
	# Draw sprites
	
	# Draw dropped items on the field
	for sprite in droppedItems:
		sprite.draw(screen)
	

	# Draw characters
	for sprite in friendlySprites:
		sprite.draw(screen)
	
	# Draw enemies
	
	for sprite in enemies:
		if sprite.dead():
			sprite.dying = True
		sprite.draw(screen)
		
	
	
	
	
	# Draw toolbar
	toolbar.draw(screen)
	

    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
     
    # --- Limit to x frames per second
	clock.tick(30)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()