import math

# Nhập a và x
a = float(input("Nhập cơ số a (>0, ≠1): "))
x = float(input("Nhập số x (>0): "))

# Kiểm tra điều kiện hợp lệ
if a > 0 and a != 1 and x > 0:
    log_a_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {log_a_x}")
else:
    print("Giá trị a và x không hợp lệ! (yêu cầu a>0, a≠1, x>0)")
