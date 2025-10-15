import math

# Nhập giá trị a và x
a = float(input("Nhập cơ số a (a > 0, a ≠ 1): "))
x = float(input("Nhập số x (x > 0): "))

# Kiểm tra điều kiện
if a > 0 and a != 1 and x > 0:
    log_ax = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {log_ax:.5f}")
else:
    print("Giá trị không hợp lệ. Yêu cầu: x > 0, a > 0, a ≠ 1.")