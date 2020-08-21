from . import Query


class ClearBuildings(Query):
    
    
    def __init__(self, token):
        self.token = token

    def perform(self, town):
        town.buildings = []
