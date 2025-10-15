#cau11
def sum1(a):
    s = 0
    while a > 0:
        s += a
        a -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s
#TRUONG HOP 1
def main():
    global val
    val = 5
    print("Kết quả sum1(5):", sum1(5))  # Tính tổng từ 1 đến 5
    print("Kết quả sum2():", sum2())    # Đếm số lần giảm val từ 5 về 0
    print("Kết quả sum3():", sum3())    # Dùng val hiện tại (đã bị giảm về 0)
    print("Giá trị cuối của val:", val) # Kiểm tra giá trị val sau khi gọi sum2

main()


#TRUONG HOP 2
def main():
    global val
    val = 5
    print("Kết quả sum1(5):", sum1(5))  # Tính tổng từ 1 đến 5
    print("Kết quả sum2():", sum2())    # Dùng val hiện tại (đã bị giảm về 0)
    print("Kết quả sum3():", sum3())    # Đếm số lần giảm val từ 5 về 0
main()
#TRUONG HOP 3
def main():
    global val
    val = 5
    print("Kết quả sum1():", sum1())
    print("Kết quả sum2(5):", sum2(5))
    print("Kết quả sum3():", sum3())
main()