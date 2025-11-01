# Nhập chuỗi từ bàn phím
chuoi = input("Nhập vào một chuỗi: ")

# Khởi tạo biến đếm
dem_hoa = dem_thuong = dem_so = dem_kytudacbiet = dem_khoangtrang = 0
dem_nguyenam = dem_phuam = 0

nguyen_am = "aeiouAEIOU"

# Duyệt qua từng ký tự trong chuỗi
for c in chuoi:
    if c.isupper():
        dem_hoa += 1
    elif c.islower():
        dem_thuong += 1
    elif c.isdigit():
        dem_so += 1
    elif c.isspace():
        dem_khoangtrang += 1
    else:
        dem_kytudacbiet += 1

    # Kiểm tra nguyên âm / phụ âm
    if c.isalpha():  # chỉ xét ký tự là chữ cái
        if c in nguyen_am:
            dem_nguyenam += 1
        else:
            dem_phuam += 1

# Xuất kết quả
print("Số chữ IN HOA:", dem_hoa)
print("Số chữ in thường:", dem_thuong)
print("Số chữ là chữ số:", dem_so)
print("Số ký tự đặc biệt:", dem_kytudacbiet)
print("Số ký tự khoảng trắng:", dem_khoangtrang)
print("Số chữ là nguyên âm:", dem_nguyenam)
print("Số chữ là phụ âm:", dem_phuam)
