def doc_so(n):
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi",
                 "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    hang_donvi = ["", "một", "hai", "ba", "bốn",
                  "năm", "sáu", "bảy", "tám", "chín"]

    if n < 0 or n > 99:
        return "Số không hợp lệ (chỉ nhập từ 0 đến 99)"

    if n < 10:
        # Trường hợp 1 chữ số
        return hang_donvi[n]

    chuc = n // 10
    dv = n % 10

    if dv == 0:
        return hang_chuc[chuc]
    elif chuc == 1:
        # trường hợp 10–19
        if dv == 5:
            return "mười lăm"
        else:
            return "mười " + hang_donvi[dv]
    else:
        # từ 20–99
        if dv == 1:
            return hang_chuc[chuc] + " mốt"
        elif dv == 5:
            return hang_chuc[chuc] + " lăm"
        else:
            return hang_chuc[chuc] + " " + hang_donvi[dv]


# --- Chương trình chính ---
n = int(input("Nhập số nguyên n (0–99): "))
print("Cách đọc:", doc_so(n))