#Câu 5: Hãy cho biết kết quả xuất ra màn hình
#Yêu cầu:
#Cho i, j, k là các con số và lệnh dưới đây:
i=int(input("Nhập i:"))
j=int(input("Nhập j:"))
k=int(input("Nhập k:"))
if(i<j):
    if j<k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =",i, "j =",j,"k =",k)
    

#Hãy cho biết kết quả xuất ra màn hình nếu tuần tự 3 biến trên có các giá trị sau:
#(a) i = 3, j = 5, and k = 7 ==> i = 5 j = 5 k = 7
#(b) i = 3, j = 7, and k = 5 ==> i = 3 j = 5 k = 5
#(c) i = 5, j = 3, and k = 7 ==> i = 7 j = 3 k = 7
#(d) i = 5, j = 7, and k = 3 ==> i = 5 j = 3 k = 3 
#(e) i = 7, j = 3, and k = 5 ==> i = 5 j = 3 k = 5
#(f) i = 7, j = 5, and k = 3 ==> i = 7 j = 7 k = 3