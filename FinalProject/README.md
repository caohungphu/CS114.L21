<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>ĐỒ ÁN CUỐI KỲ</b></h1>
<h1 align="center"><b>TÊN ĐỒ ÁN: PHÁT HIỆN CHÁY THÔNG QUA HÌNH ẢNH</b></h1>

## 1. MÔ TẢ BÀI TOÁN
- Từ trước đến nay, cháy vẫn luôn là một tai nạn gây thiệt hại nghiêm trọng đến tính mạng, tài sản của người dân. Vì vậy để đảm bảo an toàn, tín hiệu báo cháy phải được phát hiện chính xác và trong thời gian sớm nhất có thể. Tuy nhiên các thiết bị báo cháy truyền thống dựa trên nhiệt độ hay khói dễ bị ảnh hưởng bởi các yếu tố của môi trường như độ cao đặt thiết bị hay bụi,... Do đó, nhóm em xây dựng một thuật toán để phát hiện cháy thông qua hình ảnh dựa trên Image Classification.
* Input: Một bức ảnh bất kỳ.
* Output: Một con số 1 hoặc 0 đại diện cho có hay không sự xuất hiện của đám cháy trong bức hình.
## 2. MÔ TẢ VỀ BỘ DỮ LIỆU
- Thu thập dữ liệu: 
 + Nhóm tự crawl hình ảnh có cháy và không có cháy từ google.
- Số lượng: 3300 ảnh có cháy, gần 2000 ảnh không có cháy.
- Phân chia: 
  + 60% train
  + 20% validation
  + 20% test.
- Các thao tác tiền xử lý dữ liệu:
  + Chuẩn hoá kích thước ảnh.
  + Remove noise,background, chuyển hình ảnh về hai màu đen trắng.
  
 ## 3. MÔ TẢ VỀ ĐẶC TRƯNG

