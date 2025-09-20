# Một số cách nhập dữ liệu từ bàn phím trong Python

# 1. Sử dụng hàm input() để nhập chuỗi
name = input("Nhập họ và tên của bạn: ")
print("Tên bạn là:", name)

# 2. Nhập số nguyên và chuyển kiểu dữ liệu
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là:", age)

# 3. Nhập số thực và chuyển kiểu dữ liệu
height = float(input("Nhập chiều cao của bạn (m): "))
print("Chiều cao của bạn là:", height)

# 4. Nhập nhiều giá trị trên một dòng và tách bằng split()
a, b = input("Nhập hai số, cách nhau bởi dấu cách: ").split()
print("Số thứ nhất:", a)
print("Số thứ hai:", b)

# 5. Nhập nhiều số và chuyển sang kiểu số nguyên
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
print("Danh sách các số vừa nhập:", numbers)