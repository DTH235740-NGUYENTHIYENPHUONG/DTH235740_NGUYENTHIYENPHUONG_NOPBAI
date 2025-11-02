import random

# Nhập số lượng phần tử
N = int(input("Nhập số lượng phần tử của list: "))

# Sinh ngẫu nhiên N số KHÔNG TRÙNG từ khoảng 0 đến 100
lst = random.sample(range(0, 101), N)

print("List ngẫu nhiên không trùng là:", lst)
