import math
try:
    r = float(input("Mời bạn nhập bán kính hình tròn: "))
    cv=2*math.pi*r
    dt=2*r
    print("Chu vi =",cv)
    print("Diện tích =",dt)
except:
    print("Lỗi rồi!!!")