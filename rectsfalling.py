import pygame, random
pygame.init()
screen=pygame.display.set_mode((500,500),pygame.RESIZABLE)
pygame.display.set_caption("hai")
screen.fill((200,200,250))
colourss=[(123,106,176),(176,106,142),(116,145,214),(222,212,182),(151,166,148)]


class blackboxes(pygame.sprite.Sprite):
    def __init__(self,colour):
        super().__init__()
        self.image=pygame.Surface((25,25))
        self.image.fill(colour)
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.y+=1
        if self.rect.y==500:
            self.resetpos()
    
    def resetpos(self):
            self.rect.x=random.randint(10,450)
            self.rect.y=random.randint(-300,-20)
    

class redblock(blackboxes):
     def update(self):
          mousepos=pygame.mouse.get_pos()
          self.rect.x=mousepos[0]
          self.rect.y=mousepos[1]

blackboxeslist=pygame.sprite.Group()
allboxeslist=pygame.sprite.Group()

for i in range(50):
     box=blackboxes(random.choice(colourss))
     blackboxeslist.add(box)
     allboxeslist.add(box)

redbox=redblock((0,0,0))
allboxeslist.add(redbox)

clock=pygame.time.Clock()

while True:
    clock.tick(40)
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
        
        elif i.type==pygame.VIDEORESIZE:
             screen=pygame.display.set_mode((i.w,i.h),pygame.RESIZABLE)
    
    screen.fill((250,250,250))

    allboxeslist.update()

    collidedblocks=pygame.sprite.spritecollide(redbox,blackboxeslist,False)
    for i in collidedblocks:
         i.resetpos()
    
    allboxeslist.draw(screen)
    pygame.display.update()