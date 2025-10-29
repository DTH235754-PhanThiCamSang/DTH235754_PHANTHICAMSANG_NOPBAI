#chuong trinh toi uu chuoi
def ToiUuChuoi(s):
    s2 =s;
    s2 = s2.strip() #loai bo khoang trang dau va cuoi
    arr = s2.split(' ') #tach chuoi thanh mang cac tu
    s2 = "" 
    for x in arr:
        word = x
        if len(word.strip()) != 0: #kiem tra tu khong rong
            s2 = s2 + word.strip() + " " #noi cac tu lai voi nhau bo khoang trang thua
    return s2.strip() #loai bo khoang trang cuoi cung neu co
s ="Tran    Duy      Thanh "
print(s,"=>",len(s))
s = ToiUuChuoi(s)
print(s,"=>",len(s))