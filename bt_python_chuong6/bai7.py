# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của dãy: "))

lst = []

for i in range(n):
    while True:
        x = int(input(f"Nhập số thứ {i+1}: "))
        # Nếu là phần tử đầu tiên, chấp nhận luôn
        if i == 0:
            lst.append(x)
            break
        # Nếu các phần tử sau lớn hơn phần tử trước → hợp lệ
        elif x > lst[i-1]:
            lst.append(x)
            break
        else:
            print("❌ Sai quy tắc (phải nhập lớn hơn số trước). Vui lòng nhập lại!")

print("\n✅ Dãy số hợp lệ là:", lst)