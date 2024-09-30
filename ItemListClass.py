# ItemListClass.py

class ItemList:


    def __init__(self, id=None, value=None, creator=None):
        self.__id = id
        self.__value = value
        self.__creator = creator
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
         self.__id = id

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
    
        self.__value = value

    @property
    def creator(self):
        return self.__creator

    @creator.setter
    def creator(self, creator):

        self.__creator = creator

    def input(self):
        # Nhập thông tin cho ItemList
        while True:
            self.__id = input("Enter ID: ")
            if self.__id:
                break
            else:
                print("ID cannot be empty.")

        while True:
            try:
                self.__value = int(input("Enter Value: "))
                if self.__value >= 0:
                    break
                else:
                    print("Value must be >= 0.")
            except ValueError:
                print("Invalid input. Please enter a positive integer for value.")

        while True:
            self.__creator = input("Enter Creator: ").upper()
            if self.__creator != "":
                break
            else:
                print("Creator cannot be empty.")
    def __str__(self) :
        return f"ID:{self.__id} Value:{self.__value} Creator:{self.__creator}"
