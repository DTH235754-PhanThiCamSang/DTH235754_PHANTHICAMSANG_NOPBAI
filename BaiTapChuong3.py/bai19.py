import math
n = int(input("Nhap n: "))
x = int(input("Nhap x: "))
def series_s(x: int, n: int) -> float:
    if n < 0:
        raise ValueError("n phải là số nguyên không âm")
    term = x          
    s = term
    for k in range(1, n + 1):
        term *= (x * x) / ( (2*k) * (2*k + 1) )
        s += term
    return s
print(f"S({x}, {n}) = {series_s(x, n)}")