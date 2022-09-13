from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

color = (255, 255, 255)

player_x = 4
game_speed = 7

cars = []
target_num_cars = 3
high_score = 0
total_cars_passed = 0

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

def draw_cars():
    global cars
    global total_cars_passed
    global game_speed
    global high_score
    
    for car in cars:
        if car.y >= 0 and car.y < 8:
            sense.set_pixel(car.x, car.y, car.color)
        if car.y - 1 >= 0 and car.y - 1 < 8:
            sense.set_pixel(car.x, car.y - 1, car.color)
            
        if car.x == player_x and 8 > car.y > 5:
            sense.show_message("Helaas!", 0.04, (60, 255, 70))
            sense.show_message("Score: ", 0.04, (60, 255, 70))
            sense.show_message(str(total_cars_passed), 0.04, (255, 60, 70))
            sense.show_message("Highscore: ", 0.04, (60, 255, 70))
            sense.show_message(str(high_score), 0.04, (255, 60, 70))
            game_speed = 7
            if total_cars_passed > high_score:
                high_score = total_cars_passed
            total_cars_passed = 0
            cars = []
            break
    
    
class Car:
    def __init__(self) -> None:
        self.x = random.randint(0, 7)
        self.y = -1
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.passed = False
       
        
# Main Program ----------------------
    sense.stick.direction_right = move_right
    sense.stick.direction_left = move_left

def mapval(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while(1):
    draw_player()
    draw_cars()
    time.sleep(1 / game_speed)
    
    orientation = sense.get_orientation()
    rawpitch = round(orientation["pitch"], 0)
    rawpitch = rawpitch if rawpitch < 180 else rawpitch - 360
    rawpitch = -rawpitch
    pitch = int(mapval(rawpitch, -25, 25, 0, 7))
    pitch = pitch if pitch > 0 else 0
    pitch = pitch if pitch < 8 else 7
    print(rawpitch)
    print(pitch)
    player_x = pitch
    
    if random.randint(0, 100) < 25:
        if len(cars) < target_num_cars:
            newCar = Car()
            cars.append(newCar)
    
    tmp_cars = cars
    for car in cars:
        if car.passed:
            tmp_cars.remove(car)
            total_cars_passed += 1
        car.y += 1
        if car.y > 7:
            car.passed = True
    cars = tmp_cars
    
    print("Cars passed: " + str(total_cars_passed) + " speed: " + str(game_speed))
    if total_cars_passed > 0 and total_cars_passed < 50 and total_cars_passed % 10 == 0:
        sense.show_message("Speed up!", 0.04, (60, 255, 70))
        game_speed += 1
        total_cars_passed += 1
    
    if total_cars_passed > 50 and total_cars_passed % 40 == 0:
        sense.show_message("Speed up!", 0.04, (60, 255, 70))
        game_speed += 1
        total_cars_passed += 1
#     cars_y += 1
#     if cars_y > 6:
#         cars_y = 0
#         cars_x  = random.randint(0, 7)
    sense.clear(0,0,0)
    

    

