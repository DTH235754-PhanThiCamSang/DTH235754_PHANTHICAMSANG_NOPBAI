#trích lục số âm trong chuoi
import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các chuỗi có dạng -<số>
    # (?<!-) để đảm bảo không có dấu '-' trước đó (tránh trường hợp '--5')
    nums = re.findall(r'(?<!-)-\d+', s)
    
    if nums:
        print("Các số nguyên âm trong chuỗi là:")
        for n in nums:
            print(n)
    else:
        print("Không có số nguyên âm nào trong chuỗi.")
def main():
    print("Nhập chuỗi :")
    s = input()
    NegativeNumberInStrings(s)

if __name__ == "__main__":
    main()