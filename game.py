#xgv3cj Christian Camacho Evan Schmader ems6rm
'''The game we are creating will be Space Invaders
Like the traditional game, it will consist of a space ship that
will be controlled by the user. There will then be rows of alien ships.
Our goal is to create multiple levels with the difficulty increasing. '''
#4 required features
'''User input: The space ship will be controlled by A and D with A allowing for
 movement to the left, and D for movement to right. The space bar will
 be used to shoot lasers from the space ship that will destroy enemies.'''
'''Game Over: The player will lose the game when an enemy ship fires
back and destroys them or the enemies make it past them.'''
'''Window Size: The plan is to create a window screen of 800 by 600
although this may change.'''
'''Graphics/Images: The background of our game will be like space
with the occasional planet/star. The user controlled ship will be a 
fighter jet or futuristic looking ship. The aliens will be random UFOs.'''
#4 optional features
'''Enemies: Enemies will consist of the UFOs who will sporadically fire
back at the user ship.
Collectables: The goal is to have random coins drop that will act
as a sort of bonus. Another feature to make the game more competitive.
(The hope will be to make these coins savable and placed on a high score screen
per each level.)
Levels: The game will consist of 3 levels with difficulties of
Easy, Medium, and Hard.
Healthbar: The healthbar will be the amount of hits the ship can take.(3)'''

import pygame
import gamebox
import random

camera = gamebox.Camera(600, 600)
#Camera was changed to (600,600) rather than (800,600)
usership = (gamebox.from_image(300,550,'https://im2.ezgif.com/tmp/ezgif-2-fde01b5170.png'))
alive = True
end_game = gamebox.from_text(300, 300, 'Game Over!', 120, 'red', bold=True)
win_game = gamebox.from_text(300, 300, 'You Win!', 120, 'blue', bold = True)
bottom = gamebox.from_color(300, 300, 'white', 0, 600)
lives = 3
randomvariable = 0
score = 0
count = 0
currentlvl = 1
user_lasers = []
enemy_lasers = []
coin = []

#Each level will add a new type of alien
enemy1 = gamebox.from_image(400,250,'1alien3.0.png')
enemy2 = gamebox.from_image(400,300, '2alien3.0.png')
enemy3 = gamebox.from_image(400,350, '3alien3.0.png')

#Level 1
row1_level1 = [
    gamebox.from_image(30, 100, '1alien3.0.png'),
    gamebox.from_image(90, 100, '1alien3.0.png'),
    gamebox.from_image(150, 100, '1alien3.0.png'),
    gamebox.from_image(210, 100, '1alien3.0.png'),
    gamebox.from_image(270, 100, '1alien3.0.png'),
    gamebox.from_image(330, 100, '1alien3.0.png'),
    gamebox.from_image(390, 100, '1alien3.0.png'),
    gamebox.from_image(450, 100, '1alien3.0.png'),
    gamebox.from_image(510, 100, '1alien3.0.png'),
    gamebox.from_image(570, 100, '1alien3.0.png') ]

row2_level1 = [
        gamebox.from_image(30, 200, '1alien3.0.png'),
        gamebox.from_image(90, 200, '1alien3.0.png'),
        gamebox.from_image(150, 200, '1alien3.0.png'),
        gamebox.from_image(210, 200, '1alien3.0.png'),
        gamebox.from_image(270, 200, '1alien3.0.png'),
        gamebox.from_image(330, 200, '1alien3.0.png'),
        gamebox.from_image(390, 200, '1alien3.0.png'),
        gamebox.from_image(450, 200, '1alien3.0.png'),
        gamebox.from_image(510, 200, '1alien3.0.png'),
        gamebox.from_image(570, 200, '1alien3.0.png') ]

