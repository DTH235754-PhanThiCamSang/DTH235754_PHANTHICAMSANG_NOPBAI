#tính BMI
def BMI(height, weight):
    bmi = weight / (height ** 2)
def PHANLOAI(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi < 24.9:
        return "Bình thường"
    elif bmi < 29.9:
        return "Hơi béo"
    elif bmi < 34.9:
        return "Béo phì cấp độ 1"
    elif bmi < 39.9:
        return "Béo phì cấp độ 2"   
    else:
        return "Béo phì cấp độ 3"
def Nguycobenh(bmi):
    if bmi < 18.5:
        return "Nguy cơ bệnh thấp"
    elif bmi < 24.9:
        return "Nguy cơ bệnh trung bình"
    elif bmi < 29.9:
        return "Nguy cơ bệnh cao"
    elif bmi < 34.9:
        return "Nguy cơ bệnh rất cao"
    elif bmi < 39.9:
        return "Nguy cơ bệnh rất rất cao"   
    else:
        return "Nguy hiểm"
print ("Nhap chieu cao (m): ")
height = float(input())
print ("Nhap can nang (kg): ")  
weight = float(input()) 
bmi = BMI(height, weight)
print("BMI cua ban la: ", bmi)
print("PHAN LOAI THEO BMI: ", PHANLOAI(bmi))
print("Nguy co benh: ", Nguycobenh(bmi))
