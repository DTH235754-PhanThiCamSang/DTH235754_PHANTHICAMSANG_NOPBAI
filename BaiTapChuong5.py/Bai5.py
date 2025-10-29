#chuong trinh nhap vào mot chuoi
def NhapChuoi():
    s = input("Nhap 1 chuoi: ")
    return s
#bao nhieu chu in hoa
def DemChuInHoa(s):
    dem =0
    for i in range (len(s)):
        if s[i].isupper():
            dem +=1
    return dem
#bao nhieu chu in thuong
def DemChuInThuong(s):
    dem =0
    for i in range (len(s)):
        if s[i].islower():
            dem +=1
    return dem
# bao nhiue chu la chu so
def DemChuSo(s):
    dem =0
    for i in range (len(s)):
        if s[i].isdigit():
            dem +=1
    return dem
# bao nhieu lá kí tự dac biet
def DemChuDacBiet(s):
    dem =0
    for i in range (len(s)):
        if not s[i].isalnum() and not s[i].isspace():
            dem +=1
    return dem
# bao nhieu tu la khoang trang
def DemTuKhoangTrang(s):
    dem =0
    for i in range (len(s)):
        if s[i].isspace():
            dem +=1
    return dem
# bao nhieu chu la nguyen am
def DemChuNguyenAm(s):
    dem =0
    nguyenam = "aAeEiIoOuUyY"
    for i in range (len(s)):
        if s[i] in nguyenam:
            dem +=1
    return dem
#bao nhieu chu la phu am
def DemChuPhuAm(s):
    dem =0
    phuam = "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXzZ"
    for i in range (len(s)):
        if s[i] in phuam:
            dem +=1
    return dem
def main():
    s = NhapChuoi()
    print("So chu in hoa:",DemChuInHoa(s))
    print("So chu in thuong:",DemChuInThuong(s))
    print("So chu so:",DemChuSo(s))
    print("So chu dac biet:",DemChuDacBiet(s))
    print("So tu khoang trang:",DemTuKhoangTrang(s))
    print("So chu nguyen am:",DemChuNguyenAm(s))
    print("So chu phu am:",DemChuPhuAm(s))
while True:
    main()
    print("Tiep khong ban (y/n)?")
    s = input()
    if s == "n":
        break