import random
from materials import Materials
import uuid

class Box:
    def __init__(self, max_w : int,  type : Materials, w : int = 0) -> None:
        self.id = uuid.uuid4().int
        self.max_weight = max_w
        self.current_weight = w
        self.type = type
    
    def fill_box(self) -> int:
        weight = round(self.max_weight / random.randint(10, 20), 2)
        self.current_weight += weight
        return round((self.current_weight / self.max_weight) * 100, 2)

    def collect_box(self) -> None:
        self.current_weight = 0
    
    def to_dict(self) -> dict:
        return {
            'id' : self.id,
            'max_weight' : self.max_weight,
            'current_weight' : self.current_weight,
            'type' : self.type.value
        }