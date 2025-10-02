a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
toantu = input("Nhap toan tu (+, -, *, /): ")
if toantu not in ['+', '-', '*', '/']:
    print("Toan tu khong hop le")
    exit()
elif b == 0 and toantu == '/':
    print("Khong the chia cho 0")
    exit()
elif toantu == '+':
    c = a + b
    print(f"{a} + {b} = {c}")
elif toantu == '-':
    d= a - b
    print(f"{a} - {b} = {d}")
elif toantu == '*':
    e = a * b
    print(f"{a} * {b} = {e}")
elif toantu == '/':
    f = a / b
    print(f"{a} / {b} = {f}")
    '''
#phep cong
c = a + b
print(f"{a} + {b} = {c}")
#phep tru
d= a - b
print(f"{a} - {b} = {d}")
#phep nhan
e = a * b
print(f"{a} * {b} = {e}")
#phep chia

f = a / b
print(f"{a} / {b} = {f}")
'''