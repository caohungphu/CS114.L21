<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>ĐỒ ÁN CUỐI KỲ</b></h1>
<h1 align="center"><b>TÊN ĐỒ ÁN: NHẬN DIỆN CHỮ VIẾT TAY TIẾNG VIỆT</b></h1>

## 1. MÔ TẢ BÀI TOÁN
- Trong thời đại nước ta đang phát triển chính phủ số, chính quyền số. Việc số hoá dữ liệu tức  chuyển đổi dữ liệu từ dạng văn bản hệ thống bên ngoài thành những dữ liệu lưu trữ trong máy tính là rất cần thiết. Hay đơn giản một công ty muốn lưu giữ tất cả hợp đồng tài liệu viết tay cho các phòng ban của công ty.
- Vì vậy để góp phần đẩy nhanh quá trình số hoá, nhóm em hướng tới tận dụng sự phát triển của Machine Learning để thực hiện quá trình này bằng cách xây dựng mô hình chuyển hình ảnh chữ viết tay tiếng việt thành văn bản lưu trên máy tính.
* Input: Hình ảnh dòng chữ viết tay
* Output: Kết quả chữ viết tay nhận diện được. 

## 2. MÔ TẢ VỀ BỘ DỮ LIỆU
- Thu thập dữ liệu: Tự xây dựng bằng cách xin hình ảnh về chữ viết tay từ tập vở của những người xung quanh. Sau đó sẽ gán nhãn cho từng ảnh chụp các dòng chữ.
- Số lượng: 5000 dòng chữ từ 50 người.
- Phân chia: 
  + 70% train
  + 20% validation
  + 10% test.
- Các thao tác tiền xử lý dữ liệu:
  + Chuẩn hoá kích thước ảnh.
  + Remove noise,background, chuyển hình ảnh về hai màu đen trắng.
  
 ## 3. MÔ TẢ VỀ ĐẶC TRƯNG

