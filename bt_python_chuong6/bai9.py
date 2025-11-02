# Hàm kiểm tra số nguyên tố
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập dãy số tự nhiên
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Phân loại
le = [x for x in M if x % 2 != 0]
chan = [x for x in M if x % 2 == 0]
nguyen_to = [x for x in M if la_nguyen_to(x)]
khong_nguyen_to = [x for x in M if not la_nguyen_to(x)]

# Xuất kết quả
print("Dãy số lẻ:", le)
print("👉 Tổng cộng có", len(le), "số lẻ.\n")

print("Dãy số chẵn:", chan)
print("👉 Tổng cộng có", len(chan), "số chẵn.\n")

print("Dãy số nguyên tố:", nguyen_to)
print("Dãy số không phải nguyên tố:", khong_nguyen_to)
