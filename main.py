import pygame
import random
import math

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hello World")
clock = pygame.time.Clock()

class coin:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.x2 = x + width
        self.y2 = y + height
        self.height = height
        self.width = width

font = pygame.font.Font('freesansbold.ttf', 32) 
x = 50
y = 50
width = 20
height = 20
x2 = x + width
y2 = y + height
vel = 10
newCoin = coin(0,0,0,0)
needCoin = True
amountLeft = 10
paths = []
gameOver = False


def generateCoin():
    randX = math.floor(random.randint(50, 450))
    randY = math.floor(random.randint(50, 450))
    print(randX)
    print(randY)
    return coin(randX, randY, 10, 10)


AImode = True
run = True
start_ticks=pygame.time.get_ticks()
while run:
    keys = pygame.key.get_pressed()
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if keys[pygame.K_r]:
            amountLeft = 10
            gameOver = False

    if(gameOver == False):
        if AImode:
            pass

        if amountLeft <= 0:
            gameOver = True

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 500 - width -vel:
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - vel - height:
            y += vel

        win.fill((0,0,0))
        if needCoin:
            newCoin = generateCoin()
            needCoin = False

        #go down
        if(y < newCoin.y and (abs(newCoin.y - y) > 5)):
            y += vel
        #go up
        elif(y > newCoin.y and (abs(newCoin.y - y) > 5)):
            y -= vel
        #go left
        if(x > newCoin.x and (abs(newCoin.x - x) > 5)):
            x -= vel
        #go right
        elif(x < newCoin.x and (abs(newCoin.x - x) > 5)):
            x += vel

        coin_rect = pygame.Rect(newCoin.x, newCoin.y, newCoin.width, newCoin.height)
        pygame.draw.rect(win, (0,255,0), coin_rect)
        player = pygame.Rect(x, y, width, height)
        coinsLeftText = font.render('Coins Left: ' + str(amountLeft), True, (255,0,0), (0,0,0))
        textRect = coinsLeftText.get_rect()  
        timeText = font.render('Time: ' + str(seconds), True, (255,255,255), (0,0,0))
        pygame.draw.rect(win, (255,0,0), player)
        win.blit(coinsLeftText, textRect)  
        win.blit(timeText, (500 - timeText.get_width() + 20, 0))

        if coin_rect.collidelist([player]) == False: # collision with coin
            print("Colliding")
            amountLeft -= 1
            needCoin = True
            pygame.time.delay(100)
    else:
        gameOverText = font.render('Game Over', True, (255,255,255), (0,0,0))
        gmtextRect = coinsLeftText.get_rect() 
        pygame.draw.rect(win, (0,0,0), (0,0,500,500))
        win.blit(gameOverText,((500 / 2) - (gameOverText.get_width() / 2), (500 / 2) - (gameOverText.get_height() / 2)))
        win.blit(timeText, ((500 / 2) - (timeText.get_width() / 2), (500 / 2) + (timeText.get_height() / 2)))

    pygame.display.update()

    
    
pygame.quit()
