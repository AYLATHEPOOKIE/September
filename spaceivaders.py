import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("hai")
screen.fill((200,200,250))
score=[0,0]
gameover=False
winner="nobody :p"

border=pygame.Rect(247,0,15,500)
yellowship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("yellow.png"),(40,40)),270)
redship=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("red.png"),(40,40)),90)
bg=pygame.image.load("bg20.png")

redrect=pygame.Rect(150,250,40,40)
yellowrect=pygame.Rect(330,250,40,40)

def draw():
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,(170,170,170),border)
    screen.blit(redship,(redrect.x,redrect.y))
    screen.blit(yellowship,(yellowrect.x,yellowrect.y))
    font=pygame.font.SysFont("Rockwell",30)
    scoretext=font.render(f"{score[0]} - {score[1]}",True,(250,250,250))
    screen.blit(scoretext,(220,25))
    if gameover:
        gameovertext=font.render(f"GAME OVERR! The winner is {winner}",True,(250,250,250))
        screen.blit(gameovertext)

def gameovernow():
    global gameover,winner
    
    if score[0]==10:
        gameover=True
        winner="yellow"
    elif score[1]==10:
        gameover=True
        winner="red"

def redmove(key):
    if key[pygame.K_w]:
        redrect.y-=5
    if key[pygame.K_a]:
        redrect.x-=5
    if key[pygame.K_s]:
        redrect.y+=5
    if key[pygame.K_d] and redrect.x<205:
        redrect.x+=5

    
    
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    draw()
    gameovernow()
    key=pygame.key.get_pressed()
    redmove(key)
    pygame.display.update()