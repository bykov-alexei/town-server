from Config.game import GAME_CONFIG

from Person import Person
from Town import Town
from Query import get_queries

import time
from pymongo import MongoClient
from uuid import uuid4 as uuid


class Game:


    def __init__(self):
        self.clear_db()

        self.tokens = [str(i) for i in range(1, GAME_CONFIG['town_number'] + 1)]
        self.towns = {token: Town(token) for token in self.tokens}
        self.people = [Person(i) for i in range(GAME_CONFIG['people_number'])]
        
        self.terrain = None
        
        self.make_terrain()
        self.settle(self.people)

        
    def step(self):
        print(list(self.towns.values())[0].get_timestring())
    
        start = time.time()
        
        self.do_queries()
        for town in self.towns.values():
            town.step()
        for person in self.people:
            person.step()
        self.save_state()
        
        end = time.time()
        delta = end - start
        if delta < GAME_CONFIG['step_real_time']:
            time.sleep(GAME_CONFIG['step_real_time'] - delta)
       
    def do_queries(self):
        queries = get_queries()
        for query in queries:
            query.perform(self.towns[str(query.token)])
        
        db = MongoClient().new_game
        db.delete_building.delete_many({})
        db.put_building.delete_many({})
        db.clear_buildings.delete_many({})

    def clear_db(self):
        db = MongoClient().new_game
        towns_table = db.towns
        towns_table.delete_many({})

    def save_state(self):
        db = MongoClient().new_game
            
        towns_table = db.towns
        for town in self.towns.values():
            obj = town.object()
            obj['_id'] = str(uuid())
            towns_table.insert_one(obj)
    
    
    def settle(self, people):
        for person in people:
            person.change_town(list(self.towns.values()))
            
    
    def make_terrain(self):
        self.terrain = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        MongoClient().new_game.terrain.insert_one({'terrain': self.terrain})

 
