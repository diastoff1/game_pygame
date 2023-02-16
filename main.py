# importing and inicializing
import sys
import pygame
import random
from comet import Comet

pygame.init()

# to optimize the program we use clock to set a framerate (not necessary here)
clock = pygame.time.Clock()

# set the size and create a display
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# load the images

icon = pygame.image.load('img/comet.png')
playerImg = pygame.image.load('img/nave1.png')

# comet
comet_img1 = pygame.image.load('img/ast2.png')
comet_img2 = pygame.image.load('img/ast3.png')
comets = []

# change the logo and title of the app
pygame.display.set_icon(icon)
pygame.display.set_caption("Arcade Storm")

# background
background = pygame.image.load('img/background1.jpg')

# variables of position and variation
posX = 370
posY = 500
varX = 0
varX_L = 0
varX_R = 0
varY = 0
varY_U = 0
varY_D = 0

prob = 10

game_over = False

# Font and size for the score display
score_font = pygame.font.SysFont("PressStart2P", 40)
score = 0
score_text = score_font.render("Score: " + str(score), True, (255, 255, 51))


def point():
    global score
    global score_text
    score += 2
    score_text = score_font.render(
        "Score: " + str(score), True, (255, 255, 51))


score_x = 3
score_y = 3

# Set the font and font size for the "Game Over" message
game_over_font = pygame.font.SysFont("PressStart2P", 128)
game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))

# Set the font and font size for the "Press Space to Continue" message
continue_font = pygame.font.SysFont("PressStart2P", 40)
continue_text = continue_font.render(
    "Press Space to Continue", True, (255, 255, 255))

center_x = 400
center_y = 300

# Calculate the coordinates to position the "Game Over" message in the center of the screen
game_over_x = center_x - game_over_text.get_width() // 2
game_over_y = center_y - game_over_text.get_height()

# Calculate the coordinates to position the "Press Space to Continue" message below the "Game Over" message
continue_x = center_x - continue_text.get_width() // 2
continue_y = center_y + game_over_text.get_height() // 2

# maintain the display and create an exit to it
while True:
    # RGB
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    if random.randint(0, 1) == 1:
        comet_img = comet_img1
    else:
        comet_img = comet_img2

    if prob < 200:
        prob += 0.002

    if random.randint(0, 10000) <= prob:
        comet = Comet(width, comet_img)
        comets.append(comet)

    for comet in comets:
        comet.update()
        comet.draw(screen)

    for event in pygame.event.get():

        # press X to exit
        if event.type == pygame.QUIT:
            sys.exit()
        # putting keys to move
        if event.type == pygame.KEYDOWN and not game_over:
            # X axis
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                varX_L = -0.5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                varX_R = 0.5
            # Y axis
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                varY_U = -0.5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                varY_D = 0.5
        if event.type == pygame.KEYUP:
            # X axis
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                varX_L = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                varX_R = 0
            # Y axis
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                varY_U = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                varY_D = 0
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                score = 0
                game_over = False

    # check if the player is inside the limit of the map
    """if posX <= 2:
        varX_L = 0
    if posX > 734:
        varX_R = 0
    if posY <= 0:
        varY_U = 0
    if posY > 540:
        varY_D = 0"""

    varX = varX_L + varX_R
    varY = varY_U + varY_D
    posX += varX
    posY += varY

    # there's also an easy alternative insted the above code, but in some level it 'teleport' the player, so I thought to do in a way it couldn't happen, which is the way I did.

    if posX >= 734:
        posX = 734
    if posX <= 2:
        posX = 2
    if posY <= 0:
        posY = 0
    if posY >= 540:
        posY = 540

    # revome comets off the screen
    new_comets = []
    clean = []
    for comet in comets:
        if (comet.y+15 >= posY and comet.y <= posY+47) and (comet.x+15 >= posX and comet.x <= posX+47):
            game_over = True
            new_comets = clean
            posX = 370
            posY = 500
            varX = 0
            varX_L = 0
            varX_R = 0
            varY = 0
            varY_U = 0
            varY_D = 0
            prob = 10

        if comet.y < height and not game_over and not comet.y > height+3:
            new_comets.append(comet)
        if comet.y > height:
            point()

    comets = new_comets

    if game_over == True:
        # Draw the "Game Over" message in the center of the screen
        screen.blit(game_over_text, (game_over_x, game_over_y))

        # Draw the "Press Space to Continue" message below the "Game Over" message
        screen.blit(continue_text, (continue_x, continue_y))

    # Draw the score display
    screen.blit(score_text, (score_x, score_y))

    # draw the player image on the screen
    screen.blit(playerImg, (posX, posY))

    # update the display
    pygame.display.update()
