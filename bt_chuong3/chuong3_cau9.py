# Nhập tháng 
month = int(input("Nhập tháng (1-12): "))

# Xác định quý của tháng
if month < 1 or month > 12:
    print("Lỗi: Tháng không hợp lệ. Vui lòng nhập số từ 1 đến 12.")
else:
    if month in [1, 2, 3]:
        quarter = 1
    elif month in [4, 5, 6]:
        quarter = 2
    elif month in [7, 8, 9]:
        quarter = 3
    else:  # tháng 10, 11, 12
        quarter = 4

    print(f"Tháng {month} thuộc quý {quarter} trong năm.")