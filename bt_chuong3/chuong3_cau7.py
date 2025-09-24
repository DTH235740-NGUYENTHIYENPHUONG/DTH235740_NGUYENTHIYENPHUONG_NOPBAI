def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 0  # tháng không hợp lệ

def ngay_ke_tiep(ngay, thang, nam):
    ngay_max = so_ngay_trong_thang(thang, nam)
    if ngay < ngay_max:
        return ngay + 1, thang, nam
    else:
        if thang == 12:
            return 1, 1, nam + 1
        else:
            return 1, thang + 1, nam

# --- Chương trình chính ---
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ngay_sau, thang_sau, nam_sau = ngay_ke_tiep(ngay, thang, nam)
print(f"Ngày kế tiếp: {ngay_sau}/{thang_sau}/{nam_sau}")