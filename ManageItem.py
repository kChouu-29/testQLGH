from VaseClass import Vase
from PaintingClass import Painting
from StatueClass import Statue
class Manage:
    def __init__(self):
        self.dsItem = []
        self.dsVase = []

    def add_vase(self, vase):
        self.dsVase.append(vase)
        self.dsItem.append(vase)
        print("Vase added successfully")

    def add_painting(self, painting):
        self.dsItem.append(painting)
        print("Painting added successfully")

    def add_statue(self, statue):
        self.dsItem.append(statue)
        print("Statue added successfully")

    def show_vase(self):
        if self.dsVase:
            for vase in self.dsVase:
                print(vase)
        else:
            print("No vases available")

    def show_all(self):
        if self.dsItem:
            for item in self.dsItem:
                print(item)
        else:
            print("No items available")

