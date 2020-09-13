class Action:


    def __init__(self):
        self.time = 0
        pass
 
 
    def do(self, person):
        
        pass
        
        
    def finish(self, person):
        person.action = None


    def get_weight(self, person):
        return 1
        

from .Wander import Wander
from .GoHome import GoHome
from .GoWork import GoWork
from .GoSomewhere import GoSomewhere