#Level 2
row1_level2 = [
    gamebox.from_image(30, 200, '1alien3.0.png'),
    gamebox.from_image(90, 200, '1alien3.0.png'),
    gamebox.from_image(150, 200, '1alien3.0.png'),
    gamebox.from_image(210, 200, '1alien3.0.png'),
    gamebox.from_image(270, 200, '1alien3.0.png'),

    gamebox.from_image(330, 200, '1alien3.0.png'),
    gamebox.from_image(390, 200, '1alien3.0.png'),
    gamebox.from_image(450, 200, '1alien3.0.png'),
    gamebox.from_image(510, 200, '1alien3.0.png'),
    gamebox.from_image(570, 200, '1alien3.0.png') ]
row2_level2 = [
     gamebox.from_image(30, 100, '2alien3.0.png'),
     gamebox.from_image(90, 100, '2alien3.0.png'),
     gamebox.from_image(150, 100, '2alien3.0.png'),
     gamebox.from_image(210, 100, '2alien3.0.png'),
     gamebox.from_image(270, 100, '2alien3.0.png'),
     gamebox.from_image(330, 100, '2alien3.0.png'),
     gamebox.from_image(390, 100, '2alien3.0.png'),
     gamebox.from_image(450, 100, '2alien3.0.png'),
     gamebox.from_image(510, 100, '2alien3.0.png'),
     gamebox.from_image(570, 100, '2alien3.0.png') ]

#Level 3
row1_level3 = [
    gamebox.from_image(30, 300, '1alien3.0.png'),
    gamebox.from_image(90, 300, '1alien3.0.png'),
    gamebox.from_image(150, 300, '1alien3.0.png'),
    gamebox.from_image(210, 300, '1alien3.0.png'),
    gamebox.from_image(270, 300, '1alien3.0.png'),
    gamebox.from_image(330, 300, '1alien3.0.png'),
    gamebox.from_image(390, 300, '1alien3.0.png'),
    gamebox.from_image(450, 300, '1alien3.0.png'),
    gamebox.from_image(510, 300, '1alien3.0.png'),
    gamebox.from_image(570, 300, '1alien3.0.png') ]
row2_level3 = [
     gamebox.from_image(30, 200, '2alien3.0.png'),
     gamebox.from_image(90, 200, '2alien3.0.png'),
     gamebox.from_image(150, 200, '2alien3.0.png'),
     gamebox.from_image(210, 200, '2alien3.0.png'),
     gamebox.from_image(270, 200, '2alien3.0.png'),
     gamebox.from_image(330, 200, '2alien3.0.png'),
     gamebox.from_image(390, 200, '2alien3.0.png'),
     gamebox.from_image(450, 200, '2alien3.0.png'),
     gamebox.from_image(510, 200, '2alien3.0.png'),
     gamebox.from_image(570, 200, '2alien3.0.png') ]
row3_level3 = [
     gamebox.from_image(30, 100, '3alien3.0.png'),
     gamebox.from_image(90, 100, '3alien3.0.png'),
     gamebox.from_image(150, 100, '3alien3.0.png'),
     gamebox.from_image(210, 100, '3alien3.0.png'),
     gamebox.from_image(270, 100, '3alien3.0.png'),
     gamebox.from_image(330, 100, '3alien3.0.png'),
     gamebox.from_image(390, 100, '3alien3.0.png'),
     gamebox.from_image(450, 100, '3alien3.0.png'),
     gamebox.from_image(510, 100, '3alien3.0.png'),
     gamebox.from_image(570, 100, '3alien3.0.png') ]

level1 = [row1_level1,
          row2_level1]

level2 = [row1_level2,
          row2_level2]

level3 =[row1_level3,
         row2_level3,
         row3_level3]

level4 = []

level = {1: level1, 2: level2, 3 : level3, 4: level4}

