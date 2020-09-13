from . import Query


import Building


class PutBuilding(Query):
    
    
    def __init__(self, token, building):
        self.token = token
        self.building = building
        
    
    def perform(self, town):
        print(self.building)
        x, y = self.building['position']
        building = Building.Building(x, y)
        if self.building['type'] == 'home':
            building = Building.Home(x, y)
        elif self.building['type'] == 'work':
            building = Building.Work(x, y)
        elif self.building['type'] == 'entertainment':
            building = Building.Entertainment(x, y)
        town.money -= building.construction_cost
        town.buildings.append(building)
        
