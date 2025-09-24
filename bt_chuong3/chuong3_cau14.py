a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a+b) % 2 == 0:
            print('*', end = '' )
        b += 1
    print()
    a += 1
    # có 2000 dấu sao được in
    # a chạy từ 0 --> 99 có 100 dòng được in
    # b chạy từ 0 --> 39 có 20 dấu sao được in trên mỗi dòng
    # 20 * 100 = 2000