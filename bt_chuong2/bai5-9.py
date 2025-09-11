#Câu 5
#print("-----Các loại ghi chú trong python-----")
#print("Ghi chú một dòng, dùng kí hiệu # ở đầu hoặc giữa dòng. Nội dung sau dấu # trên cùng một dòng sẽ bị bỏ qua khi chạy chương trình")
#print("Ghi chú nhiều dòng. Dùng nhiều dấu # liên tiếp cho từng dòng")
#print("Ghi chú cho chuỗi văn bản đặc biệt. Được đặt trong cặp dấu 3 nháy ")

#Câu 6
# '/' – Chia thực (Float Division)
#Thực hiện phép chia và luôn trả về số thực(float) kể cả khi chia hết.
# '//' – Chia nguyên (Floor Division)
#Thực hiện phép chia nhưng lấy phần nguyên (làm tròn xuống – floor).
#'%' – Chia lấy dư (Modulo)
#Trả về phần dư của phép chia.
#'**' – Lũy thừa (Exponentiation)
#Dùng để tính số mũ.
#'and' – Toán tử logic "Và"
#Kết quả là True nếu cả hai biểu thức đều đúng, ngược lại trả về False.
#Python có đặc điểm trả về giá trị cuối cùng được đánh giá, không chỉ True/False.

#Câu 7
#Các cách nhập dữ liệu từ bàn phím
#input() → chuỗi
#int(input()) → số nguyên
#float(input()) → số thực
#split() → nhiều giá trị cùng lúc
#map() + list() → danh sách phần tử
#input()[0] → một ký tự

#Câu 8
#Các lỗi trong Python
#Lỗi cú pháp(Syntax Error), lỗi thực thi(Runtime Error / Exception), lỗi logic(Logical Error)
#Cách bắt lỗi trong python: try – except – else – finally.

#Câu 9
#Với các giá trị đã cho ta có:

#a) i1 + (i2 * i3)
#= 2 + (5 * -3)
#= 2 + -15
#= -13

#b) i1 * (i2 + i3)

#= 2 * (5 + -3)
#= 2 * 2
#= 4

#c) i1 / (i2 + i3)

#= 2 / (5 + -3)
#= 2 / 2
#= 1.0 (chia / luôn ra float)

#d) i1 // (i2 + i3)

#= 2 // (5 + -3)
#= 2 // 2
#= 1 (chia nguyên, kết quả int)

#e)i1 / i2 + i3

#= (2 / 5) + (-3)
#= 0.4 - 3
#= -2.6

#f) i1 // i2 + i3

#= (2 // 5) + (-3)
#= 0 + (-3)
#= -3

#g) 3 + 4 + 5 / 3

#= 3 + 4 + (5 / 3)
#= 7 + 1.666...
#= 8.666...

#h) 3 + 4 + 5 // 3

#= 3 + 4 + (5 // 3)
#= 7 + 1
#= 8

#i) (3 + 4 + 5) / 3

#= (12) / 3
#= 4.0

#j) (3 + 4 + 5) // 3

#= (12) // 3
#= 4

#k)d1 + (d2 * d3)

#= 2.0 + (5.0 * -0.5)
#= 2.0 + -2.5
#= -0.5

#l) d1 + d2 * d3

#Theo thứ tự ưu tiên * trước +.
#= 2.0 + (5.0 * -0.5)
#= 2.0 - 2.5
#= -0.5

#m) d1 / d2 - d3

#= (2.0 / 5.0) - (-0.5)
#= 0.4 + 0.5
#= 0.9

#n) d1 / (d2 - d3)

#= 2.0 / (5.0 - -0.5)
#= 2.0 / 5.5
#≈ 0.3636

#o) d1 + d2 + d3 / 3

#Theo thứ tự ưu tiên: d3 / 3 tính trước.
#= 2.0 + 5.0 + (-0.5 / 3)
#= 7.0 - 0.166...
#≈ 6.833...

#p) (d1 + d2 + d3) / 3

#= (2.0 + 5.0 + -0.5) / 3
#= 6.5 / 3
#≈ 2.166...

#q) d1 + d2 + (d3 / 3)

#= 2.0 + 5.0 + (-0.5 / 3)
#= 7.0 - 0.166...
#≈ 6.833... (giống câu o)

#r) 3 * (d1 + d2) * (d1 - d3)

#= 3 * (2.0 + 5.0) * (2.0 - -0.5)
#= 3 * 7.0 * 2.5
#= 21.0 * 2.5
#= 52.5