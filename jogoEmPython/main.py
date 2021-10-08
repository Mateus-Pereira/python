import pygame
from player import Player
from asteroide import Asteroide
from tiro import Tiro
import random
#Inicializado o Paygame
pygame.init()
#Ciando a janela
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Jogo 2D")

#group
objectGroup = pygame.sprite.Group()
asteroideGroup = pygame.sprite.Group()
tiroGroup = pygame.sprite.Group()

#backgroud!!
bg= pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/fundoA.jpg")
bg.image = pygame.transform.scale(bg.image, [840,480])
bg.rect = bg.image.get_rect()

player = Player(objectGroup)


#Musica
pygame.mixer.music.load("music/fundo.mp3")
pygame.mixer.music.play(-1)

#Som
shoot = pygame.mixer.Sound("music/tiro.wav")

#cria loop do jogo
gameLoop = True
gameOver = False
timer = 20
mclock = pygame.time.Clock()
if __name__ == "__main__":
    #loop do jogo
    while gameLoop:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameOver:
                    shoot.play()
                    newTiro = Tiro(objectGroup, tiroGroup)
                    newTiro.rect.center = player.rect.center
            

        #Update Logic
        if not gameOver:
            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.2:
                    newAsteroide = Asteroide(objectGroup, asteroideGroup)
            
            collisions = pygame.sprite.spritecollide(player, asteroideGroup, False, pygame.sprite.collide_mask)

            if collisions:
                print("Game Over!")
                gameOver = True


            hits = pygame.sprite.groupcollide(tiroGroup, asteroideGroup,  True, True, pygame.sprite.collide_mask)

        #draw
        display.fill([82, 76, 76])
        objectGroup.draw(display)
        pygame.display.update()
