# xac dinh quy trong nam
print("Chuong trinh xac dinh quy trong nam")
month = int(input("Nhap thang can kiem tra: "))
if month in [1, 2, 3]:
    print(f"Thang {month} thuoc quy 1")
elif month in [4, 5, 6]:
    print(f"Thang {month} thuoc quy 2")
elif month in [7, 8, 9]:
    print(f"Thang {month} thuoc quy 3")
elif month in [10, 11, 12]:
    print(f"Thang {month} thuoc quy 4")
else:
    print("Thang khong hop le")
    