import math
xA = int(input("Nhập xA: "))
yA = int(input("Nhập yA: "))
xB = int(input("Nhập xB: "))
yB = int(input("Nhập yB: "))
#DO DAI DOAN AB

AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
print("Độ dài đoạn AB là: ", AB)