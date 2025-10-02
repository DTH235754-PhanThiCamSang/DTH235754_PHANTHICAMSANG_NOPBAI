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