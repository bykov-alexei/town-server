from Config.field import FIELD_CONFIG
from Config.building import BUILDING_CONFIG

from . import Building


class Work(Building):

    def __init__(self, x, y):
        super(Work, self).__init__(x, y)
        
        self.type = 'work'
        self.work_places = BUILDING_CONFIG[self.type]['work_places']
        self.construction_cost = BUILDING_CONFIG[self.type]['construction_cost']
        self.maintenance_cost = BUILDING_CONFIG[self.type]['maintenance_cost']
        self.income = BUILDING_CONFIG[self.type]['income']
        
        self.taken_places = 0
        
    
    def step(self):
        pass
        
        
    def object(self):
        return {
            'type': self.type,
            'position': [int(self.position[0]), int(self.position[1])],
        }
        

