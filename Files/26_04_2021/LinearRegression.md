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

### Bài toán 1: Dự đoán sản lượng nông sản dựa trên số lượng phân bón
- Input: Lượng phân bón của từng loại phân trên một ![km^2](https://latex.codecogs.com/svg.latex?km^2)
- Output: Sản lượng nông sản (kg)
- Cách thu thập data: 
  - Tạo form điền thông tin khảo sát cho nông dân
  - Xin dữ liệu từ nhà máy nông sản, công trường
  - Xin dữ liệu từ các đại lý phân bón
- Cách xử lí data:
  - Gom nhóm các dữ liệu về phân bón, sản lượng theo từng mùa vụ vào cùng 1 file CSV
  - Xóa các dòng mà thuộc tính không có giá trị (NULL)
  - Xóa các dòng mà thuộc tính có giá trị âm 

### Bài toán 2: Dự đoán doanh thu sản phẩm dựa trên chi phí quảng cáo
- Input: Chi phí quảng cáo trên tivi, báo, mạng xã hội (Kiểu số nguyên)
- Output: Doanh thu sản phẩm được quảng cáo (Kiểu số nguyên)
- Cách thu thập data: Thu thập bộ dữ liệu thực về doanh thu theo chi phí quảng cáo từ các công ty
- Cách xử lí data: 
  + Gom nhóm dữ liệu chi phí quảng cáo và doanh thu vào cùng 1 file CSV
  + Xóa các dòng mà thuộc tính không có giá trị (NULL)
  + Xóa các dòng mà thuộc tính có giá trị âm 
### Bài toán 3: Dự đoán điểm kiểm tra cuối kì dựa trên điểm quá trình, giữa kì và thực hành
- Input: Điểm quá trình, giữa kì, thực hành (Kiểu số thực)
- Output: Điểm cuối kì (Kiểu số thực)
- Cách thu thập data:
  - Tạo form điền thông tin khảo sát
  - Xin dữ liệu từ phòng đào tạo
  - Xin dữ liệu từ giáo viên bộ môn
- Cách xử lí data:
  + Gom nhóm các dữ liệu vào cùng 1 file CSV
  + Xóa các dòng mà thuộc tính không có giá trị (NULL)
  + Xóa các dòng mà thuộc tính có giá trị âm hoặc lớn hơn 10 (Điểm dao động từ 0 -> 10)
