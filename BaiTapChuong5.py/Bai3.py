#xu ly tach chuoi
def CheckPrime(x):
    dem =0
    for i in range(1,x+1):
        if x % i ==0:
            dem +=1
    return dem ==2
s= "5; 7; -8; 21; 13; 15; 17"
arr = s.split(";")
sochan =0
soam  =0
sont=0
sum =0
for x in arr:
    print(x.strip())
    number = int(x.strip())
    if number % 2 ==0:
        sochan +=1
    if number <0:
        soam +=1
    if CheckPrime(number):
        sont +=1
    sum += number
print("So chan:",sochan)
print("So am:",soam)
print("So nguyen to:",sont)
print("Tong cac so:",sum)
print("Trung binh cong:",sum/len(arr)) 