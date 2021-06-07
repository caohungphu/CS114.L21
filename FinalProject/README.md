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
- Khi mà việc đọc sách ngày càng trở nên phổ biến, thì nhu cầu lưu trữ thông tin về sách mình đã đọc để kiểm tra, chia sẽ, trao đổi hay mua bán ngày càng nhiều. Khi lượng sách quá nhiều thì việc nhập liệu sẽ mất thời gian hơn, cho nên để hỗ trợ cho việc này nhóm em quyết định xây dựng công cụ khi chụp vào một tấm ảnh bìa sách thì sẽ xuất ra dòng text chứa các thông tin về cuốn sách đó (tác giả, tên sách, nhà xuất bản, năm xuất bản) 
* Input: Ảnh bìa của một cuốn sách. 
* Output: Dòng text chứa các thông tin về cuốn sách đó (tác giả, tên sách, nhà xuất bản, năm xuất bản) 
## 2. MÔ TẢ VỀ BỘ DỮ LIỆU
- Thu thập dữ liệu: 
 + Chụp ảnh bìa sách từ các nhà sách.
 + Thu thập ảnh bìa sách của người mua sách đánh giá trên các trang bán hàng.
- Số lượng: 2000 cuốn sách, mỗi cuốn 2-3 tấm.
- Phân chia: 
  + 70% train
  + 20% validation
  + 10% test.
- Các thao tác tiền xử lý dữ liệu:
  + Chuẩn hoá kích thước ảnh.
  + Remove noise,background, chuyển hình ảnh về hai màu đen trắng.
  
 ## 3. MÔ TẢ VỀ ĐẶC TRƯNG

