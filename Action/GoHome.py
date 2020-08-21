from Config.field import FIELD_CONFIG
from Config.person import PERSON_CONFIG

from . import Action

from random import randint
import numpy as np
from math import atan2, cos, sin


class GoHome(Action):
    
    def __init__(self):
        self.name = "Go home"
        self.destination = None


    def do(self, person):
        self.destination = person.home.common_position
    
        angle = atan2(self.destination[1] - person.position[1], self.destination[0] - person.position[0])
        distance = np.sqrt(np.sum((self.destination - person.position) ** 2))
        speed = PERSON_CONFIG['default_speed']
        if distance < speed:
            speed = distance
        person.velocity = np.array([speed * cos(angle), speed * sin(angle)])
        person.position = person.position + person.velocity
        if np.all(person.position == self.destination):
            person.state_vector['rest'] -= 1
            if person.state_vector['rest'] <= 0:
                person.state_vector['rest'] = 0
                self.finish(person)
        
        
    def get_weight(self, person):
        if person.home is None:
            return 0
        return person.state_vector['rest']
