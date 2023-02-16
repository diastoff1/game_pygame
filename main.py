#importing and inicializing 
import sys, pygame, random
from comet import Comet
pygame.init()

#to optimize the program we use clock to set a framerate
clock = pygame.time.Clock()

#set the size and create a display
size = width, height = 800,600
screen = pygame.display.set_mode(size)

#load the images

icon = pygame.image.load('img/comet.png')
playerImg = pygame.image.load('img/nave1.png')

#comet
comet_img=pygame.image.load('img/cometa.png')
comets=[]

#change the logo and title of the app
pygame.display.set_icon(icon)
pygame.display.set_caption("Arcade Storm")

#background (img source: br.freepik.com/vetores-gratis/fundo-gradiente-de-galaxia_14658088.htm#query=space&position=0&from_view=search&track=sph)
background = pygame.image.load('img/background.jpg')

#variables of position and variation
posX = 370
posY = 500
varX = 0
varX_L = 0
varX_R = 0
varY = 0
varY_U = 0
varY_D = 0

#maintain the display and create an exit to it
while True:   
    #RGB
    screen.fill((0,0,0))

    screen.blit(background,(0,0))


    if random.randint(0, 1500) == 0:
        comet = Comet(width, comet_img)
        comets.append(comet)

    for comet in comets:
        comet.update()
        comet.draw(screen)

    for event in pygame.event.get():

        #set the max framerate to 144 (set it because my monitor is 144hz but 30 is very ok)

        #press X to exit
        if event.type == pygame.QUIT:
            sys.exit()

        #putting keys to move
        if event.type == pygame.KEYDOWN:
            # X axis
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                varX_L = -0.2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                varX_R = 0.2
            # Y axis
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                varY_U = -0.2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                varY_D = 0.2
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
        

    #check if the player is inside the limit of the map 
    if posX <= 2:
        varX_L = 0
    if posX > 734:
        varX_R = 0
    if posY <= 0:
        varY_U = 0
    if posY > 540:
        varY_D = 0
          
    varX = varX_L + varX_R
    varY = varY_U + varY_D
    posX += varX
    posY += varY

    #there's also an easy alternative insted the above code, but in some level it 'teleport' the player, so I thought to do in a way it couldn't happen, which is the way I did.
    """
    if posX >= 734:
        posX = 734
    if posX <= 2:
        posX = 2
    if posY <= 0:
        posY = 0
    if posY >= 540:
        posY = 540
    """

    #revome comets off the screen
    comets = [comet for comet in comets if comet.y < height]

    #draw the player image on the screen
    screen.blit(playerImg, (posX, posY))

    #update the display
    pygame.display.update()
