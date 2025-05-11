from box import Box
import uuid

class GlobalBox:
    def __init__(self, c : int, box_list : list[Box]):
        self.id = uuid.uuid4().int
        self.capacity = c
        if len(box_list) <= c:
            self.list_box = box_list
        else:
            raise Exception(f"box list length should not exceed maximum capacity of {c}.")
    
    def add_box(self, box : Box) -> None:
        if len(self.list_box) < self.capacity:
            self.list_box.append(box)
        else:
            raise Exception(f"Exceeded maximum capacity({self.capacity}) of GlobalBox.")

    def remove_box(self, box: Box) -> None:
        if len(self.list_box) == 0:
            self.list_box.pop(self.list_box.index(box))
        else:
            raise Exception("GlobalBox does not contain any boxes.")
    
    def to_dict(self):
        return {
            'id' : self.id,
            'capacity' : self.capacity,
            'list_box' : [box.to_dict() for box in self.list_box]
        }