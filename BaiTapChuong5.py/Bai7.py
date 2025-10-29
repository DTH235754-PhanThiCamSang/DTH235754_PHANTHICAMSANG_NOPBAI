#toi uu hoa chuoi danh tu
def ToiUuHoaChuoiDanhTu(s):
    s2 =s;
    s2 = s2.strip() #loai bo khoang trang dau va cuoi
    arr = s2.split(' ') #tach chuoi thanh mang cac tu
    s2 = "" 
    for x in arr:
        word = x
        if len(word.strip()) != 0: #kiem tra tu khong rong
            #viet hoa chu cai dau tien cua tu
            word = word.strip()
            word = word[0].upper() + word[1:].lower()
            s2 = s2 + word + " " #noi cac tu lai voi nhau bo khoang trang thua
    return s2.strip() #loai bo khoang trang cuoi cung neu co
s ="tran    duy      THANH "
print("Input:",s)
s = ToiUuHoaChuoiDanhTu(s)
print("Output:",s)