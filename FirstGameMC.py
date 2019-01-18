import pygame, time, sys, random
#creates instance of pygame
pygame.init()
#game font
myfont = pygame.font.Font("Haike-col.ttf", 60)
font2 = pygame.font.Font("gomarice_game_music_love.ttf", 60)
#game constants and other initializations
ENEMYSPEED = 17
PLAYERSPEED = 10
WIDTH = 600
HEIGHT = 600
PURPLE = (139,0,139)
BLACK = (255,255,255)
#level
level = 0
timesEnemyHitBottom = 0
#enemy position list that will keep track of all enemy positions by storing each list of coordinates in here (2d list).
enemy_poslist = [[100, 0],[200,0],[300, 0],[400, 0],[500, 0]]
enemy_size = 35
enemy_sizelist = [enemy_size,enemy_size,enemy_size,enemy_size,enemy_size]
#player functionality like size (area of rectangle) and the start x and y coordinates
player_size=35
player_x = WIDTH/2
player_y = HEIGHT - (player_size*2)
#create screen by setting the display to width and height
screen = pygame.display.set_mode([WIDTH,HEIGHT])
game_over = False
clock = pygame.time.Clock()
dodgecount = 0

#background class that creates a background object that has both image,and location of where image is placed
#also creates a rectangle and gives its location as the top (0), allows for image provided to be the background by being a rectangle displayed to the screen

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def levelchange(dodgecount):
    if dodgecount == 10 or dodgecount == 20 or dodgecount == 30 or dodgecount == 40 or dodgecount == 50 : #every addition of dodgecount += 10 here to check signifies levels
        return True
    else: return False

# create backgrounds to be used in the function below that puts these images on the background coordinate of [0,0] that gets stored as the background rect
BackGroundlvl1 = Background("background1.jpg", [0,0])
BackGroundlvl2 = Background("background2.jpg", [0,0])
BackGroundlvl3 = Background("background3.jpg", [0,0])
BackGroundlvl4 = Background("background4.jpg", [0,0])
BackGroundlvl5 = Background("background5.jpg", [0,0])
BackGroundlvl6 = Background("backgroundfinallvl.jpg", [0,0])
def displayBG(level):
    print(level)
    if level == 1:
        screen.blit(BackGroundlvl1.image, BackGroundlvl1.rect)
    elif level == 2:
        screen.blit(BackGroundlvl2.image, BackGroundlvl2.rect)
    elif level == 3:
        screen.blit(BackGroundlvl3.image, BackGroundlvl3.rect)
    elif level == 4:
        screen.blit(BackGroundlvl4.image, BackGroundlvl4.rect)
    elif level == 5:
        screen.blit(BackGroundlvl5.image, BackGroundlvl5.rect)
    elif level >= 6:
        screen.blit(BackGroundlvl6.image, BackGroundlvl6.rect)
def create_enemies(level,enemy_sizelist):
    global enemy_poslist
    if level == 2:
        # each enemies size (in radius)
        count = 0
        for i in enemy_sizelist:
            enemy_sizelist[count] = 30
            count = count + 1
        enemy_sizelist.append(30)
        #clear list to fill with enemies for lvl2
        # enemy starting coordinates, after the first drop their x starting position is randomized through a function.
        enemy_poslist = [[100, 0],[200, 0],[300, 0],[400, 0],[500,0]]
    if level == 3:
        # each enemies size (in radius)
        count = 0
        for i in enemy_sizelist:
            enemy_sizelist[count] = 32
            count = count + 1
        enemy_sizelist.append(32)
        #clear list to fill with enemies for lvl2
        # enemy starting coordinates, after the first drop their x starting position is randomized through a function.
        enemy_poslist = [[100, 0],[200, 0],[300, 0],[400, 0],[500,0],[550,0]]
    if level == 4:
        # each enemies size (in radius)
        count = 0
        for i in enemy_sizelist:
            enemy_sizelist[count] = 34
            count = count + 1
        enemy_sizelist.append(34)
        #clear list to fill with enemies for lvl2
        # enemy starting coordinates, after the first drop their x starting position is randomized through a function.
        enemy_poslist = [[100, 0],[200, 0],[300, 0],[400, 0],[500,0],[550,0]]
    if level == 5:
        # each enemies size (in radius)
        count = 0
        for i in enemy_sizelist:
            enemy_sizelist[count] = 34
            count = count + 1
        enemy_sizelist.append(34)
        #clear list to fill with enemies for lvl2
        # enemy starting coordinates, after the first drop their x starting position is randomized through a function.
        enemy_poslist = [[100, 0],[200, 0],[300, 0],[400, 0],[500,0],[550,0], [600,0]]
    if level == 6:
        # each enemies size (in radius)
        count = 0
        for i in enemy_sizelist:
            enemy_sizelist[count] = 19
            count = count + 1
        enemy_sizelist.append(19)
        #clear list to fill with enemies for lvl2
        # enemy starting coordinates, after the first drop their x starting position is randomized through a function.
        enemy_poslist = [[100, 0],[200, 0],[300, 0],[400, 0],[500,0],[550,0], [600,0]]
