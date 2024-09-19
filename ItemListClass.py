# ItemListClass.py

class ItemList:


    def __init__(self, id=None, value=None, creator=None):
        self._id = id
        self._value = value
        self._creator = creator

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
         self._id = id

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
    
        self._value = value

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, creator):

        self._creator = creator

    def input(self):
        # Nhập thông tin cho ItemList
        while True:
            self._id = input("Enter ID: ")
            if self._id:
                break
            else:
                print("ID cannot be empty.")

        while True:
            try:
                self._value = int(input("Enter Value: "))
                if self._value >= 0:
                    break
                else:
                    print("Value must be >= 0.")
            except ValueError:
                print("Invalid input. Please enter a positive integer for value.")

        while True:
            self._creator = input("Enter Creator: ")
            if self._creator != "":
                break
            else:
                print("Creator cannot be empty.")

