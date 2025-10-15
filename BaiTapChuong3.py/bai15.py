'''

start: giá trị bắt đầu (nếu không ghi thì mặc định là 0)

stop: dừng trước giá trị này (không bao gồm stop)

step: bước nhảy (mặc định là 1)

### Giải thích :###
(a) range(5)
range(5)  →  [0, 1, 2, 3, 4]


➡ Mặc định start = 0, step = 1. Dừng trước 5.

(b) range(5, 10)
range(5, 10)  →  [5, 6, 7, 8, 9]


➡ Bắt đầu từ 5, dừng trước 10.

(c) range(5, 20, 3)
range(5, 20, 3)  →  [5, 8, 11, 14, 17]


➡ Tăng từ 5 đến trước 20, mỗi lần +3.

(d) range(20, 5, -1)
range(20, 5, -1)  →  [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]


➡ Giảm từ 20 đến lớn hơn 5, mỗi lần -1.

(e) range(20, 5, -3)
range(20, 5, -3)  →  [20, 17, 14, 11, 8]


➡ Giảm từ 20, mỗi lần -3, dừng trước nhỏ hơn hoặc bằng 5

(f) range(10, 5)
range(10, 5)  →  []


➡ Mặc định step = 1, nhưng 10 < 5 là sai chiều tăng ⟹ rỗng

(g) range(0)
range(0)  →  []


➡ Không có số nào từ 0 đến trước 0 ⟹ rỗng

(h) range(10, 101, 10)
range(10, 101, 10) → [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


➡ Bắt đầu từ 10 đến 100, mỗi lần +10

(i) range(10, -1, -1)
range(10, -1, -1) → [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


➡ Giảm từ 10 đến 0, dừng trước -1

(j) range(-3, 4)
range(-3, 4) → [-3, -2, -1, 0, 1, 2, 3]


➡ Tăng từ -3 đến trước 4, mặc định step = 1

(k) range(0, 10, 1)
range(0, 10, 1) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


➡ Tăng từ 0 đến trước 10, bước nhảy 1range(10, 5)  →  []


➡ Mặc định step = 1, nhưng 10 < 5 là sai chiều tăng ⟹ rỗng

(g) range(0)
range(0)  →  []


➡ Không có số nào từ 0 đến trước 0 ⟹ rỗng

(h) range(10, 101, 10)
range(10, 101, 10) → [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


➡ Bắt đầu từ 10 đến 100, mỗi lần +10

(i) range(10, -1, -1)
range(10, -1, -1) → [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


➡ Giảm từ 10 đến 0, dừng trước -1

(j) range(-3, 4)
range(-3, 4) → [-3, -2, -1, 0, 1, 2, 3]


➡ Tăng từ -3 đến trước 4, mặc định step = 1

(k) range(0, 10, 1)
range(0, 10, 1) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


➡ Tăng từ 0 đến trước 10, bước nhảy 1
'''