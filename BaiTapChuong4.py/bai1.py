from math import sqrt
print("Nhap vao 3 canh cua tam giac:")
a = float(input("Canh a > 0: "))
b = float(input("Canh b > 0: "))
c = float(input("Canh c > 0: "))
if (a <= 0 or b <= 0 or c <= 0) or (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Tam giac khong hop le")
else:
    cv = a + b + c
    p = cv / 2
    dt = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Dien tich cua tam giac: ", dt)
