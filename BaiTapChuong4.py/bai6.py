import random

# Các giá trị cần kiểm tra
gtriKT = [4.5, 34, -1, 100, 0, 99]

# Tập giá trị có thể xuất hiện
rd = list(range(0, 100))  # randrange(0, 100) tạo số nguyên từ 0 đến 99

# Kiểm tra từng giá trị
for value in gtriKT:
    if value in rd:
        print(f"{value} có thể xuất hiện trong randrange(0, 100)")
    else:
        print(f"{value} không thể xuất hiện trong randrange(0, 100)")