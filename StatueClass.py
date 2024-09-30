from ItemListClass import ItemList
class Statue(ItemList):
    def __init__(self, id=None, value=None, creator=None,heightStatue=None,colorStatue=None):
        super().__init__(id, value, creator)
        self.__heightStatue=heightStatue
        self.__colorStatue=colorStatue
    @property
    def heightStatue(self):
        return self.__heightStatue
    @heightStatue.setter
    def heightStatue(self,heightStatue):
        self.__heightStatue=heightStatue
    @property
    def colorStatue(self):
        return self.__colorStatue
    @colorStatue.setter
    def colorStatue(self,colorStatue):
        self.__colorStatue=colorStatue
    def inputStatue(self):
        super().input()
        while True:
            self.__heightStatue=int(input("Enter height statue "))
            if self.__heightStatue >=0:
                break
            else :
                print("The height of statue cannot be less than 0")
        while True:
            self.__colorStatue=input("Enter the color of statue ")
            if self.__heightStatue !="":
                break
            else :
                print("The color of statue can not empty")
    def __str__(self):
        parents=super().__str__()
        return f'{parents} Height Statue : {self.heightStatue} Color Statue: {self.colorStatue}'