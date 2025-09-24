import math

def tinh_day_so(x, n):
    S = 0
    for i in range(1, n+1):
        S += (x**i) / math.factorial(i) #math.factorial(i) để tính giai thừa i!
    return S

# Nhập giá trị từ bàn phím
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

ket_qua = tinh_day_so(x, n)
print(f"Tổng S({x}, {n}) = {ket_qua}")