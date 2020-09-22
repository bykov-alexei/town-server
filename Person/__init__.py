from Config.field import FIELD_CONFIG
from Config.game import GAME_CONFIG

from random import choices, randint
import numpy as np


from Action import GoHome

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
        self.happiness = 50
        self.penalties = {
            'work': 0,
            'home': 0,
        }

        self.delta_vector = {}
        self.state_vector = {}
        for interest in self.interests:
            self.delta_vector[interest] = 1
            self.state_vector[interest] = 0
        for need in self.needs:
            self.delta_vector[need] = 1
            self.state_vector[need] = 0
            
        
    def step(self):
        if type(self.action) == GoHome:
            print(self.action)

        self.increase_state()
        self.calc_happiness()

        self.choose_action()
        self.action.do(self)
        
   
    def increase_state(self):
        for key, item in self.state_vector.items():
            if key in self.needs or key in self.interests:
                self.state_vector[key] += (0.1 * self.delta_vector[key])


    def calc_happiness(self):
        happiness = 0
        if self.home is not None:
            happiness += 30
        if self.work_place is not None:
            happiness += 15
        for key, value in self.penalties.items():
            if value < 0:
                self.penalties[key] = 0
            happiness -= self.penalties[key]
        self.happiness = happiness

    
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
            'happiness': self.happiness,
        }
        return obj
