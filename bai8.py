hang = int(input("Nhập số hàng: "))
cot = int(input("Nhập số cột: "))

for i in range(hang):
    for j in range(cot):
        if i == 0 or i == hang - 1 or j == 0 or j == cot - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
