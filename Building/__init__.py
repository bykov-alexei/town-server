from Config.field import FIELD_CONFIG


class Building:

    def __init__(self, x, y):
        self.position = [x, y]
        self.common_position = [x * FIELD_CONFIG['max_x'] // FIELD_CONFIG['max_building_x'], 
                              y * FIELD_CONFIG['max_y'] // FIELD_CONFIG['max_building_y']]
        
        self.type = ''
        
    
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
