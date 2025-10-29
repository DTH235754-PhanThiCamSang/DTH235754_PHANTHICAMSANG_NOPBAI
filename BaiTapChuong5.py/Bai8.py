def LayTenFile(path):
    # Tách theo dấu "\" để lấy phần cuối cùng
    # Vì "\" là ký tự đặc biệt nên cần viết "\\"
    parts = path.split("\\")
    return parts[-1]  # phần cuối là tên file.mp3

def LayTenBaiHat(path):
    ten_file = LayTenFile(path)
    # Tách phần tên và phần mở rộng
    ten_bai_hat = ten_file.split(".")[0]
    return ten_bai_hat

# ====== Chạy thử ======
duongdan = input("Nhập đường dẫn file nhạc: ")
print("Tên file:", LayTenFile(duongdan))
print("Tên bài hát:", LayTenBaiHat(duongdan))
