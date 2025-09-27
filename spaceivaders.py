import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("hai")
screen.fill((200,200,250))
score=[0,0]
gameover=False
winner="nobody :p"
bullety=[]
bulletr=[]


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
        gameovertext=font.render(f"GAME OVER! The winner is {winner}",True,(250,250,250))
        screen.blit(gameovertext,(10,200))
    else:
     for i in bulletr:
        pygame.draw.rect(screen,(200,200,250),i)
     for i in bullety:
        pygame.draw.rect(screen,(200,250,250),i)

def gameovernow():
    global gameover,winner
    
    if score[0]==10:
        gameover=True
        winner="yellow"
    elif score[1]==10:
        gameover=True
        winner="red"

def redmove(key):
    if key[pygame.K_w] and redrect.y>0:
        redrect.y-=5
    if key[pygame.K_a] and redrect.x>0:
        redrect.x-=5
    if key[pygame.K_s] and redrect.y<460:
        redrect.y+=5
    if key[pygame.K_d] and redrect.x<205:
        redrect.x+=5

def bluemove(key):
    if key[pygame.K_UP] and yellowrect.y>0:
        yellowrect.y-=5
    if key[pygame.K_LEFT] and yellowrect.x>265:
        yellowrect.x-=5
    if key[pygame.K_DOWN] and yellowrect.y<460:
        yellowrect.y+=5
    if key[pygame.K_RIGHT] and yellowrect.x<460:
        yellowrect.x+=5

def bulletfunc(bulletr,bullety):
    for i in bulletr:
        i.x+=15
        if yellowrect.colliderect(i):
            score[1]+=1
            bulletr.remove(i)
        elif i.x==500:
            bulletr.remove(i)

    for i in bullety:
        i.x-=15
        if redrect.colliderect(i):
            score[0]+=1
            bullety.remove(i)
        elif i.x==0:
            bullety.remove(i)
    
    
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_RCTRL:
                bullet=pygame.Rect(yellowrect.x-25,yellowrect.y+25,10,10)
                bullety.append(bullet)

            if i.key==pygame.K_SPACE:
                bullet=pygame.Rect(redrect.x+25,redrect.y+25,10,10)
                bulletr.append(bullet)
            
    draw()
    gameovernow()
    if not gameover:
        bulletfunc(bulletr,bullety)
        key=pygame.key.get_pressed()
        redmove(key)
        bluemove(key)
   
    pygame.display.update()