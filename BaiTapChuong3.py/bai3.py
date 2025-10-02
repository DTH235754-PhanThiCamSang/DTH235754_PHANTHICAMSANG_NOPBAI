#phuong trinh bac hai
from math import sqrt

print("Chuong trinh giai phuong trinh bac hai ax^2 + bx + c = 0")
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x = -c / b
        print(f"Phuong trinh co mot nghiem x = {x}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phuong trinh co nghiem kep x1 = x2 = {x}")
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f"Phuong trinh co hai nghiem phan biet x1 = {x1}, x2 = {x2}")
