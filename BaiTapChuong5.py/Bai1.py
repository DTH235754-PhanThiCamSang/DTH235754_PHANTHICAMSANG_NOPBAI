# Kiem tra chuoi doi xung
def CheckDoiXung(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            flag = False
            break
    return flag
def main():
    s = input("Nhap 1 chuoi: ")
    if CheckDoiXung(s):
        print("Chuoi doi xung")
    else:
        print("Chuoi khong doi xung")
while True:
    main()
    print("Tiep khong ban (y/n)?")
    s = input()
    if s == "n":
        break
print("Bye bye")