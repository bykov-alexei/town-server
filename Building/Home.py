from Config.field import FIELD_CONFIG
from Config.building import BUILDING_CONFIG

from . import Building

import numpy as np


class Home(Building):

    def __init__(self, x, y):
        super(Home, self).__init__(x, y)
        
        self.type = 'home'
        self.taken_places = 0
        
        self.capacity = BUILDING_CONFIG['home']['capacity']
        
        self.income = BUILDING_CONFIG['home']['income']
        self.maintenance_cost = BUILDING_CONFIG['home']['maintenance_cost']
        self.construction_cost = BUILDING_CONFIG['home']['construction_cost']

        min_happiness = BUILDING_CONFIG['home']['min_happiness']
        happiness_delta = BUILDING_CONFIG['home']['happiness_delta']

        x, y = np.arange(0, FIELD_CONFIG['max_x'] + 1), np.arange(0, FIELD_CONFIG['max_y'] + 1)
        x, y = np.meshgrid(x, y)
        a_x, a_y = -1, -1
        home_x, home_y = self.common_position
        b_x, b_y = -2*a_x*home_x, -2*a_y*home_y
        formula = a_x*(x**2) + a_y*(y**2) + b_x*x + b_y*y
        formula = formula - formula.min()
        formula = formula / formula.max()
        formula = formula * happiness_delta
        formula = formula + min_happiness
        self.happiness_layer = formula
        
    
    def step(self):
        pass

    def happiness(self, person):
        x, y = map(int, person.position)
        return round(self.happiness_layer[y][x], 2)
        
    def object(self):
        return {
            'type': self.type,
            'position': [int(self.position[0]), int(self.position[1])],
        }
        

