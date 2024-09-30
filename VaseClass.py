# vase.py

from ItemListClass import ItemList  # Nhập lớp ItemList từ file ItemListClass.py



class Vase(ItemList):
    def __init__(self, id=None, value=None, creator=None, height=None, material=None):
        super().__init__(id, value, creator)  # Khởi tạo các thuộc tính từ lớp cha
        self.__height = height
        self.__material = material

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        if material != "":
            self.__material = material

    def inputVase(self):
        super().input()  # Gọi phương thức input của lớp cha

        # Nhập thông tin cho lớp con
        while True:
            try:
                self.__height = int(input("Enter vase height: "))
                if self.__height > 0:
                    break
                else:
                    print("Vase height must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter an integer value for height.")

        while True:
            self.__material = input("Enter vase material: ")
            if self.__material != "":
                break
            else:
                print("Material cannot be empty.")

    def __str__(self):
        # Gọi phương thức __str__ của lớp cha và thêm thuộc tính riêng của Vase
        parent_str = super().__str__()
        return f"{parent_str}, Height: {self.__height}, Material: {self.__material}"


# # Quản lý danh sách các bình hoa (Vase)
# dsVase1 = []

# new_vase = Vase()
# new_vase.inputVase()
# dsVase1.append(new_vase)

# # Hiển thị thông tin bình hoa
# for vase in dsVase1:
#     print(vase)
