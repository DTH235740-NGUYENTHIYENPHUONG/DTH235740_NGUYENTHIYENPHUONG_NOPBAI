# --- Hàm nhập ma trận ---
def nhap_matrix(ten):
    rows = int(input(f"Nhập số hàng của ma trận {ten}: "))
    cols = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    M = []
    for i in range(rows):
        row = list(map(float, input(f"Hàng {i+1}: ").split()))
        while len(row) != cols:
            print("⚠️  Số phần tử không khớp số cột, nhập lại!")
            row = list(map(float, input(f"Hàng {i+1}: ").split()))
        M.append(row)
    return M

# --- Hàm in ma trận ---
def in_matrix(M, name="Matrix"):
    print(f"\n{name}:")
    for row in M:
        print(row)

# --- Hàm cộng hai ma trận ---
def cong_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("⚠️  Hai ma trận phải cùng kích thước mới cộng được!")
        return None
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

# --- Hàm hoán vị ma trận ---
def hoan_vi(M):
    rows = len(M)
    cols = len(M[0])
    T = [[M[j][i] for j in range(rows)] for i in range(cols)]
    return T


# --- Chương trình chính ---
A = nhap_matrix("A")
B = nhap_matrix("B")

# In A, B
in_matrix(A, "Ma trận A")
in_matrix(B, "Ma trận B")

# Cộng A + B
C = cong_matrix(A, B)
if C:
    in_matrix(C, "Ma trận C = A + B")

# Hoán vị
AT = hoan_vi(A)
BT = hoan_vi(B)

in_matrix(AT, "Ma trận hoán vị Aᵀ")
in_matrix(BT, "Ma trận hoán vị Bᵀ")
