from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
Rectangle = True
Circle = False
turn = False
direction = 'right'
cx = 400
cy = 90
r = 200
angle = 0

while True:
    clear_canvas_now()
    grass.draw_now(400, 30) 
    if Rectangle:
        character.draw_now(x, y)
        if direction == 'right':
            if x < 750:
                x = x + 5
                if turn == True:
                    if x == 400:
                        Rectangle = False
                        Circle = True
                        turn = False
                
            else:
                direction = 'up'
                
        elif direction == 'up':
            if y < 550:
                y = y + 5
            else:
              direction = 'left'
              
        elif direction == 'left':
            if x > 50:
                x = x - 5
            else:
               direction = 'down'
               
        elif direction == 'down':
            if y > 90:
                y = y - 5
            else:               
                direction = 'right'
                turn = True
               
    if Circle:
        x = 400 + r * math.cos(math.radians(angle))
        y = 90 + r * math.sin(math.radians(angle))
        character.draw_now(x, y)
        angle = angle + 1
        if angle >= 360:
            angle = 0
            Circle = False
            Rectangle = True
            
    delay(0.01)
         
close_canvas()
