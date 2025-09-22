#Kiem Tra Nam Nhuan
print("Chuong trinh kiem tra nam nhuan ")
year = int(input("Nhap nam can kiem tra: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} la nam nhuan")
else:
    print(f"{year} khong phai la nam nhuan")