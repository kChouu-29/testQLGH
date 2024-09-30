from ManageItem import Manage
from VaseClass import Vase  # Import lớp Vase để tạo đối tượng
from StatueClass import Statue
from PaintingClass import Painting
import os
import time
def main():
    # Tạo đối tượng của lớp Manage
    manage = Manage()
    
    while True:
        print("\nMenu:")
        print("1.Add a new vase")
        print("2.Add a new statue")
        print("3.Add a new painting")
        print("4.Display all item")
        print("5.Find the items by creator")
        print("6.Display the list of vase items")
        print("0.Out programming")

        try:
            m = int(input("Enter your choice: "))
        except ValueError:
            print("You must press a number valid ,pls.")
            continue

        match m:
            case 1:
                new_vase = Vase()  # Tạo một đối tượng Vase mới
                new_vase.inputVase()  # Nhập dữ liệu cho Vase
                manage.add_vase(new_vase)  # Thêm Vase vào danh sách quản lý
            case 6:
                manage.show_vase()  # Hiển thị các Vase
            case 2:
                # Tạo một đối tượng Statue tương tự như cách làm với Vase
                # manage.add_statue()  # Thêm một Statue mới
                new_statue = Statue()
                new_statue.inputStatue()
                manage.add_statue(new_statue)
                pass
            case 3:
                new_paiting=Painting()
                new_paiting.InputPaint()
                manage.add_painting(new_paiting)
            case 4:
                manage.show_all()  # Hiển thị tất cả các item
            case 5:
                Search_Id=input("Enter the place of production you want to search for: ").upper()
                if manage.dsItem == []:
                    print("The list items empty")
                for i in range(len(manage.dsItem)):
                    if(Search_Id==manage.dsItem[i].creator):
                        print(manage.dsItem[i])
                    else:
                        print("The production location you just entered does not exist.")
                        break
            case 0:
                print("Log out programming.")
                break  # Thoát khỏi vòng lặp và kết thúc chương trình
            case _:
                print("Your choice not valid.pls return choice")

if __name__ == "__main__":
    main()
