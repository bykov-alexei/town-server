from pymongo import MongoClient


class Query:


    def __init__(self):
        pass
        
        
    def perform(self, town):
        pass


from .PutBuilding import PutBuilding
from .ClearBuildings import ClearBuildings
from .DeleteBuilding import DeleteBuilding

def get_queries():
    conn = MongoClient().new_game
    
    queries = []
    
    put_building_table = conn.put_building
    put_buildings = put_building_table.find({})
    for query in put_buildings:
        token = query['token']
        building = query['building']
        
        put_building = PutBuilding(token, building)
        queries.append(put_building)
    
    delete_building_table = conn.delete_building
    delete_buildings = delete_building_table.find({})
    for query in delete_buildings:
        token = query['token']
        
        delete_building_q = DeleteBuilding(token)
        queries.append(delete_building_q) 
    
    clear_buildings_table = conn.clear_buildings
    clear_buildings = clear_buildings_table.find({})
    for query in clear_buildings:
        token = query['token']
        
        clear_buildings_q = ClearBuildings(token)
        queries.append(clear_buildings_q)
    
    return queries

