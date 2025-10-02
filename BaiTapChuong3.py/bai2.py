#dem so ngay trong thang
print("Chuong trinh dem so ngay trong thang")
month = int(input("Nhap thang can kiem tra: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Thang {month} co 31 ngay")
elif month in [4, 6, 9, 11]:
    print(f"Thang {month} co 30 ngay")
elif month == 2:
    year = int(input("Nhap nam can kiem tra: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Thang {month} co 29 ngay")
    else:
        print(f"Thang {month} co 28 ngay")
else:
    print("Thang khong hop le")
