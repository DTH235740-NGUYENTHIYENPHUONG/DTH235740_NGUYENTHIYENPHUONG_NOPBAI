a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
operation = input("Nhập phép toán (+, -, *, /): ")

# Thực hiện phép toán và xuất kết quả
if operation == '+':
    result = a + b
    print(f"Kết quả: {a} + {b} = {result}")
elif operation == '-':
    result = a - b
    print(f"Kết quả: {a} - {b} = {result}")
elif operation == '*':
    result = a * b
    print(f"Kết quả: {a} * {b} = {result}")
elif operation == '/':
    if b != 0:
        result = a / b
        print(f"Kết quả: {a} / {b} = {result}")
    else:
        print("Lỗi: Không thể chia cho 0.")
else:
    print("Lỗi: Phép toán không hợp lệ.")