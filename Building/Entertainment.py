from Config.field import FIELD_CONFIG
from Config.game import GAME_CONFIG

from . import Building

from random import choices


class Entertainment(Building):

    def __init__(self, x, y):
        super(Entertainment, self).__init__(x, y)
        
        self.type = 'entertainment'
        self.capacity = 30
        self.taken_places = 0
        
        self.tags = choices(GAME_CONFIG['interests'] + GAME_CONFIG['needs'])
        
    
    def step(self):
        pass
        
        
    def object(self):
        return {
            'type': self.type,
            'position': [int(self.position[0]), int(self.position[1])],
        }
        

