from Config.game import GAME_CONFIG

from Person import Person
from Town import Town
from Query import get_queries


from pymongo import MongoClient


class Game:


    def __init__(self):
        self.tokens = [str(i) for i in range(1, GAME_CONFIG['town_number'] + 1)]
        self.towns = {token: Town(token) for token in self.tokens}
        self.people = [Person(i) for i in range(GAME_CONFIG['people_number'])]
        
        self.make_terrain()
        self.settle(self.people)

        
    def step(self):
        self.do_queries()
        
        for town in self.towns.values():
            town.step()
        
        for person in self.people:
            person.step()
            
        self.save_state()
    
        
    def do_queries(self):
        queries = get_queries()
        # print(queries)
        for query in queries:
            query.perform(self.towns[str(query.token)])
        
        db = MongoClient().new_game
        db.delete_building.delete_many({})
        db.put_building.delete_many({})
        db.clear_buildings.delete_many({})
        

    def save_state(self):
        db = MongoClient().new_game
            
        towns_table = db.towns
        towns_table.delete_many({})
        for town in self.towns.values():
            obj = town.object()
            obj['_id'] = town.token
            towns_table.insert_one(obj)
    
    
    def settle(self, people):
        for person in people:
            person.change_town(list(self.towns.values()))
            
    
    def make_terrain(self):
        terrain = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2],
                [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],]
        MongoClient().new_game.terrain.insert_one({'terrain': terrain})

 
