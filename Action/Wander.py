from Config.field import FIELD_CONFIG
from Config.person import PERSON_CONFIG

from . import Action

from random import randint
import numpy as np
from math import atan2, cos, sin


class Wander(Action):
    
    def __init__(self):
        super().__init__()
        self.name = "Wander"
        
        self.destination = np.array([randint(0, FIELD_CONFIG['max_x'] - 1), randint(0, FIELD_CONFIG['max_y'] - 1)])


    def do(self, person):
        super().do(person)
        angle = atan2(self.destination[1] - person.position[1], self.destination[0] - person.position[0])
        distance = np.sqrt(np.sum((self.destination - person.position) ** 2))
        speed = PERSON_CONFIG['default_speed']
        if distance < speed:
            speed = distance
        person.velocity = np.array([speed * cos(angle), speed * sin(angle)])
        person.position = person.position + person.velocity
        if np.all(person.position == self.destination):
            self.finish(person)
        
        
    def get_weight(self, person):
        return 100
