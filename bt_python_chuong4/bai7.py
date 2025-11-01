import math

# Nhập tọa độ 2 điểm
xA = float(input("Nhập hoành độ xA: "))
yA = float(input("Nhập tung độ yA: "))
xB = float(input("Nhập hoành độ xB: "))
yB = float(input("Nhập tung độ yB: "))

# Tính độ dài đoạn AB
dAB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Xuất kết quả
print(f"Độ dài đoạn AB là: {dAB}")