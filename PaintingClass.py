from ItemListClass import ItemList
class Painting(ItemList):
    def __init__(self, id=None, value=None, creator=None,heightPaint=None,widthPaint=None,WaterColor=None,Frame=None):
        super().__init__(id, value, creator)
        self.__heightPaint=heightPaint
        self.__widthPaint=widthPaint
        self.__WaterColor=WaterColor
        self.__Frame=Frame
    @property
    def heightPaint(self):
        return self.__heightPaint
    @heightPaint.setter
    def heightPaint(self,heightPaint):
        self.__heightPaint=heightPaint
    @property
    def widthPaint(self):
        return self.__widthPaint
    @widthPaint.setter
    def widthPaint(self,widthPaint):
        self.__widthPaint=widthPaint
    @property
    def WaterColor(self):
        return self.__WaterColor
    @WaterColor.setter  
    def WaterColor(self,WaterColor):
        if WaterColor:
            print("The painting used to watercolor")
            
        else:
            print("The painting not used to watercolor")
        self.__WaterColor=WaterColor
    @property
    def Frame(self):
        return self.__Frame
    @Frame.setter
    def Frame(self,Frame):
        if Frame:
            print("The paint has frame")
        else:
            print("The frame dose not use frame ")
        self.__Frame=Frame
    def InputPaint(self):
        super().input()
        while True:
            self.__heightPaint=int(input("Enter paint height "))
            if 0<=self.__heightPaint:
                break
            else :
                print("The weight of vase must be gratter than 0 ")
        while True:
            self.__widthPaint=int(input("Enter paint width "))
            if self.__widthPaint >=0:
                break
            else :
                print("The width of vase must be gratter than 0 ")
        while True:
            frame_check=input('Dose the painting use frame (yes or no)').strip().lower()
            if frame_check == 'yes':
                self.__Frame=True
                break
            elif frame_check=='no':
                self.__Frame=False
                break
            else :
                print("Enter 'yes' or 'no',pls")
        while True:
            WaterColor_check=input('Dose the painting use watercolor (yes or no)').strip().lower()
            if WaterColor_check == 'yes':
                self.__WaterColor=True
                break
            elif WaterColor_check=='no':
                self.__WaterColor=False
                break
            else :
                print("Enter 'yes' or 'no',pls")
    def __str__(self):
        parents2=super().__str__()
        return f'{parents2} Height Paint : {self.heightPaint} Witdth Paint: {self.widthPaint} WaterColor: {self.WaterColor} Frame: {self.Frame}'