def tick(keys):
    global alive
    global gameover
    global lives
    global level
    global lives
    global user_lasers
    global enemy_lasers
    global lvltype
    global randomvariable
    global hits
    global currentlvl
    global diamond
    global count
    global score

    if lives != 0 and alive is True:
        camera.clear('black')
        randomvariable += 1

        #determines the level
        if currentlvl == 1:
            if len(level1[0]) == 0 and len(level1[1]) == 0:
                currentlvl += 1
        if currentlvl == 2:
            if len(level1[0]) == 0 and len(level1[1]) == 0 and len(level2[0]) == 0 and len(level2[1]) == 0:
                currentlvl += 1
        elif currentlvl == 3:
            if len(level1[0]) == 0 and len(level1[1]) == 0 and len(level2[0]) == 0 and len(level2[1]) == 0 and len(level3[0]) == 0 and len(level3[1]):
                gameover = True
                currentlvl += 1

        #Determines which heart png shows up
        if lives == 3:
            lives3 = gamebox.from_image(550,25,'heart 3.png')
            camera.draw(lives3)
        if lives == 2:
            lives2 = gamebox.from_image(550,25,'heartbar2.png')
            camera.draw(lives2)
        if lives == 1:
            lives1 = gamebox.from_image(550,25,'heartbar1.png')
            camera.draw(lives1)

#User ship movement and firing
        if pygame.K_d in keys:
            usership.x += 15
            if usership.x > 580:
                usership.x = 580
        if pygame.K_a in keys:
            usership.x -= 15
            if usership.x < 20:
                usership.x = 20
        camera.draw(usership)
        if pygame.K_s in keys:
            laser = gamebox.from_color(usership.x, usership.y, 'red', 2, 6)
            user_lasers.append(laser)

        for laser in enemy_lasers: # Removing lasers that hit bottom
            if laser.touches(bottom):
                enemy_lasers.remove(laser)

        if lives != 0: # If enemy laser hits user ship, the ship will lose a life
            for laser in enemy_lasers:
                if laser.touches(usership):
                    enemy_lasers.remove(laser)
                    lives -= 1
#draws the enemy rows for each level
        if currentlvl == 1:
            for row in level1:
                for enemy in row:
                    camera.draw(enemy)
        if currentlvl == 2:
            for row in level1:
                for enemy in row:
                    camera.draw(enemy)
            for row in level2:
                for enemy in row:
                    camera.draw(enemy)
        if currentlvl == 3:
            for row in level1:
                for enemy in row:
                    camera.draw(enemy)
            for row in level2:
                for enemy in row:
                    camera.draw(enemy)
            for row in level3:
                for enemy in row:
                    camera.draw(enemy)
#Sets up aliens shooting back
        if randomvariable % 7 == 0:
            if currentlvl == 1:
                enemy_x = -30
                enemy_y = 0
                for row in level1:
                    for enemy in row:
                        if random.randint(0, 30) == 20:
                            enemy_x = enemy.x
                            enemy_y = enemy.y
                laser = gamebox.from_color(enemy_x, enemy_y, 'white', 2, 5)
                enemy_lasers.append(laser)
        if randomvariable % 7 == 0:
            if currentlvl == 2:
                enemy_x = -30
                enemy_y = 0
                for row in level1:
                    for enemy in row:
                        if random.randint(0, 30) == 20:
                            enemy_x = enemy.x
                            enemy_y = enemy.y
                laser = gamebox.from_color(enemy_x, enemy_y, 'white', 2, 5)
                enemy_lasers.append(laser)
                enemy_a = -30
                enemy_b = 0
                for row in level2:
                    for enemy in row:
                        if random.randint(0, 20) == 10:
                            enemy_a = enemy.x
                            enemy_b = enemy.y
                laser = gamebox.from_color(enemy_a, enemy_b, 'white', 2, 5)
                enemy_lasers.append(laser)
        if randomvariable % 15 == 0:
            if currentlvl == 3:
                enemy_x = -30
                enemy_y = 0
                for row in level1:
                    for enemy in row:
                        if random.randint(0, 25) == 15:
                            enemy_x = enemy.x
                            enemy_y = enemy.y
                laser = gamebox.from_color(enemy_x, enemy_y, 'white', 2, 5)
                enemy_lasers.append(laser)
                enemy_a = -30
                enemy_b = 0
                for row in level2:
                    for enemy in row:
                        if random.randint(0, 20) == 10:
                            enemy_a = enemy.x
                            enemy_b = enemy.y
                laser = gamebox.from_color(enemy_a, enemy_b, 'white', 2, 5)
                enemy_lasers.append(laser)
                enemy_p = -30
                enemy_l = 0
                for row in level3:
                    for enemy in row:
                        if random.randint(0, 15) == 10:
                            enemy_p = enemy.x
                            enemy_l = enemy.y
                laser = gamebox.from_color(enemy_p, enemy_l, 'white', 2, 5)
                enemy_lasers.append(laser)
