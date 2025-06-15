import pygame
import random
import asyncio
pygame.display.set_caption("blob game")
pygame.init()
game_over = 0
run = True
game_WITH = 800
game_height = 600
st_y = 0
st_x = 0
bullllet = False
speed = 2
pl_x = 350
pl_y = 220
pl_h = 11
pl_b = 77
scall = 10
sall = 100
bl_x = pl_x+50
bl_y = pl_y
spt = 0.5
spt2 = 0.5
score = 0
st2_y = 0
st2_x = 200
TEXTCOLOUR = (200, 100, 0)
fps = 60
bg = pygame.image.load('bg.png')
screen = pygame.display.set_mode((game_WITH, game_height))

#images
player_mg_r = pygame.image.load('Sprite-0001.png').convert_alpha()
bulllet = pygame.image.load('bullet.png').convert_alpha()
star = pygame.image.load('sttar.png').convert_alpha()

def draw():
    screen.blit(player.image, player)
    screen.blit(bullet.image, bullet)

screen.fill((0,0,0))
screen.blit(bg,(0,0))
pygame.display.flip()


class Player(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_mg_r
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location

class Bullet(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulllet
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
class Star(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = star
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location

fontObj = pygame.font.Font('font.ttf', 50)
fontObj2 = pygame.font.Font('font.ttf', 50)
fontObj3 = pygame.font.Font('font.ttf', 50)
fontObj4 = pygame.font.Font('font.ttf', 50)
score: str = 0
textSufaceObj = fontObj.render(str(score), True, TEXTCOLOUR, None)
textSufaceObj2 = fontObj2.render("game over", True, TEXTCOLOUR, None)
textSufaceObj3 = fontObj3.render("quit", True, TEXTCOLOUR, None)
textSufaceObj4 = fontObj4.render("play again", True, TEXTCOLOUR, None)
screen.blit(textSufaceObj, (1000, 100))
playyy = pygame.draw.rect(screen, "blue", (0, 599, 799, 20))
bullet = Bullet([pl_x,pl_y])
player = Player([pl_x,pl_y])
stars = Star([st_x,st_y])
stars2 = Star([200,st_y])
clock = pygame.time.Clock()
posss = random.randint(0, 710)
st_x = posss
st_y = -10 
posss = random.randint(0, 710)
st2_x = posss
st2_y = -10 
game_over = 0

async def main():
    global game_over
    global TEXTCOLOUR
    while True:
        clock.tick(fps)
        if game_over == 0:
            textSufaceObj2 = fontObj2.render("shoot the space", True, TEXTCOLOUR, None)
            textSufaceObj4 = fontObj4.render("play", True, TEXTCOLOUR, None)
            screen.fill((0,55,0))
            screen.blit(bg,(0,0))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mous = pygame.draw.rect(screen, "black", (mouse_x, mouse_y, 1, 1))
            screen.blit(textSufaceObj2, (150, 180))
            starrr4 = pygame.draw.rect(screen, "black", (280, 270, 200, 100), border_radius=40)
            starrr64 = pygame.draw.rect(screen, "black", (280, 380, 200, 100), border_radius=40)
            screen.blit(textSufaceObj3, (315, 290))
            screen.blit(textSufaceObj4, (315, 400))
            if starrr4.colliderect(mous):
                starrr4 = pygame.draw.rect(screen, "grey", (280, 270, 200, 100), border_radius=40)
                screen.blit(textSufaceObj3, (315, 290))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exit()
                    run = False
            if starrr64.colliderect(mous):
                starrr64 = pygame.draw.rect(screen, "grey", (280, 380, 200, 100), border_radius=40)
                screen.blit(textSufaceObj4, (315, 400))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_over = 1
                    run = True
                    game_WITH = 800
                    game_height = 600
                    st_y = 0
                    st_x = 0
                    bullllet = False
                    speed = 2
                    pl_x = 350
                    pl_y = 220
                    pl_h = 11
                    pl_b = 77
                    scall = 10
                    sall = 100
                    bl_x = pl_x+50
                    bl_y = pl_y
                    spt = 0.5
                    spt2 = 0.5
                    score = 0
                    st2_y = 0
                    st2_x = 200
                    TEXTCOLOUR = (200, 100, 0)
                    score = 0
                    textSufaceObj = fontObj.render(str(score), True, TEXTCOLOUR, None)
        if game_over == 3:
            textSufaceObj2 = fontObj2.render("paus menu", True, TEXTCOLOUR, None)
            textSufaceObj4 = fontObj4.render("play again", True, TEXTCOLOUR, None)
            screen.fill((0,55,0))
            screen.blit(bg,(0,0))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mous = pygame.draw.rect(screen, "black", (mouse_x, mouse_y, 1, 1))
            screen.blit(textSufaceObj2, (200, 250))
            starrr4 = pygame.draw.rect(screen, "black", (280, 320, 200, 100), border_radius=40)
            starrr64 = pygame.draw.rect(screen, "black", (200, 430, 400, 100), border_radius=40)
            screen.blit(textSufaceObj3, (315, 330))
            screen.blit(textSufaceObj4, (240, 440))
            screen.blit(textSufaceObj, (380, 0))
            if starrr4.colliderect(mous):
                starrr4 = pygame.draw.rect(screen, "grey", (280, 320, 200, 100), border_radius=40)
                screen.blit(textSufaceObj3, (315, 330))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exit()
                    run = False
            if starrr64.colliderect(mous):
                starrr64 = pygame.draw.rect(screen, "grey", (200, 430, 400, 100), border_radius=40)
                screen.blit(textSufaceObj4, (240, 440))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_over = 1
                    textSufaceObj = fontObj.render(str(score), True, TEXTCOLOUR, None)
        if game_over == 2:
            textSufaceObj2 = fontObj2.render("game over", True, TEXTCOLOUR, None)
            textSufaceObj4 = fontObj4.render("play again", True, TEXTCOLOUR, None)
            screen.fill((0,55,0))
            screen.blit(bg,(0,0))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mous = pygame.draw.rect(screen, "black", (mouse_x, mouse_y, 1, 1))
            screen.blit(textSufaceObj2, (200, 250))
            starrr4 = pygame.draw.rect(screen, "black", (280, 320, 200, 100), border_radius=40)
            starrr64 = pygame.draw.rect(screen, "black", (200, 430, 400, 100), border_radius=40)
            screen.blit(textSufaceObj3, (315, 330))
            screen.blit(textSufaceObj4, (240, 440))
            screen.blit(textSufaceObj, (380, 0))
            if starrr4.colliderect(mous):
                starrr4 = pygame.draw.rect(screen, "grey", (280, 320, 200, 100), border_radius=40)
                screen.blit(textSufaceObj3, (315, 330))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exit()
                    run = False
            if starrr64.colliderect(mous):
                starrr64 = pygame.draw.rect(screen, "grey", (200, 430, 400, 100), border_radius=40)
                screen.blit(textSufaceObj4, (240, 440))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_over = 1
                    run = True
                    game_WITH = 800
                    game_height = 600
                    st_y = 0
                    st_x = 0
                    bullllet = False
                    speed = 2
                    pl_x = 350
                    pl_y = 220
                    pl_h = 11
                    pl_b = 77
                    scall = 10
                    sall = 100
                    bl_x = pl_x+50
                    bl_y = pl_y
                    spt = 0.5
                    spt2 = 0.5
                    score = 0
                    st2_y = 0
                    st2_x = 200
                    TEXTCOLOUR = (200, 100, 0)
                    score = 0
                    textSufaceObj = fontObj.render(str(score), True, TEXTCOLOUR, None)

            

        if game_over == 1:
            stars2 = Star([st2_x,st2_y])
            st_y += spt
            st2_y += spt2
            stars = Star([st_x,st_y])
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                pl_x -= speed
                if keys[pygame.K_s]:
                    pl_y += speed / 2
                if keys[pygame.K_w]:
                    pl_y -= speed / 2
            elif keys[pygame.K_d]:
                pl_x += speed
                if keys[pygame.K_s]:
                    pl_y += speed / 2
                if keys[pygame.K_w]:
                    pl_y -= speed / 2
            elif keys[pygame.K_s]:
                pl_y += speed
            elif keys[pygame.K_w]:
                pl_y -= speed
            if keys[pygame.K_ESCAPE]:
                game_over = 3
            if keys[pygame.K_SPACE] or event.type == pygame.MOUSEBUTTONDOWN:
                bl_x = pl_x+50
                bl_y = pl_y
                bullllet = True
                
        
            if bullllet:
                pygame.draw.rect(screen, (255, 0, 0), (pl_x, pl_y, 20, 40))
        
            



            player = Player([pl_x,pl_y])
            player.image = pygame.transform.scale(player.image, (110, 110))
            stars.image = pygame.transform.scale(stars.image, (100, 100))
            stars2.image = pygame.transform.scale(stars.image, (100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                run = False
        if game_over == 1:
            screen.fill((0,55,0))
            screen.blit(bg,(0,0))
            screen.blit(player.image,player.rect)
            screen.blit(stars.image,stars.rect)
            screen.blit(stars2.image,stars2.rect)
            if bullllet:
                bullet = Bullet([bl_x,bl_y])
                bl_y = bl_y - 5
                bullet.image = pygame.transform.scale(bullet.image, (10, 10))
                screen.blit(bullet.image,bullet.rect)
        
            starrr = pygame.draw.rect(screen, "red", (st_x, st_y, sall, sall), 1)
            bull = pygame.draw.rect(screen, "green", (bl_x, bl_y, scall, scall), 1)
            playy = pygame.draw.rect(screen, "blue", (pl_x, pl_y, sall, sall), 1)
            starrr2 = pygame.draw.rect(screen, "red", (st2_x, st2_y, sall, sall), 1)


            if playyy.colliderect(starrr2):
                posss = random.randint(0, 750)
                st2_x = posss
                st2_y = -10 
            if playyy.colliderect(starrr):
                posss = random.randint(0, 750)
                st_x = posss
                st_y = -10
            if starrr.colliderect(bull):
                spt += 0.3
                posss = random.randint(0, 710)
                st_x = posss
                st_y = -10 
                speed += 0.1
                score += 1
                print(score)
                pygame.draw
                print(spt)
                textSufaceObj = fontObj.render(str(score), True, TEXTCOLOUR, None)
            if starrr2.colliderect(bull):
                spt2 += 0.3
                posss = random.randint(0, 710)
                st2_x = posss
                st2_y = -10 
                speed += 0.1
                score += 1
                print(score)
                pygame.draw
                print(spt)
                textSufaceObj = fontObj.render(str(score), True, TEXTCOLOUR, None)
            if starrr.colliderect(playy):
                game_over = 2
            if starrr2.colliderect(playy):
                game_over = 2
            screen.blit(textSufaceObj, (380, 0))


        pygame.display.update()
        await asyncio.sleep(0)
    
asyncio.run(main())









































    