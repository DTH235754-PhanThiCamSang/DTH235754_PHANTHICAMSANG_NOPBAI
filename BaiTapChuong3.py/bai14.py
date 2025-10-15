#co biet bao nhieu dau sao duoc in ra man hinh
print("Chuong trinh co biet bao nhieu dau sao duoc in ra man hinh")
a=0
while a < 100:
    b=0
    while b < 40:
        if(a+b)%2==0:
            print("*", end="")
        b+=1
    print()
    a+=1
print()
'''
Dieu Kien: if(a+b)%2==0:

Chỉ in * nếu tổng a + b là số chẵn

Tổng số giá trị b mỗi vòng = 40

Trong 40 số liên tiếp, sẽ có 20 số chẵn và 20 số lẻ

⟹ Mỗi dòng sẽ in đúng 20 dấu *

Có 100 dòng như vậy → mỗi dòng 20 dấu *
'''