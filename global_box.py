from box import Box

class GlobalBox:
    id = 1
    def __init__(self, c : int, box_list : list[Box]):
        self.capacity = c
        if len(box_list) <= c:
            self.list_box = box_list
        else:
            raise Exception(f"box list length should not exceed maximum capacity of {c}.")
        GlobalBox.id += 1
    
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
        
    # def __str__(self):
    #     return f"GlobalBox_{GlobalBox.id}: [capacity: {self.capacity}, list_box: {self.list_box}]"
    
    def to_dict(self):
        return {
            'id' : GlobalBox.id,
            'capacity' : self.capacity,
            'list_box' : [box.to_dict() for box in self.list_box]
        }