def hinh_vuong_rong(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def hinh_tam_giac_trai_duoi(n):
    for i in range(1, n+1):
        print("* " * i)

def hinh_tam_giac_trai_tren(n):
    for i in range(n, 0, -1):
        print("* " * i)

def hinh_chu_L_nguoc(n):
    for i in range(n):
        print("* ", end="")
    print()
    for i in range(1, n):
        print("  " * (n-1) + "*")
def hinh_cuoi(n):
    mid = (n + 1) // 2   # chỉ số hàng giữa (dòng in ngang n dấu *)
    width = n + 1        # chiều ngang đủ lớn để chứa các vị trí sao

    for i in range(n):
        # tạo một hàng chứa các ký tự (khoảng trắng hoặc '*')
        row = [' '] * width

        if i == 0:
            # dòng đầu: chỉ 1 sao ở cột trái
            row[0] = '*'
        elif i < mid:
            # phần trên: sao ở cột trái + sao di chuyển sang phải theo i
            row[0] = '*'
            row[i + 1] = '*'
        elif i == mid:
            # hàng giữa: n sao liên tiếp
            for j in range(n):
                row[j] = '*'
        else:
            # phần dưới: hai sao dịch dần sang phải (nếu còn chỗ)
            k = i - mid
            j1 = mid + k
            j2 = n - k
            if j1 <= j2:
                if j1 < len(row): row[j1] = '*'
                if j2 < len(row): row[j2] = '*'
            else:
                if j1 < len(row): row[j1] = '*'

        # in hàng (mỗi ký tự cách nhau 1 dấu cách để canh lề đẹp)
        print(' '.join(row).rstrip())
# =============================
n = int(input("Nhập chiều cao n: "))

print("\nHình vuông rỗng:")
hinh_vuong_rong(n)

print("\nHình tam giác vuông (trái dưới):")
hinh_tam_giac_trai_duoi(n)

print("\nHình tam giác vuông (trái trên):")
hinh_tam_giac_trai_tren(n)

print("\nHình chữ L ngược:")
hinh_chu_L_nguoc(n)

print("\nHình cuối:")
hinh_cuoi(n)