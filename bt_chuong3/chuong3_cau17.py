#done được gọi là biến cờ (flag variable)
#done = False --> chưa xong tiếp tục lặp
#n, m = 0, 100
#while not done and n != m:
#    n = int(input())
#    if n < 0:
#        done = True --. thoát lập
#    print('n =', n)

# viết lại đoạn code trên dùng từ khóa break
n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break   # Thoát vòng lặp ngay lập tức
    print('n =', n)