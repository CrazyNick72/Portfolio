#############################
# Author: Max McLaughlin
# Date : 4/15/21
# Assignment: dev1-42
##############################
# Awesome game program
# Player has to destroy the asteroids to gain points while trying not to get hit

# imports

import sys

import random

import pygame

from pygame.locals import \
    (RLEACCEL,
     K_UP,
     K_DOWN,
     K_LEFT,
     K_RIGHT,
     K_ESCAPE,
     KEYDOWN,
     KEYUP,
     K_SPACE,
     QUIT)

from pygame.locals import *

SCREEN_WIDTH = 900  # Screen size

SCREEN_HEIGHT = 800

class Player(pygame.sprite.Sprite):  # Player class
    walkCount = 0

    def __init__(self):

        super(Player, self).__init__()
        self.surf = pygame.image.load('images/Player_Ship1.png').convert_alpha()
        self.rect = self.surf.get_rect(center=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT - 80),))

    def animationUpdate(self):  # Player animations

        playeranimation = ['images/Player_Ship1.png', 'images/Player_Ship2.png',
                           'images/Player_Ship3.png', 'images/Player_Ship4.png']

        if self.walkCount > len(playeranimation) - 1:  # Goes through animation list, resets back at begining of list
            self.walkCount = 0
        self.surf = pygame.image.load(playeranimation[self.walkCount]).convert_alpha()
        self.walkCount += 1

    def update(self, pressed_keys):  # Player movement

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-9, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(9, 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -9)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 9)

        if self.rect.left <= -60:         # When player goes left or right off the screen, they appear on the other side
            self.rect.right = SCREEN_WIDTH + 55
        if self.rect.right > SCREEN_WIDTH + 60:
            self.rect.left = -55
        if self.rect.top <= 0:                      # player cant go off the top or bottom of the screen
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Laser(pygame.sprite.Sprite):      # laser class

    def __init__(self, right, left):                 # laser and spawn position
        super(Laser, self).__init__()
        Laserimage = 'images/laser.png'
        self.surf = pygame.image.load(Laserimage).convert_alpha()
        self.OGimage = self.surf
        self.right = right
        self.left = left
        self.rightangle = -20
        self.leftangle = 20
        self.rect = self.surf.get_rect(
            center=(player.rect.left + 40, player.rect.bottom - 75),
        )

    def rotate(self):                       # rotate function
        if self.right:
            self.surf = pygame.transform.rotozoom(self.OGimage, self.rightangle, 1)
            self.rect = self.surf.get_rect(center=self.rect.center)
        elif self.left:
            self.surf = pygame.transform.rotozoom(self.OGimage, self.leftangle, 1)
            self.rect = self.surf.get_rect(center=self.rect.center)
    def update(self):           # laser movement
        self.rect.move_ip(0, -15)
        if self.right:
            self.rotate()
            self.rect.move_ip(5, -5)
        if self.left:
            self.rotate()
            self.rect.move_ip(-5, -5)
        if self.rect.bottom <= 0:
            self.kill()


class SmallAsteroid(pygame.sprite.Sprite):  # asteroids

    def __init__(self, chunk, loc):             # asteroid and spawn position
        super(SmallAsteroid, self).__init__()
        self.Xmovement = random.randint(-4, 4)
        self.smallasteroid = 'images/asteroid1.png'
        self.etype = self.smallasteroid
        self.surf = pygame.image.load(self.smallasteroid).convert_alpha()
        self.OGimage = self.surf
        self.angle = 0                                              # angle variable
        self.anglemovement = random.choice([-3, -2, -1, 1, 2, 3])   # Value asteroid will turn
        if chunk:                               # Checks if asteroid is a chunk
            self.rect = loc
        else:
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(5, SCREEN_WIDTH - 10),
                    random.randint(1, 10),
                ))

    def rotate(self):                       # rotate function
        self.surf = pygame.transform.rotozoom(self.OGimage, self.angle, 1)
        self.rect = self.surf.get_rect(center=self.rect.center)

    def update(self):  # Asteroid movement
        self.angle += self.anglemovement
        self.rotate()                       # Asteroid will rotate by a value
        self.rect.move_ip(self.Xmovement, 5)
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()  # Gets killed if it goes off the bottom of the screen
        if self.rect.left <= -35:               # Appears on the other side of the screen if it goes left or right
            self.rect.right = SCREEN_WIDTH + 30
        if self.rect.right > SCREEN_WIDTH + 35:
            self.rect.left = -30
        if upgrades < level and upgrades < 7:
            self.kill()