#checks if enemy is at the bottom of the screen or not,  if they are randomize where at the top they start again.
def enemy_movement(enemy_positions,level,count):
    if enemy_positions[1] >= 0 and enemy_positions[1] < HEIGHT-enemy_size:
        #since top of screen is 0 bottom is height we add to make the enemy go downward
        enemy_positions[1] += ENEMYSPEED
    else:
        enemy_positions[0] = random.randint(0, WIDTH - enemy_size)
        enemy_positions[1] = 0
        #if the count that is passed as param to this function is 0 then this is the first enemy been replaced after hitting the bottom, increment dodgecount only for this ememy as to not multiply the number.
        if count == 0:
            global dodgecount
            dodgecount = dodgecount + 1
            if levelchange(dodgecount):
                global problemfixcount
                problemfixcount = 0
    return enemy_positions

#checks for collisions using an algorithm I drew out to create a box around the square and check if it collides  with the rectangle
def collision_check(enemy_x,enemy_y,player_x,player_y,enemy_size,player_size):
    if (enemy_x >= player_x and enemy_x < (player_x+player_size))or(player_x >= enemy_x and player_x < (enemy_x+enemy_size)):
        if (enemy_y >= player_y and enemy_y < (player_y+player_size))or(player_y >= enemy_y and player_y < (enemy_y+enemy_size)):
            return True
    return False

#decided to make drawenemies a function that will go through the amount regardless how many and draw them to the surface accordingly
def drawenemies(enemy_poslist):
    count = 0
    listlength = len(enemy_poslist)
    while count < listlength:
        enemy_poslist[count] = enemy_movement(enemy_poslist[count],level,count)
        enemyrect = pygame.draw.rect(screen, PURPLE, (enemy_poslist[count][0], enemy_poslist[count][1], enemy_sizelist[count],enemy_sizelist[count]),0)
        enemyBackGround = Background("enemypic.jpg", [enemy_poslist[count][0], enemy_poslist[count][1]])
        screen.blit(enemyBackGround.image,enemyBackGround.rect )
        count = count + 1
pygame.mixer.music.load("game_music.mp3")
pygame.mixer.music.play(-1)
dodgecount = 0
problemfixcount = 0
dodgestowin = 60
#while the game not over...
while not game_over:
    #if level two start the graphics for level 2 at beggining then red
    if problemfixcount == 0 and (dodgecount == 0  or levelchange(dodgecount) ):
        level1 = "Level   " + str(level + 1)
        label = font2.render(level1, 1, (232, 111, 104))
        create_enemies(level, enemy_sizelist)
        level += 1
        displayBG(level)
        drawenemies(enemy_poslist)
        pygame.draw.rect(screen, PURPLE, (player_x, player_y, player_size, player_size), 0)
        screen.blit(label, (165, 240))
        pygame.display.update()
        time.sleep(2.0)
        problemfixcount = 1

    keys = pygame.key.get_pressed()  # returns an array of booleans associated to each key on whether or not it is pressed
    #appropriate up down left right key movement capabilities, holding results in continous movement by checking if keys are currently
    # pressed or not. This game uses the arrow keys for movement. the below multiline comment disables up and down movement
    """if keys[pygame.K_UP]:
        #these secondary if checks force the player to "stay in bounds"
        if player_y > 0:
            player_y -= PLAYERSPEED
    if keys[pygame.K_DOWN]:
        if player_y < HEIGHT - player_size:
            player_y += PLAYERSPEED"""
    if keys[pygame.K_LEFT]:
        if player_x > 0:
            player_x -= PLAYERSPEED
    if keys[pygame.K_RIGHT]:
        if player_x < WIDTH - player_size:
            player_x += PLAYERSPEED

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        """" the following commented out code moves the character (square) everytime an key is pressed instead of held down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x = player_x - 30
            elif event.key == pygame.K_RIGHT:
                player_x = player_x + 30
            elif event.key == pygame.K_DOWN:
                player_y = player_y + 30
            elif event.key == pygame.K_UP:
                player_y = player_y - 30 """
    #draws the background onto the surface of the screen by using background class attributes of image and the rectangle passed as it its the top corner
        # check if dodgecount is equivalent to 60 which means end of game if true print congrats they won and exit
    if dodgecount == 60:
        game_over = True
        label = myfont.render("Congratulations Winner!", 1, (232, 111, 104))
        displayBG(level)
        screen.blit(label, (25, 250))
        pygame.display.update()
        # allow music to fadeout once game is exiting
        pygame.mixer.music.fadeout(6000)
        time.sleep(6)
    else:
        displayBG(level)
        #count to be used to increment throughout, this for loop allows for any number of enemies depending on how many i decide per level ect.
        drawenemies(enemy_poslist)
        pygame.draw.rect(screen,PURPLE,(player_x,player_y,player_size,player_size),0)
        clock.tick(30)
        pygame.display.update()
    #collision check to see if there is a collision after the display has updated based on the last movements.
    if collision_check(enemy_poslist[0][0],enemy_poslist[0][1],player_x,player_y,enemy_size,player_size) or collision_check(enemy_poslist[1][0],enemy_poslist[1][1],player_x,player_y,enemy_sizelist[1],player_size) or collision_check(enemy_poslist[2][0],enemy_poslist[2][1],player_x,player_y,enemy_sizelist[2],player_size) or collision_check(enemy_poslist[3][0],enemy_poslist[3][1],player_x,player_y,enemy_sizelist[3],player_size) :
        game_over = True
        label = myfont.render("Game Over!", 1, (232, 111, 104))
        screen.blit(label, (165, 240))
        pygame.display.update()
        # allow music to fadeout once game is exiting
        pygame.mixer.music.fadeout(3000)
        time.sleep(3)
#signifies the game is over as it has exited the while loop since game_over was set to true, does the appropriate measures to exit the game after short delay.
pygame