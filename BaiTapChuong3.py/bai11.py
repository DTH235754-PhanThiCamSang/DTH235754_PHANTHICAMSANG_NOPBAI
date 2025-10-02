#kien tra so nguyen to
print("Chuong trinh kiem tra so nguyen to")
while True:
    n = int(input("Nhap so nguyen duong n: "))
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    if dem==2:
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} khong phai la so nguyen to")
    hoi = input("Ban co muon kiem tra tiep khong (y/n)? ")
    if hoi.lower() != 'y':
        break
print("Cam on ban da su dung chuong trinh")
