import random
from materials import Materials

class Box:
    id = 1
    def __init__(self, max_w : int,  type : Materials, w : int = 0) -> None:
        self.max_weight = max_w
        self.current_weight = w
        self.type = type
        Box.id += 1
    
    def fill_box(self) -> int:
        weight = self.max_weight / random.uniform(10, 20)
        self.current_weight += weight
        return (self.current_weight / self.max_weight) * 100

    def collect_box(self) -> None:
        self.current_weight = 0
    
    # def __str__(self):
    #     return f"Box_{Box.id}: [type: {self.type}, current_weight: {self.current_weight}], max_weight: {self.max_weight}"
    
    def to_dict(self):
        return {
            'id' : Box.id,
            'max_weight' : self.max_weight,
            'current_weight' : self.current_weight,
            'type' : self.type.value
        }