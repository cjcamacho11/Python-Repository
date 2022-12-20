
import pygame
import gamebox
import random

'''Game is tag. 
There are 2 users with user1 having an optional feature of collecting diamonds.
The diamonds serve as an extra measure for competition. User2 chases user1 and once
there is a collision, game is over.'''

camera = gamebox.Camera(1000, 800)
user1 = gamebox.from_color(200, 500, 'cyan', 30, 30)
user2 = gamebox.from_color(800, 500, 'black', 30, 30)
bottom = gamebox.from_color(1000, 800, 'white', -20, 1000)
game_over = gamebox.from_text(500, 400, 'Game Over. Tagger wins!', 100, 'red', bold=True)
interlude_screen = gamebox.from_text(500,400, 'Round 1 done', 80, 'black', bold=True)
random_variable = 0
diamond = []
count = 0
#Booleans
interlude = False
game_on = False
alive = True
round1 = True
round2 = False

def tick(keys):
    interlude = True
    alive2 = True
    global alive
    global diamond
    global count
    global game_on
    global round1
    global round2

#Space starts game
    if pygame.K_SPACE in keys:
        game_on = True

    if not game_on and interlude:  #Displays Starting Screen

        camera.clear('white')
        camera.draw(gamebox.from_text(500, 20, 'Tag: by CJ Camacho', 30, 'black'))
        camera.draw(gamebox.from_image(470,400,'tagimage.png'))
        camera.draw(gamebox.from_color(175,160, 'cyan',40,40))
        camera.draw(gamebox.from_color(835,160, 'black', 40, 40))
        camera.draw(gamebox.from_text(835, 200,'Player 1: Use the Arrows to Tag Player 2!',20,'black'))
        camera.draw(gamebox.from_text(190, 200, 'Player 2: Collect the Diamonds and Use A,S,D,W', 20, 'black'))
        camera.draw(gamebox.from_text(168, 220, 'to Escape the Tagger!', 20, 'black'))
        camera.draw(gamebox.from_text(500, 600, 'Press Space to Begin', 50, 'black'))
        camera.display()

    if alive and game_on:
        camera.clear('dark grey')

        #mechanics for userships 1 and 2

        if pygame.K_d in keys:
            user1.x += 12
            if user1.x > 990:
                user1.x = 990
        if pygame.K_a in keys:
            user1.x -= 12
            if user1.x < 10:
                user1.x = 12
        camera.draw(user1)
        if pygame.K_s in keys:
            user1.y += 12
            if user1.y > 790:
                user1.y = 790
        if pygame.K_w in keys:
            user1.y -= 12
            if user1.y < 10:
                user1.y = 10
        #User 2
        if pygame.K_RIGHT in keys:
            user2.x += 12
            if user2.x > 990:
                user2.x = 990
        if pygame.K_LEFT in keys:
            user2.x -= 12
            if user2.x < 10:
                user2.x = 10
        camera.draw(user2)
        if pygame.K_DOWN in keys:
            user2.y += 12
            if user2.y > 790:
                user2.y = 790
        if pygame.K_UP in keys:
            user2.y -= 12
            if user2.y < 10:
                user2.y = 10

        #collectables
        if random_variable % 10 == 0:
            if random.randint(0,30) == 15:
                new_diamond = gamebox.from_image(random.randint(20,980),random.randint(20,780), 'Diamond.png')
                diamond.append(new_diamond)
                camera.draw(new_diamond)
        for new_diamond in diamond:
            camera.draw(new_diamond)
            if user1.touches(new_diamond):
                diamond.remove(new_diamond)
                count += 1
        score = gamebox.from_text(140, 25, 'Diamonds Collected: ' + str(count), 30,'black', bold=True)
        camera.draw(score)

        #box collisions
        if user2.touches(user1):
            total_diamonds = gamebox.from_text(500, 550, 'You collected ' + str(count) + ' total diamonds!', 75, 'black',bold=True)
            camera.draw(game_over)
            camera.draw(total_diamonds)
            alive = False

    # if pygame.K_r:
    #     interlude = True
    #
    # while interlude:
    #     camera.draw(interlude_screen)


    camera.display()





gamebox.timer_loop(30,tick)