#Alien and user shooting mechanics
        for laser in enemy_lasers:
            laser.xspeed = 0
            laser.yspeed = 10
            laser.move_speed()
            camera.draw(laser)

        for laser in user_lasers:
            laser.xspeed = 0
            laser.yspeed = -10
            laser.move_speed()
            camera.draw(laser)

#Laser Collision
        if currentlvl == 1:
            for row in level1:
                for enemy in row:
                    for laser in user_lasers:
                        if laser.touches(enemy) and enemy in row:
                            row.remove(enemy)
                            user_lasers.remove(laser)
                            if len(level1[0]) == 0 and len(level1[1]) == 0:
                                user_lasers = []
        if currentlvl == 2:
            for row in level1:
                for enemy in row:
                    for laser in user_lasers:
                        if laser.touches(enemy) and enemy in row:
                            row.remove(enemy)
                            user_lasers.remove(laser)
                            if len(level1[0]) == 0 and len(level1[1]) == 0:
                                user_lasers = []

            for row in level2:
                for enemy in row:
                    for laser in user_lasers:
                        if laser.touches(enemy) and enemy in row:
                            row.remove(enemy)
                            user_lasers.remove(laser)
                            if len(level2[0]) == 0 and len(level2[1]) == 0:
                                user_lasers = []
        if currentlvl == 3:
            for row in level1:
                for enemy in row:
                    for laser in user_lasers:
                        if laser.touches(enemy) and enemy in row:
                            row.remove(enemy)
                            user_lasers.remove(laser)
                            if len(level1[0]) == 0 and len(level1[1]) == 0:
                                user_lasers = []
            for row in level2:
                for enemy in row:
                    for laser in user_lasers:
                        if laser.touches(enemy) and enemy in row:
                            row.remove(enemy)
                            user_lasers.remove(laser)
                            if len(level2[0]) == 0 and len(level2[1]) == 0:
                                user_lasers = []
            for row in level3:
                for enemy in row:
                    for laser in user_lasers:
                        if laser.touches(enemy) and enemy in row:
                            row.remove(enemy)
                            user_lasers.remove(laser)
                            if len(level3[0]) == 0 and len(level3[1]) == 0:
                                user_lasers = []
        if currentlvl == 1:
            for enemy in row2_level1:
                enemy.y += .5
            for enemy in row1_level1:
                enemy.y += .3
        if currentlvl == 2:
            for enemy in row2_level2:
                enemy.y += .4
            for enemy in row1_level2:
                enemy.y += .3
        if currentlvl == 3:
            for enemy in row3_level3:
                enemy.y += .3
            for enemy in row2_level3:
                enemy.y += .25
            for enemy in row1_level3:
                enemy.y += .2

#collectable coins
        if randomvariable % 50 == 0 and lives <= 3:
            new_coin = gamebox.from_image(random.randint(50, 575), 500, 'gold_coin.png')
            coin.append(new_coin)
            camera.draw(new_coin)
        for new_coin in coin:
            camera.draw(new_coin)
            if usership.touches(new_coin):
                coin.remove(new_coin)
                count += 1
        score = gamebox.from_text(150, 25, 'Coins Collected: ' + str(count), 40,'white', bold=True)
        camera.draw(score)
    if lives == 0:
        camera.draw(end_game)
    if lives >= 1 and currentlvl == 4:
        camera.draw(win_game)

    camera.display()

gamebox.timer_loop(30,tick)