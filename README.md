# 🕸️ Crawler Nhà Đất Đà Nẵng - alonhadat.com.vn

Đây là một script tự động thu thập thông tin bất động sản **cho thuê tại Đà Nẵng** từ trang [alonhadat.com.vn](https://alonhadat.com.vn). Dữ liệu sẽ được lưu thành file Excel và cập nhật mỗi ngày vào **6:00**.



# Tính năng

- Tự động mở trình duyệt, chọn "Đà Nẵng" và lọc tin "Cho thuê".
- Thu thập dữ liệu từ tối đa **5 trang kết quả đầu tiên**.
- Lưu dữ liệu thành file `.xlsx` có định dạng chuẩn.
- Tự động chạy vào thời gian định sẵn (6:00).
- Có xử lý lỗi cơ bản, dễ bảo trì và mở rộng.



# Yêu cầu hệ thống

- Python >= 3.7
- Google Chrome đã cài đặt
- ChromeDriver tương ứng với phiên bản Chrome



# Cài đặt thư viện

Chạy lệnh sau trong terminal/cmd để cài đặt các thư viện cần thiết:

```bash
pip install selenium pandas openpyxl
