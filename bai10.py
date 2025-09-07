
max_cot = 11                   
hang_widths = [1, 3, 7, 3, 5, 11]


duoi_cao = 2                   
khoang_trong_giua = 1           

# ===== HÀM TIỆN ÍCH =====
def print_center(s: str):
    space = (max_cot - len(s)) // 2
    print(" " * space + s)

# ===== IN PHẦN LÁ =====
for w in hang_widths:
    dong = "*" * w
    print_center(dong)

# ===== IN PHẦN ĐUÔI "* *" =====
duoi_mot_hang = "*" + " " * khoang_trong_giua + "*"

for _ in range(duoi_cao):
    print_center(duoi_mot_hang)
    
    
