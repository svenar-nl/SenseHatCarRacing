from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

color = (255, 255, 255)

player_x = 4



def draw_player():
    sense.set_pixel(player_x, 7, color)
    sense.set_pixel(player_x, 6, color)
    

  
#Functions-----------------
def move_right(event):
    global player_x
    if event.action == 'pressed' and player_x < 7:
        player_x += 1
        sense.clear()
        
def move_left(event):
    global player_x
    if event.action == 'pressed'and player_x > 0:
        player_x -= 1
        sense.clear()

cars_position = [3, 3]
cars_velocity = [1, 1]
cars_x  = random.randint(0, 7)
cars_y = 2
cars_color = (0, 0, 255)

def draw_cars():
    sense.set_pixel(cars_x, cars_y, cars_color)
    sense.set_pixel(cars_x, cars_y - 2, (0, 0, 0))

        
    if cars_position[0] == player_x and 8 > cars_position[1] > 5:
        sense.show_message("Helaas!")
    
    
       
        
# Main Program ----------------------

while(1):
    sense.stick.direction_right = move_right
    sense.stick.direction_left = move_left
    time.sleep(0.15)
    draw_player()
    draw_cars()
    cars_y += 1
    if cars_y > 7:
        cars_y = 2
        cars_x  = random.randint(0, 7)
        
    

    

