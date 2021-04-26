<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS114.L21 - MÁY HỌC - MACHINE LEARNING</b></h1>
<h1 align="center"><b>BÀI TẬP QUÁ TRÌNH NGÀY 26/04/2021</b></h1>

## ĐỀ BÀI:
- Mỗi nhóm tìm dăm ba ví dụ về bài toán regression ***TRONG THỰC TẾ***
- Ghi rõ input, output và cách thu thập + xử lý data, commit vào github repository và dẫn link lên Google Classroom.

## NHÓM THỰC HIỆN:
- Cao Hưng Phú - 19520214 - 19520214@gm.uit.edu.vn
- Nguyễn Thành Công - 19521294 - 19521294@gm.uit.edu.vn
- Trần Huỳnh Kỳ Anh - 19521216 - 19521216@gm.uit.edu.vn


## BÀI LÀM:

### Bài toán 1: Dự đoán doanh số trong tháng tiếp theo
- Input: Doanh số các tháng trước đó
- Output: Doanh số của tháng tiếp theo
- Cách thu thập data: Lấy dữ liệu từ báo cáo doanh thu hằng tháng
- Cách xử lí data: Gom nhóm các dữ liệu báo cáo doanh thu hằng tháng vào cùng 1 file CSV

### Bài toán 2: Dự đoán chỉ số tiêu thụ điện
- Input: Chỉ số tiêu thụ điện của các tháng qua từng năm
- Output: Chỉ số tiêu thụ điện của tháng cần dự đoán
- Cách thu thập data: Ghi nhận chỉ số tiêu thụ điện qua từng tháng
- Cách xử lí data: Gom nhóm dữ liệu từng tháng vào cùng 1 file CSV

### Bài toán 3: Dự đoán điểm kiểm tra cuối kì
- Input: Điểm quá trình, giữa kì, thực hành (Kiểu số thực)
- Output: Điểm cuối kì (Kiểu số thực)
- Cách thu thập data:
  - Tạo form điền thông tin khảo sát
  - Xin dữ liệu từ phòng đào tạo
  - Xin dữ liệu từ giáo viên bộ môn
- Cách xử lí data:
  + Gom nhóm các dữ liệu báo cáo doanh thu hằng tháng vào cùng 1 file CSV
  + Xóa các dòng mà thuộc tính không có giá trị (NULL)
  + Xóa các dòng mà thuộc tính có giá trị âm hoặc lớn hơn 10 (Điểm dao động từ 0 -> 10)
