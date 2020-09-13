from Config.field import FIELD_CONFIG
from Config.building import BUILDING_CONFIG

from . import Building


class Home(Building):

    def __init__(self, x, y):
        super(Home, self).__init__(x, y)
        
        self.type = 'home'
        self.taken_places = 0
        
        self.capacity = BUILDING_CONFIG['home']['capacity']
        
        self.income = BUILDING_CONFIG['home']['income']
        self.maintenance_cost = BUILDING_CONFIG['home']['maintenance_cost']
        self.construction_cost = BUILDING_CONFIG['home']['construction_cost']
        
    
    def step(self):
        pass
        
        
    def object(self):
        return {
            'type': self.type,
            'position': [int(self.position[0]), int(self.position[1])],
        }
        

