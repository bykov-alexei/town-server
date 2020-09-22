from Config.field import FIELD_CONFIG
from Config.game import GAME_CONFIG

from Action import Wander, GoHome, GoWork
from Building import Building, Work, Home, Entertainment

from random import randint, choice
from datetime import datetime

class Town:

    
    def __init__(self, token):
        self.token = token
        
        
        # time
        self.i = 0
        self.time = GAME_CONFIG['start_time']
        self.timedelta = 3600 * 24 // GAME_CONFIG['steps_in_day']
    
        self.buildings = [Home(randint(0, 15), randint(3, 13)) for i in range(3)] + [Work(randint(0, 15), randint(3, 13)) for i in range(2)] + [Entertainment(randint(0, 15), randint(3, 13)) for i in range(2)]  
        self.people = []
        
        self.attraction = 0.5
        
        self.money = 0
        
        
    def step(self):
        # Time
        self.i = self.i + 1
        self.time += self.timedelta
    
        # Money
        income = self.get_incomes()
        expenses = self.get_expenses()
        self.money += income
        self.money -= expenses

        # Attraction
        self.calc_attraction()

        # Settlement
        for person in self.people:
            self.schedule(person)
            person.step()
            self.find_home(person)
            self.find_work(person)
    
        # Building steps
        for building in self.buildings:
            building.step()

    def schedule(self, person):
        date = self.get_date()
        if date.hour >= 0 and date.hour <= 8:
            if type(person.action) != GoHome:
                person.action = GoHome()
        elif date.hour >= 8 and date.hour <= 12:
            if type(person.action) != GoWork:
                person.action = GoWork()
        elif date.hour >= 13 and date.hour <= 17:
            if type(person.action) != GoWork:
                person.action = GoWork()
        return
    
    def calc_attraction(self):
        happinesses = []
        for person in self.people:
            happinesses.append(person.happiness)
        self.attraction = sum(happinesses) / len(happinesses)
          
            
    # 
    # Town settlement
    #
            
            
    def settle(self, person):
        self.people.append(person)
        
        
    def move_out(self, person):
        self.people.remove(person)
        
        
    #
    # Home settlement
    #  
    
    
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
        
        
    #
    # Work search
    # 
     
     
    def get_available_works(self):
        works = []
        for building in self.buildings:
            if building.type == 'work' and building.taken_places < building.work_places:
                works.append(building)
        return works
        
        
    def find_work(self, person):
        if person.work_place is not None:
            return
            
        works = self.get_available_works()
        if len(works) == 0:
            return
        person.work_place = choice(works)
        person.work_place.taken_places += 1    
    
        
    #
    # Getters
    #
   
        
    def object(self):
        return {
            'token': self.token,
            'i': self.i,
            'config': {
                'max_x': FIELD_CONFIG['max_x'],
                'max_y': FIELD_CONFIG['max_y'],
                'max_building_x': FIELD_CONFIG['max_building_x'],
                'max_building_y': FIELD_CONFIG['max_building_y'],
            },
            'data': {
                'money': self.get_money(),
                'attraction': self.get_attraction(),
                'incomes': self.get_incomes(),
                'expenses': self.get_expenses(),
                'workload': self.get_workload(),
                'quarters': self.get_quarters(),
                'time': self.get_timestring(),
            
                'buildings': [building.object() for building in self.buildings],
                'people': [person.object() for person in self.people],
            }
        }
     
        
    def get_money(self):
        return self.money
        
    
    def get_attraction(self):
        return self.attraction
        
    
    def get_incomes(self):
        income = 0
        for building in self.buildings:
            income += building.income
        return income
        
        
    def get_expenses(self):
        expenses = 0
        for building in self.buildings:
            expenses += building.maintenance_cost
        return expenses
        
        
    def get_workload(self):
        return len(self.people)
        
        
    def get_quarters(self):
        quarters = 0
        for building in self.buildings:
            if building.type == 'home':
                quarters += building.capacity
        return quarters
    
        
    def get_actions(self):
        return [Wander, GoHome]
        
    
    def get_date(self):
        return datetime.fromtimestamp(self.time)    
    
    
    def get_timestring(self):
        date = self.get_date()
        return '%02d:%02d' % (date.hour, date.minute)
                 

