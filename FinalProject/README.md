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
- Input: Một bức ảnh bất kỳ.
- Output: Một con số 1 hoặc 0 đại diện cho có hay không sự xuất hiện của đám cháy trong bức hình.
## 2. MÔ TẢ VỀ BỘ DỮ LIỆU
- Thu thập dữ liệu: 
    + Nhóm tự crawl hình ảnh có cháy và không có cháy từ google.
    + Số lượng: 3600 ảnh có cháy, 2175 ảnh không có cháy.
    + Dữ liệu ảnh có cháy sẽ bao gồm lửa to, lửa nhỏ, khói nhiều, khói ít được lấy từ ảnh (cháy rừng, cháy xe, cháy nhà, ngọn lửa từ nến, từ hột quẹt,..) trong điều kiện ngày và đêm, từ góc chụp camera an ninh, góc chụp thẳng, góc chụp từ trên cao để đảm bảo bao quát được tất cả trường hợp.
    + Dữ liệu ảnh không cháy sẽ bao gồm cây xanh, công trình, con người, xe cộ, các hàng quán,... trong các điều kiện sáng, tối và có khói, không khói từ nhiều góc chụp camera an ninh, góc chụp thẳng, góc chụp từ trên cao.
- Phân chia: 
    + 60% train
    + 20% test
    + 20% validation
- Các thao tác tiền xử lý dữ liệu:
    + Chuẩn hoá kích thước ảnh.
    + Remove noise,background.
  
 ## 3. MÔ TẢ VỀ ĐẶC TRƯNG

