import math

# Nhập số n
n = int(input("Nhập số dấu căn n: "))

# Tính S(n) = √(2 + √(2 + √(2 + ...)))
result = 0
for _ in range(n):
    result = math.sqrt(2 + result)

print(f"S({n}) = {result:.5f}")