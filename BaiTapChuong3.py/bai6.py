def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    dac_biet = {5: "lăm", 1: "mốt"}
    if n < 0 or n > 99:
        return "Số không hợp lệ"
    if n < 10:
        return don_vi[n] if n != 0 else "không"
    chuc = n // 10
    dv = n % 10
    ket_qua = ""
    if chuc == 1:
        ket_qua = "mười"
        if dv == 5:
            ket_qua += " lăm"
        elif dv != 0:
            ket_qua += " " + don_vi[dv]
    else:
        ket_qua = don_vi[chuc] + " mươi"
        if dv == 1:
            ket_qua += " mốt"
        elif dv == 5:
            ket_qua += " lăm"
        elif dv != 0:
            ket_qua += " " + don_vi[dv]
    return ket_qua.strip()

n = int(input("Nhập số n (tối đa 2 chữ số): "))
print(doc_so(n))