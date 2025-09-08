# Ý nghĩa các toán tử trong Python

# / : Chia lấy kết quả là số thực (float)
a = 7 / 2    # Kết quả: 3.5

# // : Chia lấy phần nguyên (floor division)
b = 7 // 2   # Kết quả: 3

# % : Lấy phần dư của phép chia (modulo)
c = 7 % 2    # Kết quả: 1

# ** : Lũy thừa (power)
d = 2 ** 3   # Kết quả: 8

# and : Toán tử logic AND (cả hai điều kiện đều đúng)
e = (a > 3) and (b < 4)   # Kết quả: True

# or : Toán tử logic OR (một trong hai điều kiện đúng)
f = (a > 3) or (b > 4)    # Kết quả: True

# is : So sánh đối tượng (kiểm tra hai biến có cùng tham chiếu không)
x = [1, 2]
y = x
z = [1, 2]
g = (x is y)   # Kết quả: True
h = (x is z)   # Kết quả: False

# In kết quả
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
print("f =", f)
print("g =", g)
print("h =", h)