class MediumAsteroid(pygame.sprite.Sprite):

    def __init__(self, chunk, loc):
        super(MediumAsteroid, self).__init__()
        self.Xmovement = random.randint(-4, 4)
        self.mediumasteroid = 'images/asteroid3.png'
        self.etype = self.mediumasteroid
        self.surf = pygame.image.load(self.mediumasteroid).convert_alpha()
        self.OGimage = self.surf
        self.anglemovement = random.choice([-3, -2, -1, 1, 2, 3])
        self.angle = 0
        if chunk:
            self.rect = loc
        else:
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(5, SCREEN_WIDTH - 10),
                    random.randint(1, 10),
                ))

    def rotate(self):
        self.surf = pygame.transform.rotozoom(self.OGimage, self.angle, 1)
        self.rect = self.surf.get_rect(center=self.rect.center)

    def update(self):
        self.angle += self.anglemovement
        self.rotate()
        self.rect.move_ip(self.Xmovement, 3)
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()
        if self.rect.left <= -35:
            self.rect.right = SCREEN_WIDTH + 30
        if self.rect.right > SCREEN_WIDTH + 35:
            self.rect.left = -30
        if upgrades < level and upgrades < 7:
            self.kill()


class LargeAsteroid(pygame.sprite.Sprite):

    def __init__(self):
        super(LargeAsteroid, self).__init__()
        self.Xmovement = random.randint(-4, 4)
        self.largeasteroid = 'images/asteroid4.png'
        self.etype = self.largeasteroid
        self.surf = pygame.image.load(self.largeasteroid).convert_alpha()
        self.OGimage = self.surf
        self.anglemovement = random.choice([-3, -2, -1, 1, 2, 3])
        self.angle = 0
        self.rect = self.surf.get_rect(
            center=(
                random.randint(5, SCREEN_WIDTH - 10),
                random.randint(1, 10),
            ))

    def rotate(self):
        self.surf = pygame.transform.rotozoom(self.OGimage, self.angle, 1)
        self.rect = self.surf.get_rect(center=self.rect.center)

    def update(self):  # Asteroid movement
        self.angle += self.anglemovement
        self.rotate()
        self.rect.move_ip(self.Xmovement, 2)
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()
        if self.rect.left <= -70:
            self.rect.right = SCREEN_WIDTH + 65
        if self.rect.right > SCREEN_WIDTH + 70:
            self.rect.left = -65
        if upgrades < level and upgrades < 7:
            self.kill()

pygame.init()               # initializes pygame

pygame.font.init()          # initializes font and text

particles = []

level = 1

upgradedlaser = False

playerimpact = False

upgrades = 1

laser2 = False

lasercap = 10

lasercharge = 0

score = 0

levelprogress = 0

health = 5

lasers = 10

upgrading = False

white = (255, 255, 255)

yellow = (255, 255, 0)

font = pygame.font.SysFont('timesnewroman', 32)         # Creates font and print size for text

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('AHAHAHAHAHA')

player = Player()               # Creates player and other entities

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

all_lasers = pygame.sprite.Group()

all_smallasteroids = pygame.sprite.Group()

all_mediumasteroids = pygame.sprite.Group()

all_largeasteroids = pygame.sprite.Group()

ADDsmallasteroid = pygame.USEREVENT + 1
pygame.time.set_timer(ADDsmallasteroid, 7000 - level * 1000)

ADDmediumasteroid = pygame.USEREVENT + 2
pygame.time.set_timer(ADDmediumasteroid, 9000 - level * 1000)

ADDlargeasteroid = pygame.USEREVENT + 3
pygame.time.set_timer(ADDlargeasteroid, 11000 - level * 1000)

ADDlaser = pygame.USEREVENT + 4
pygame.time.set_timer(ADDlaser, 3000 - lasercharge * 1000)

running = True

