ỨNG DỤNG XEM & TRA CỨU DỮ LIỆU THỜI TIẾT TỪ FIREBASE

Đây là một ứng dụng Python + Web mô phỏng hệ thống thu thập và xem dữ liệu từ các trạm thời tiết.
Ứng dụng cho phép:

Gửi dữ liệu nhiệt độ, độ ẩm, tốc độ gió, áp suất từ các trạm lên Firebase Realtime Database.

Xem dữ liệu thời tiết của một trạm cụ thể hoặc toàn bộ danh sách trạm.

Cung cấp giao diện web để tra cứu dữ liệu theo mã trạm, hiển thị thông tin dạng bảng đẹp mắt.

CÔNG NGHỆ SỬ DỤNG

Python: Gửi và lấy dữ liệu từ Firebase thông qua thư viện firebase_admin.

Firebase Realtime Database: Lưu trữ dữ liệu trạm thời tiết theo thời gian thực.

HTML/CSS/JavaScript: Xây dựng giao diện web để tìm kiếm và hiển thị dữ liệu trạm.

Firebase Web SDK: Kết nối và truy xuất dữ liệu trực tiếp từ frontend.

Luồng xử lý hệ thống

Thu thập dữ liệu: Người dùng nhập thông số thời tiết tại trạm qua ứng dụng Python (app1.py).

Lưu trữ: Dữ liệu được gửi và lưu vào Firebase theo cấu trúc stations/{id}.

Xem dữ liệu:

Chế độ Python CLI (app2.py): Xem thông tin một trạm hoặc toàn bộ trạm.

Chế độ Web (view-station.html): Nhập mã trạm → Lấy dữ liệu từ Firebase → Hiển thị ra giao diện.

CÁC CHỨC NĂNG CHÍNH

Nhập và lưu dữ liệu trạm thời tiết lên Firebase.

Xem dữ liệu từng trạm hoặc toàn bộ danh sách.

Giao diện web hỗ trợ tìm kiếm theo mã trạm.

Hiển thị thông tin trực quan với thiết kế responsive.

Kết nối Firebase an toàn qua cấu hình riêng.

HÌNH ẢNH MINH HỌA

giao diện nhập thông tin trạm thời tiết
<img width="997" height="581" alt="image" src="https://github.com/user-attachments/assets/4a38cad6-fbbf-467e-80c3-8d049282e33d" />


giao diện xem thông tin theo mã trạm
<img width="1174" height="697" alt="image" src="https://github.com/user-attachments/assets/6cd8e743-7ee3-4a54-a0f5-5433d767d63c" />

giao diện danh sách các trạm thời tiết
<img width="1024" height="666" alt="image" src="https://github.com/user-attachments/assets/3ce52931-6169-4b84-9e8d-f18c4e12b7fb" />

