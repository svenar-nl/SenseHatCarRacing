from sense_hat import SenseHat

sense = SenseHat()

while True:
    orientation = sense.get_orientation()
    pitch = round(orientation["pitch"], 0)
    print("orientation: " + str(pitch))