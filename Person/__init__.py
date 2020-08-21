from Config.field import FIELD_CONFIG
from Config.game import GAME_CONFIG

from random import choices
import numpy as np


class Person:


    def __init__(self, id):
        self.id = id
    
        self.home_town = None
        self.home = None
        self.work_place = None
        
        self.action = None
        
        self.position = np.array([FIELD_CONFIG['max_x'] // 2, FIELD_CONFIG['max_y'] // 2])
        self.velocity = np.zeros((2,))
        
        self.interests = choices(GAME_CONFIG['interests'], k=GAME_CONFIG['n_interests'])
        self.needs = GAME_CONFIG['needs']
        self.state_vector = {}
        for interest in self.interests:
            self.state_vector[interest] = 1
        for need in self.needs:
            self.state_vector[need] = 1
            
        
    def step(self):
        self.increase_state()

        self.choose_action()
        self.action.do(self)
        
   
    def increase_state(self):
        for key, item in self.state_vector.items():
            self.state_vector[key] += item       
        
    
    def choose_action(self):
        if self.action is None:
            actions = self.home_town.get_actions()
            weights = [action().get_weight(self) for action in actions]
            self.action = choices(actions, weights)[0]()
        
    def change_town(self, towns):
        attractions = [self.town_attraction(town) for town in towns]
        self.home_town = choices(towns, attractions)[0]
        self.home_town.settle(self)
        
    
    def town_attraction(self, town):
        return town.attraction
        
    
    def object(self):
        obj = {
            'id': self.id,
            'position': [int(self.position[0]), int(self.position[1])],
            'velocity': [int(self.velocity[0]), int(self.velocity[1])],
        }
        return obj
