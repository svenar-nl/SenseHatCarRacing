import platform
from player import Player
import time
import threading

class Game:
    def __init__(self) -> None:
        self.is_running = False
        self.player = Player()
        self.cars = []
        self.tps = 20
        self.fps = 60
        
        self.thread_update = None
        self.thread_draw = None
    
    def setup(self) -> None:
        self.is_running = True
        
        self.thread_update = threading.Thread(target=self.update)
        self.thread_draw = threading.Thread(target=self.draw)
    
    def loop(self) -> None:
        self.thread_update.start()
        self.thread_draw.start()
        while self.is_running:
            pass
        self.thread_update.join()
        self.thread_draw.join()
    
    def update(self) -> None:
        while self.is_running:
            self.player.update()
            for car in self.cars:
                car.update()
            
            time.sleep(1 / self.tps)
    
    def draw(self) -> None:
        while self.is_running:
            self.player.draw()
            for car in self.cars:
                car.draw()
            
            time.sleep(1 / self.fps)

if __name__ == "__main__":
    print("Running on: " + platform.system() + " " + " ".join(platform.architecture()) + " (" + platform.machine() + ", " + platform.processor() + ")")
    
    print("Initializing...")
    game = Game()
    print("Preparing...")
    game.setup()
    print("Running...")
    try:
        game.loop()
    except KeyboardInterrupt:
        game.is_running = False
    print("Exiting the game...")