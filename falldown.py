#xgv3cj Christian Camacho
import pygame
import gamebox
import random

camera = gamebox.Camera(600, 600)
user = gamebox.from_color(50, 200, "purple", 25, 35)
lowerwall = gamebox.from_color(camera.x, camera.y + 300, "black", 600, 10)
gameover = gamebox.from_text(300, 300, "Game Over. You Lose!", 50, "purple")
tally = gamebox.from_text(camera.x, camera.y - 200, "0", 75, "purple")
alive = True
user.yspeed = 0
counter = 0
tallycounter = 0
walls = [gamebox.from_color(100, 600, "black", 200, 10),
        gamebox.from_color(300, 600, "black", 400, 10),]

def tick(keys):
    global alive
    global gameover
    global tally
    global tallycounter
    global counter
    global lowerwall

    if alive:
        camera.clear("grey")
        if pygame.K_d in keys and user.x < 600:
            user.x += 10
        if pygame.K_a in keys and user.x > 10:
            user.x -= 10
        camera.y += 3
        camera.draw(user)
        counter += 1
        user.yspeed += 2
        user.y = user.y + user.yspeed
        if counter % 30 == 0:
            flength = random.randint(40, 260)
            slength = 600 - flength
            newwall = gamebox.from_color(flength / 2, camera.y + 300, "black", flength, 10)
            walls.append(newwall)
            newwall = gamebox.from_color((slength / 2) + flength + 50, camera.y + 300, "black", slength, 10)
            walls.append(newwall)
        for wall in walls:
            if user.touches(wall):
                user.move_to_stop_overlapping(wall)
            camera.draw(wall)
        if counter % 30 == 0:
            tallycounter += 1
            tally = gamebox.from_text(camera.x, camera.y - 200, str(tallycounter), 75, "purple")
        tally.y += 3
        camera.draw(tally)
        lowerwall.y += 3
        camera.draw(lowerwall)
        if user.y <= camera.y - 320:
            gameover.y = camera.y
            alive = False
        if user.touches(lowerwall):
            user.move_to_stop_overlapping(lowerwall)
    else:
        camera.draw(gameover)
    camera.display()

gamebox.timer_loop(30 , tick)