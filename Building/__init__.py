from Config.field import FIELD_CONFIG
from Config.building import BUILDING_CONFIG


class Building:

    def __init__(self, x, y):
        self.position = [x, y]
        self.common_position = [(x + 0.5) * FIELD_CONFIG['max_x'] // FIELD_CONFIG['max_building_x'], 
                              (y + 0.5) * FIELD_CONFIG['max_y'] // FIELD_CONFIG['max_building_y']]
        
        self.type = ''
        self.income = BUILDING_CONFIG['default']['income']
        self.construction_cost = BUILDING_CONFIG['default']['construction_cost']
        self.maintenance_cost = BUILDING_CONFIG['default']['maintenance_cost']
        
    
    def step(self):
        pass
        
        
    def object(self):
        return {
            'type': self.type,
            'position': [int(self.position[0]), int(self.position[1])],
        }
        
from .Home import Home
from .Work import Work
from .Entertainment import Entertainment
