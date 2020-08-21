from Config.field import FIELD_CONFIG
from Config.person import PERSON_CONFIG

from . import Action

from random import randint
import numpy as np
from math import atan2, cos, sin


class GoSomewhere(Action):
    
    def __init__(self, building):
        self.name = "Go home"
        self.building = building
        self.destination = building.common_position


    def do(self, person):
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
        score = 0
        for tag in building.tags:
            score += person.state_vector[tag]
        return score
