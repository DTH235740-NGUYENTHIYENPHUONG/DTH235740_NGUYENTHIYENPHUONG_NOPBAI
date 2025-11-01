import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- HÀM HỖ TRỢ: in một pattern (dùng vòng lặp) ---
def render_pattern(pattern_lines):
    """pattern_lines: list of strings, mỗi string là một hàng chứa ' ' và '*'"""
    out_lines = []
    for row in pattern_lines:
        # mỗi hàng có thể được tạo/tùy chỉnh ở đây nếu muốn (vd: padding)
        out_lines.append(row.rstrip())  # giữ chính xác hàng (dùng vòng lặp)
    return '\n'.join(out_lines)

# --- HÀM SINH MẪU TỰ ĐỘNG (ví dụ) DÙNG VÒNG LẶP ---
def tam_giac_trai(n=6):
    lines = []
    for i in range(1, n+1):
        lines.append('*' * i)
    return lines

def chu_nhat_rong(r=6, c=12):
    lines = []
    for i in range(r):
        if i == 0 or i == r-1:
            lines.append('*' * c)
        else:
            lines.append('*' + ' ' * (c-2) + '*')
    return lines

def kim_cuong_rong(size=6):
    lines = []
    # top
    for i in range(size):
        out = ' ' * (size - i - 1)
        if i == 0:
            out += '*'
        else:
            out += '*' + ' ' * (2*i - 1) + '*'
        lines.append(out)
    # bottom
    for i in range(size-2, -1, -1):
        out = ' ' * (size - i - 1)
        if i == 0:
            out += '*'
        else:
            out += '*' + ' ' * (2*i - 1) + '*'
        lines.append(out)
    return lines

def chu_x(n=13):
    # n nên là số lẻ để đẹp
    if n % 2 == 0:
        n += 1
    lines = []
    for i in range(n):
        row = [' '] * n
        row[i] = '*'
        row[n-1-i] = '*'
        lines.append(''.join(row))
    return lines

# --- NẾU MẪU TRONG ẢNH RẤT CỤ THỂ: dán nguyên mẫu vào đây ---
# Thay 4 mẫu dưới bằng chính xác multiline string từ ảnh nếu cần
PATTERNS_RAW = [
    # Mẫu 1: (ví dụ) — bạn có thể thay nội dung giữa 3 dấu nháy cho giống mẫu ảnh
"""
      *
      **
      ***
   *******
   ***
   **
   *   
""",
    # Mẫu 2: chữ nhật rỗng (ví dụ)
    """
      *
      **
      * *
   *******
   * *
   **
   *   
""",
    # Mẫu 3: kim cương rỗng (ví dụ)
"""
      ****
      ***
      **
      *
     **
    ***
   **** 
""",
    # Mẫu 4: chữ X (ví dụ)
    """
      ****
      * *
      **
      *
     **
    * *
   **** 
"""
]

# --- Chuyển PATTERNS_RAW -> danh sách lines bằng việc tách dòng, loại bỏ leading/trailing blank ---
PATTERNS = []
for raw in PATTERNS_RAW:
    # tách và loại bỏ các hàng rỗng ở đầu/cuối
    rows = [line.rstrip('\n') for line in raw.strip('\n').splitlines()]
    PATTERNS.append(rows)

# --- Hoặc có thể dùng các functions tự động sinh (nếu bạn không paste mẫu) ---
AUTO_PATTERNS = [
    tam_giac_trai(6),
    chu_nhat_rong(6, 12),
    kim_cuong_rong(6),
    chu_x(13)
]

# Chọn nguồn hiển thị: uncomment một trong hai dòng dưới
use_from = "raw"   # "raw" để dùng PATTERNS (paste mẫu của bạn vào PATTERNS_RAW)
# use_from = "auto"  # "auto" để dùng AUTO_PATTERNS sinh bằng vòng lặp

if use_from == "raw":
    display_patterns = PATTERNS
else:
    display_patterns = AUTO_PATTERNS

# Hiển thị từng pattern, mỗi pattern hiện 5 giây
DELAY_SECONDS = 5

for idx, pattern_lines in enumerate(display_patterns, start=1):
    clear()
    print(f"Hình {idx}:\n")
    art = render_pattern(pattern_lines)  # in bằng vòng lặp bên trong hàm này
    print(art)
    # Đếm ngược hiển thị (tùy chọn) — in số giây còn lại
    for sec in range(DELAY_SECONDS, 0, -1):
        print(f"\nChuyển hình sau {sec} giây...", end='\r')
        time.sleep(1)

clear()
print("Hoàn thành.")
