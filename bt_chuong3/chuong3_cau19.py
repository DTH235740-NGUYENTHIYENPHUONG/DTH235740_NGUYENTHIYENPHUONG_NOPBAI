import math

def S_simple(x, n):
    S = 0.0
    for k in range(n+1):               # k = 0..n
        p = 2*k + 1                    # mũ lẻ: 1,3,5,...,2n+1
        S += x**p / math.factorial(p)
    return S

# ví dụ chạy
x = float(input("Nhập x: "))
n = int(input("Nhập n (>=0): "))
print("S =", S_simple(x, n))