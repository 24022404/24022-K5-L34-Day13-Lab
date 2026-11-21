# Báo cáo cá nhân — NguyenDucMinh-2A202603563

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Minh
- MSSV: 2A202603563
- Email: 26ai.minhnd3@vinuni.edu.vn
- GitHub: ducminhnwork
- Vai trong nhóm: người viết code (kiêm giữ hồ sơ phần A, B, D, E)

## 2. Phần việc phụ trách

Nhiệm vụ A (mô hình chi phí), B (bảng độ nhạy), D (kế hoạch pilot) và E (chỉ số, event, rủi ro kinh tế, hồ sơ launch v0).

## 3. Đóng góp cụ thể

- Viết `src/lab13.py`: ba hàm A1, `mo_hinh` (A2), bảng theo loại (A3), chi phí cố định (A4), chín kịch bản độ nhạy (B1), cặp và xếp hạng (B2), giới hạn số lần chạy (B3), xem lại 100% (B4), cỡ mẫu D1 và chỉ số tính thử E1.
- Điền `bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`.

## 4. Bằng chứng

- `python lab13.py` in ba phép thử A1 ĐẠT; chi phí mỗi việc thành công 4.472 đ [simulated] trên 978 việc thành công.
- Commit trên nhánh `ducminhnwork`; `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, có ba luật dừng.

## 5. Công cụ AI đã dùng

Claude (Anthropic). Dùng để đọc đề, viết code và điền các file hồ sơ. Tự kiểm tra: chạy `python lab13.py` trên dữ liệu thật và đối chiếu từng số với bảng đáp án trong hướng dẫn (A2, A3, A4, B1 đến B4 khớp). Phát hiện một lỗi của AI ở bản đầu: chi phí cả hệ thống chỉ cộng 148 ca chuyển nhân viên thay vì 222 yêu cầu không thành công (cho 5.125 đ thay vì 5.865 đ); đã sửa sau khi đối chiếu.

## 6. Tự đánh giá

Phần A, B và D1 khớp đáp án đối chiếu. Các ngày của kế hoạch pilot và vai trò phụ trách do nhóm chọn, cần Coach xác nhận. Mục 5 của hồ sơ launch (bảng lỗi) phụ thuộc phần của thành viên khác.
