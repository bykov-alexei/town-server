from Config.field import FIELD_CONFIG

from Action import Wander, GoHome, GoWork
from Building import Building, Work, Home, Entertainment

from random import randint, choice


class Town:

    
    def __init__(self, token):
        self.token = token
    
        # self.buildings = [Home(randint(0, 15), randint(3, 13)) for i in range(2)] + [Work(randint(0, 15), randint(3, 13)) for i in range(2)] + [Entertainment(randint(0, 15), randint(3, 13)) for i in range(2)]  
        self.buildings = []
        self.people = []
        
        self.attraction = 0.5
        
        self.money = 0
        
        for person in self.people:
            self.find_home(person)
        
        
    def step(self):
        for person in self.people:
            self.find_home(person)
    
        for building in self.buildings:
            building.step()
            
            
    def settle(self, person):
        self.people.append(person)
        
        
    def move_out(self, person):
        self.people.remove(person)
        
    
    def get_actions(self):
        return [Wander, GoHome, GoWork]
        
    
    def get_available_homes(self):
        homes = []
        for building in self.buildings:
            if building.type == 'home' and building.taken_places < building.capacity:
                homes.append(building)
        return homes    
    
    
    def find_home(self, person):
        if person.home is not None:
            return
            
        homes = self.get_available_homes()
        if len(homes) == 0:
            return
        person.home = choice(homes)
        person.home.taken_places += 1
        # print(person.home)
        
        
        
    def object(self):
        return {
            'token': self.token,
            'config': {
                'max_x': FIELD_CONFIG['max_x'],
                'max_y': FIELD_CONFIG['max_y'],
                'max_building_x': FIELD_CONFIG['max_building_x'],
                'max_building_y': FIELD_CONFIG['max_building_y'],
            },
            'data': {
                'money': randint(0, 100),
                'attraction': randint(0, 100),
                'incomes': randint(0, 100),
                'expenses': randint(0, 100),
                'workload': randint(0, 100),
                'quarters': randint(0, 100),
            
                'buildings': [building.object() for building in self.buildings],
                'people': [person.object() for person in self.people],
            }
        }

