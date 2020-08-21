from Config.field import FIELD_CONFIG

from . import Building


class Work(Building):

    def __init__(self, x, y):
        super(Work, self).__init__(x, y)
        
        self.type = 'work'
        self.capacity = 30
        self.taken_places = 0
        
    
    def step(self):
        pass
        
        
    def object(self):
        return {
            'type': self.type,
            'position': [int(self.position[0]), int(self.position[1])],
        }
        

