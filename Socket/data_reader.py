from pymongo import MongoClient


def connect():
    conn = MongoClient().new_game
    return conn

def get_town(token):
    conn = connect()
    town = conn.towns.find_one({'token': str(token)})
    return town
    

def get_buildings(token):
    conn = connect()
    town = conn.towns.find_one({'token', str(token)})
    return town['buildings']


def get_people(token):
    town = get_town(str(token))['data']
    return {'people': town['people']}

def get_stats(token):
    town = get_town(token)['data']
    return {
        'attraction': town['attraction'],
        'incomes': town['incomes'],
        'expenses': town['expenses'],
        'workload': town['workload'],
        'money': town['money'],
        'quarters': town['quarters'],
    }


def get_terrain():
    conn = connect()
    terrain = conn.terrain.find_one({})['terrain']
    terrain = [{'line':[int(v) for v in line]} for line in terrain]  
    return terrain

