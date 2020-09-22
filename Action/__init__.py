from Config.game import GAME_CONFIG


class Action:


    def __init__(self):
        self.time = 0
        pass
 
 
    def do(self, person):
        self.time += 1
        pass
        
        
    def finish(self, person):
        person.action = None


    def get_weight(self, person):
        return 1

    def get_minutes(self):
        delta = 60 * 24 // GAME_CONFIG['steps_in_day']
        return self.time * delta
        

from .Wander import Wander
from .GoHome import GoHome
from .GoWork import GoWork
from .GoSomewhere import GoSomewhere
