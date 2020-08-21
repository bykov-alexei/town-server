import socketserver
import json

from data_reader import get_people, get_town, get_terrain, get_stats

from pymongo import MongoClient

class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = json.loads(self.request.recv(1024))
        self.action = self.data['action']
        self.route()
        self.reply()

    def route(self):
        print('action ', self.data['action'])
        if self.data['action'] == 'get_town':
            town = get_town(self.data['token'])
            del town['data']['people']
            self.response = json.dumps(town)
        elif self.data['action'] == 'get_people':
            self.response = json.dumps(get_people(self.data['token']))
        elif self.data['action'] == 'get_terrain':
            self.response = json.dumps({'data': get_terrain()})
        elif self.data['action'] == 'get_stats':
            self.response = json.dumps(get_stats(self.data['token']))
        elif self.data['action'] == 'put_building':
            print(self.data)
            db = MongoClient().new_game.put_building.insert_one(self.data)
            self.response = json.dumps({})
        elif self.data['action'] == 'delete_building':
            db = MongoClient().new_game.delete_building.insert_one(self.data)
            self.response = json.dumps({})
        elif self.data['action'] == 'clear_buildings':
            db = MongoClient().new_game.clear_buildings.insert_one(self.data)
            self.response = json.dumps({})
        else:
            self.response = json.dumps({})

    def reply(self):
        self.send_message(self.response)

    def send_message(self, message):
        print(message)
        self.request.send(bytes(message, encoding='utf-8'))

host, port = "", 10000

server = socketserver.TCPServer((host, port), Handler)
server.serve_forever()