while running: # game loop

    screen.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    if levelprogress >= 100:
        level += 1
        levelprogress = 0

        pygame.time.set_timer(ADDlaser, 3000 - lasercharge * 1000)

        if level < 6:
            pygame.time.set_timer(ADDsmallasteroid, 7000 - level * 1000)
            pygame.time.set_timer(ADDmediumasteroid, 9000 - level * 1000)
            pygame.time.set_timer(ADDlargeasteroid, 11000 - level * 1000)
        elif level == 6 or level < 8:
            pygame.time.set_timer(ADDsmallasteroid, 1000)
            pygame.time.set_timer(ADDmediumasteroid, 9000 - level * 1000)
            pygame.time.set_timer(ADDlargeasteroid, 11000 - level * 1000)
        elif level == 8 or level < 10:
            pygame.time.set_timer(ADDsmallasteroid, 1000)
            pygame.time.set_timer(ADDmediumasteroid, 1000)
            pygame.time.set_timer(ADDlargeasteroid, 11000 - level * 1000)
        elif level == 10:
            pygame.time.set_timer(ADDsmallasteroid, 1000)
            pygame.time.set_timer(ADDmediumasteroid, 1000)
            pygame.time.set_timer(ADDlargeasteroid, 1000)

    if health == 0:
        running = False

    if playerimpact:
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            colors = ['white', 'yellow']
            color = random.choice(colors)
            if color == 'yellow':
                color = yellow
            elif color == 'white':
                color = white
            pygame.draw.circle(screen, color, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

    else:
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(screen, white, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)

    playerimpact = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                quit()

            if event.key == K_SPACE:        # Laser functionality
                makeparticle = True

                if lasers > 0:
                    laser = Laser(False, False)
                    all_lasers.add(laser)
                    all_sprites.add(laser)
                    lasers -= 1
                    if laser2:
                        laser = Laser(True, False)
                        all_lasers.add(laser)
                        all_sprites.add(laser)
                        laser = Laser(False, True)
                        all_lasers.add(laser)
                        all_sprites.add(laser)

            if event.key == K_w:
                if laser2 == False:
                    if upgrades < level and upgrades < 7:
                        laser2 = True
                        upgrades += 1

            if event.key == K_d:
                if upgrades < level and upgrades < 7:
                    lasercap += 5
                    lasers = lasercap
                    upgrades += 1

            if event.key == K_s:
                if upgrades < level and upgrades < 7:
                    health += 5
                    upgrades += 1

            if event.key == K_a:
                if lasercharge < 2:
                    if upgrades < level and upgrades < 7:
                        lasercharge += 1
                        upgrades += 1

        elif event.type == QUIT:
            running = False

        elif event.type == ADDlaser:            # Laser cool down time
            if lasers >= 0 and lasers < lasercap:
                lasers += 1

        if event.type == ADDsmallasteroid:  # Spawns asteroids
            epicAsteroid = SmallAsteroid(False, 'nope')
            all_smallasteroids.add(epicAsteroid)
            all_sprites.add(epicAsteroid)

        elif event.type == ADDmediumasteroid:
            epicAsteroid = MediumAsteroid(False, 'nope')
            all_mediumasteroids.add(epicAsteroid)
            all_sprites.add(epicAsteroid)

        elif event.type == ADDlargeasteroid:
            epicAsteroid = LargeAsteroid()
            all_largeasteroids.add(epicAsteroid)
            all_sprites.add(epicAsteroid)

    textlaser = font.render('LASERS: ' + str(lasers), False, (white))       # Creates and updates text

    texthealth = font.render('HEALTH: ' + str(health), False, (white))

    textscore = font.render('SCORE: ' + str(score), False, (white))

    textlevel = font.render('LEVEL: ' + str(level), False, (white))

    textleveldown = font.render('S to level up health', False, (white))

    textlevelright = font.render('D to level up laser capacity', False, (white))

    textlevelleft = font.render('A to level up laser recharge', False, (white))

    textlevelspace = font.render('W to level up laser', False, (white))

    textlevelsure = font.render('are you sure you want to level this up?', False, (white))

    textYes = font.render('Y for yes', False, (white))

    textno = font.render('N for no', False, (white))

    player.animationUpdate()  # Updates positions of player and other entities

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    all_lasers.update()

    all_smallasteroids.update()

    all_mediumasteroids.update()

    all_largeasteroids.update()

    screen.blit(texthealth, (0, 0))         # Displays text

    screen.blit(textlaser, (0, 50))

    screen.blit(textscore, (0, 100))

    screen.blit(textlevel, (700, 0))

    if upgrades < level and upgrades < 7:

        screen.blit(textlevelleft, (0, 300))

        screen.blit(textlevelright, (500, 300))

        screen.blit(textleveldown, (300, 350))

        screen.blit(textlevelspace, (300, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

# Collisions

    hit = pygame.sprite.groupcollide(all_smallasteroids, all_lasers, True, True)
    for sprite in hit:
        score += 5
        levelprogress += 5
        if hit[sprite]:
            loc = sprite.rect
            Ploc1 = loc[0]
            Ploc2 = loc[1]
            for num in range(10):
                particles.append([[Ploc1, Ploc2], [random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5],
                                  random.randint(1, 6)])


    hit = pygame.sprite.groupcollide(all_mediumasteroids, all_lasers, True, True)
    for sprite in hit:
        score += 5
        levelprogress += 5
        if hit[sprite]:     # If laser hits an asteroid that is medium or large, asteroid will spawn smaller asteroids
            loc = sprite.rect
            Ploc1 = loc[0]
            Ploc2 = loc[1]
            for num in range(10):
                particles.append([[Ploc1, Ploc2], [random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5],
                                  random.randint(1, 6)])

        for i in [1, 2]:
            epicAsteroid = SmallAsteroid(True, loc)
            all_smallasteroids.add(epicAsteroid)
            all_sprites.add(epicAsteroid)

    hit = pygame.sprite.groupcollide(all_largeasteroids, all_lasers, True, True)
    for sprite in hit:
        levelprogress += 5
        score += 5
        if hit[sprite]:
            collision = True
            loc = sprite.rect
            Ploc1 = loc[0]
            Ploc2 = loc[1]
            for num in range(40):
                particles.append([[Ploc1, Ploc2], [random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5],
                                  random.randint(1, 6)])

        for i in [1, 2]:
            epicAsteroid = MediumAsteroid(True, loc)
            all_mediumasteroids.add(epicAsteroid)
            all_sprites.add(epicAsteroid)

    playerSmallAsteroid = pygame.sprite.spritecollideany(player, all_smallasteroids)  # Collision with player sprite
    if playerSmallAsteroid != None:
        playerSmallAsteroid.kill()
        score -= 5
        levelprogress -=5
        health -= 1
        loc = player.rect
        Ploc1 = loc[0]
        Ploc2 = loc[1]
        for num in range(6):
            particles.append([[Ploc1, Ploc2], [random.randint(0, 200) / 6 - 3.5, random.randint(0, 200) / 6 - 3.5],
                            random.randint(2, 3)])
        playerimpact = True

    playerMediumAsteroid = pygame.sprite.spritecollideany(player, all_mediumasteroids)
    if playerMediumAsteroid != None:
        playerMediumAsteroid.kill()
        score -= 10
        levelprogress -= 10
        health -= 1
        loc = player.rect
        Ploc1 = loc[0]
        Ploc2 = loc[1]
        for num in range(8):
            particles.append([[Ploc1, Ploc2], [random.randint(0, 150) / 6 - 3.5, random.randint(0, 150) / 6 - 3.5],
                              random.randint(2, 3)])
        playerimpact = True

    playerLargeAsteroid = pygame.sprite.spritecollideany(player, all_largeasteroids)
    if playerLargeAsteroid != None:
        playerLargeAsteroid.kill()
        score -= 20
        levelprogress -= 20
        health -= 1
        loc = player.rect
        Ploc1 = loc[0]
        Ploc2 = loc[1]
        for num in range(10):
            particles.append([[Ploc1, Ploc2], [random.randint(0, 100) / 6 - 3.5, random.randint(0, 100) / 6 - 3.5],
                              random.randint(2, 3)])
        playerimpact = True

    pygame.display.flip()  # Displays game

    clock.tick(30)
