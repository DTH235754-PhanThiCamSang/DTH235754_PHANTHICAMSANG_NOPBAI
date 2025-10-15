n = int(input("Nhap n: "))
r = n 
def hinh_A(n):
    
    # hàng trên
    print("* " * r)
    # các hàng giữa
    for _ in range(n-2):
        if r <= 1:
            print("*")
        else:
            print("* " + "  " * (r-2) + "*")
    # in hàng đáy 
    print("* " * r)
def hinh_B(n):
    
    for i in range(1, n + 1):
        spaces = "  " * (n - i)   
        stars  = "* " * i
        print(spaces + stars)




if __name__ == "__main__":
 
    print("Hình A:")
    hinh_A(n)
    print("\nHình B:")
    hinh_B(n)
   